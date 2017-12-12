
# Fake input needed
test = open('test_cases/input_4', 'r').readlines()

idx = 0
def input():
    global idx
    rs = test[idx]
    idx += 1
    return rs

###############
def parse():
    l = input()
    l = l.strip()
    l = l.split(' ')
    return l

def make_road(cities, city_1, city_2):
    cities[city_1].append(city_2)
    cities[city_2].append(city_1)


def expand_group(cities, start):
    visited = set()
    tovisit = set([start])
    while len(tovisit) > 0:
        on = tovisit.pop()
        visited.add(on)
        for item in cities[on]:
            if item not in visited:
                visited.add(item)
                tovisit.add(item)
    return visited

def fetch_groups(cities):
    groups = []
    unvisited = set(cities.keys())
    while len(unvisited) > 0:
        start = unvisited.pop()
        group = expand_group(cities, start)
        groups.append(group)
        for item in group:
            try:
                unvisited.remove(item)
            except KeyError:
                pass
    return groups

def make_cities(n_cities, n_roads):
    cities = {str(c): [] for c in range(1, n_cities + 1)}
    for j in range(n_roads):
        res = parse()
        city_1, city_2 = res
        make_road(cities, city_1, city_2)
    return cities


def calculate_costs(cities, lib_cost, road_cost):
    # Hack result in case libraries are cheaper/same as roads
    if lib_cost <= road_cost:
        return len(cities) * lib_cost

    # Otherwise
    groups = fetch_groups(cities)

    cost = 0
    for group in groups:
        tot_road_cost = (len(group) - 1) * road_cost
        cost += lib_cost + tot_road_cost
    return cost

def do_one():
    n_cities, n_roads, lib_cost, road_cost = [int(i) for i in parse()]
    
    cities = make_cities(n_cities, n_roads)

    cost = calculate_costs(cities, lib_cost, road_cost)
    return cost


q = int(input().strip())
for i in range(q):
    print(do_one())
