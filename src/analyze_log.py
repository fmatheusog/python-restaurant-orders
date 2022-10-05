import csv
import os

def most_ordered_by_name(orders, name):
    filtered = []

    for order in orders:
        if order[0] == name:
            filtered.append(order[1])

    return max(set(filtered), key=filtered.count)


def times_ordered_by_food_and_name(orders, name, food):
    count = 0

    for order in orders:
        if order[0] == name and order[1] == food:
            count += 1

    return count


def never_ordered_by_name(orders, name):
    foods = set()
    ordered_foods = set()

    for order in orders:
        foods.add(order[1])

        if order[0] == name:
            ordered_foods.add(order[1])

    return foods.difference(ordered_foods)


def days_never_visited_by_name(orders, name):
    days = set()
    days_visited = set()

    for order in orders:
        days.add(order[2])

        if order[0] == name:
            days_visited.add(order[2])

    return days.difference(days_visited)


def read(path_to_file):
    if not os.path.exists(path_to_file):
        raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")

    if ".csv" not in path_to_file:
        raise FileNotFoundError(f"Extensão inválida: {path_to_file}")


    with open(path_to_file) as file:
        return list(csv.reader(file))

def write(path, data):
    with open(path, encoding="utf-8") as file:
        for line in data:
            file.writelines(line)


def analyze_log(path_to_file):
    data = read(path_to_file)

    maria_most = most_ordered_by_name(data, "maria")
    arnaldo_hamburguer = times_ordered_by_food_and_name(data, "arnaldo", "hamburguer")
    joao_never = never_ordered_by_name(data, "joao")
    joao_never_went = days_never_visited_by_name(data, "joao")

    output = [
        f"{maria_most}\n",
        f"{arnaldo_hamburguer}\n",
        f"{joao_never}\n",
        f"{joao_never_went}\n",
    ]

    write("data/mkt_campaign.txt", output)
