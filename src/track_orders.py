from collections import Counter


class TrackOrders:
    def __init__(self):
        self.all_orders = []

    def __len__(self):
        return len(self.all_orders)

    def add_new_order(self, customer, order, day):
        self.all_orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        orders = []

        for order in self.all_orders:
            if order[0] == customer:
                orders.append(order[1])

        return max(set(orders), key=orders.count)

    def get_never_ordered_per_customer(self, customer):
        foods = set()
        ordered_foods = set()

        for order in self.all_orders:
            foods.add(order[1])

        if order[0] == customer:
            ordered_foods.add(order[1])

        return foods.difference(ordered_foods)

    def get_days_never_visited_per_customer(self, customer):
        days = set()
        days_visited = set()

        for order in self.all_orders:
            days.add(order[2])

        if order[0] == customer:
            days_visited.add(order[2])

        return days.difference(days_visited)

    def get_busiest_day(self):
        days = list()

        for order in self.all_orders:
            days.append(order[2])

        return Counter(days).most_common(1)[0][0]

    def get_least_busy_day(self):
        orders = list()

        for order in self._data:
            orders.append(order[2])

        return min(set(orders), key=orders.count)
