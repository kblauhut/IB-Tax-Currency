from ibtc.struct import Sale, ClosedLot
import datetime
import requests
import csv


def main():
    obj_arr = csv_to_obj('ibreport.csv')
    create_output_csv(obj_arr, "EUR")


def csv_to_obj(path):
    obj_arr = []

    with open(path, newline='') as csvfile:
        reader = list(csv.reader(csvfile))
        for i, row in enumerate(reader):
            closed_lots_arr = []
            if row[0] == "Trades" and row[2] == "Trade" and row[3] == "Stocks":
                if float(row[13]) != 0:
                    pass
                n = i + 1
                while reader[n][2] == "ClosedLot":
                    closed_lot = ClosedLot(
                        float(reader[n][9]), date_reformat(reader[n][6]), int(reader[n][8]))
                    closed_lots_arr.append(closed_lot)
                    n = n+1
            if len(closed_lots_arr) != 0:
                date = get_date(row[6])
                time = get_time(row[6])
                sale = Sale(row[4], float(row[9]), date, time,
                            row[5], int(row[8]), closed_lots_arr)
                obj_arr.append(sale)
    return obj_arr


def create_output_csv(obj_arr, currency):
    with open('out.csv', 'w', newline='', encoding='utf8') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(["Stückzahl", "Symbol", "Kaufdatum", "Kaufpreis (" + currency + ")",
                         "Verkaufdatum", "Verkaufserlös (" + currency + ")", "Gewinn/Verlust"])

        for obj in obj_arr:
            create_rows(writer, obj, currency)


def create_rows(writer, obj, currency):
    sale_exchange_rate = get_exchange_rate(
        obj.get_date(), currency, obj.get_currency())
    sale_share_price = exchange(sale_exchange_rate, obj.get_share_price())

    for closed_lot in obj.get_closed_lots():
        closed_lot_row = []

        lot_exchange_rate = get_exchange_rate(
            closed_lot.get_date(), currency, obj.get_currency())
        lot_share_price = exchange(
            lot_exchange_rate, closed_lot.get_share_price())

        closed_lot_row.append(closed_lot.get_quantity())
        closed_lot_row.append(obj.get_symbol())
        closed_lot_row.append(closed_lot.get_date())
        closed_lot_row.append(
            round(lot_share_price * closed_lot.get_quantity(), 2))
        closed_lot_row.append(obj.get_date())
        closed_lot_row.append(
            round(sale_share_price * closed_lot.get_quantity(), 2))
        closed_lot_row.append(round(sale_share_price * closed_lot.get_quantity() -
                                    lot_share_price * closed_lot.get_quantity(), 2))

        writer.writerow(closed_lot_row)


def get_exchange_rate(date, currency, base_currency):
    if currency == base_currency:
        return 1
    url = "https://api.exchangeratesapi.io/" + date + "?base=" + base_currency
    response = requests.get(url)
    return response.json()["rates"][currency]


def exchange(exchange_rate, value):
    return value * exchange_rate


def get_date(date_time_str):
    index = date_time_str.index(",")
    return date_reformat(date_time_str[:index])


def get_time(date_time_str):
    index = date_time_str.index(" ")
    return date_time_str[index+1:]


def date_reformat(date_str):
    if date_str.index("-") == 4:
        return date_str

    index = len(date_str) - 2
    date_str = date_str[:index] + "20" + date_str[index:]
    format_str = "%d-%m-%Y"
    datetime_obj = datetime.datetime.strptime(date_str, format_str)
    return str(datetime_obj.date())
