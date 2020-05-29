from ibtc.struct import Sale, ClosedLot
import requests
import csv


def main():
    obj_arr = csv_to_obj('test-csv/ibreport.csv')
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
                        float(reader[n][9]), reader[n][6], int(reader[n][8]))
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
    with open('test-csv/out.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        for obj in obj_arr:
            writer.writerow(["Symbol", "Date", "Quantity",
                             "Share Price " + currency, "Basis " + currency])
            create_row(writer, obj, currency)
            writer.writerow(["", "", "", "", ""])


def create_row(writer, obj, currency):
    sale_exchange_rate = get_exchange_rate(
        obj.get_date(), currency, obj.get_currency())
    sale_proceeds = exchange(
        sale_exchange_rate, obj.get_share_price()) * abs(obj.get_quantity())
    print(sale_proceeds)


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
    return date_time_str[:index]


def get_time(date_time_str):
    index = date_time_str.index(" ")
    return date_time_str[index+1:]