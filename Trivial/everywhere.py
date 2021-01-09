num_trips = int(input())
for trips in range(num_trips):
    city_list = []
    num_cities = int(input())
    for cities in range(num_cities):
        city_list.append(input())
    city_list = set(city_list)
    print(len(city_list))
