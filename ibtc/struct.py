class Sale:
    def __init__(self, currency, share_price, date, time, symbol, quantity, closed_lots):
        self.currency = currency
        self.share_price = share_price
        self.data = date
        self.time = time
        self.symbol = symbol
        self.quantity = quantity
        self.closed_lots = closed_lots


class ClosedLot:
    def __init__(self, share_price, date, quantity):
        self.share_price = share_price
        self.date = date
        self.quantity = quantity
