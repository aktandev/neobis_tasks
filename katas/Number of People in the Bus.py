def number(bus_stops):
    in_bus = []
    left_bus = []
    for elem in bus_stops:
        in_bus.append(elem[0])
        left_bus.append(elem[1])

    return sum(in_bus) - sum(left_bus)


print(number([[10, 0], [3, 5], [5, 8]]))  # 5
print(number([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]]))  # 17
print(number([[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]]))  # 21