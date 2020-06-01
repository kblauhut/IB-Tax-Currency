class Sale:
    def __init__(self, currency, share_price, date, time, symbol, quantity, closed_lots):
        self.currency = currency
        self.share_price = share_price
        self.date = date
        self.time = time
        self.symbol = symbol
        self.quantity = quantity
        self.closed_lots = closed_lots

    def get_currency(self):
        return self.currency

    def get_share_price(self):
        return self.share_price

    def get_date(self):
        return self.date

    def get_time(self):
        return self.time

    def get_symbol(self):
        return self.symbol

    def get_quantity(self):
        return self.quantity

    def get_closed_lots(self):
        return self.closed_lots


class ClosedLot:
    def __init__(self, share_price, date, quantity):
        self.share_price = share_price
        self.date = date
        self.quantity = quantity

    def get_share_price(self):
        return self.share_price

    def get_date(self):
        return self.date

    def get_quantity(self):
        return self.quantity
