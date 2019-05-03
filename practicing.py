#!/bin/python3
from argparse import ArgumentParser
from math import sqrt
from csv import reader


def handle_parser():
    parser = ArgumentParser(usage='./tsp.py <country> [<algorithm>]')
    parser.add_argument('country', help='the start country')
    parser.add_argument('-t', '--type', help='select the algorithm',
                        choices=['K-NN', 'BaB'])
    args = parser.parse_args()
    return args


def get_data(file):
    content = []
    with open(file) as csv_file:
        readerable = reader(csv_file)
        for row in readerable:
            content.append(row)
    return content


def find_shortest_city(city, content):
    global total_len
    min = 0
    target_city = ()
    count = 0
    count2 = 0
    for other_cities in content:
        distace = find_distance(city, other_cities)
        if min == 0:
            min = distace
            target_city = other_cities
            count2 = count
        elif min > distace:
            min = distace
            target_city = other_cities
            count2 = count
        count += 1
    total_len += min
    return target_city, count2


def check_single_city(country):
    global total_len
    content = get_data(country)
    origin = content[0]
    city_information = content.pop(0)
    while len(content) != 1:
        city_information, count = find_shortest_city(city_information, content)
        print(city_information)
        content.pop(count)
    print(content[0])
    total_len += find_distance(origin, content[0])
    return total_len


def find_distance(city1, city2):
    distance = sqrt((float(city1[1]) - float(city2[1])) ** 2 +
                    (float(city1[2]) - float(city2[2])) ** 2)
    return distance


def use_bab(country):
    pass


def main():
    args = handle_parser()
    if args.country in ['china_cities.csv', 'vietnam_cities.csv',
                        'usa_cities.csv']:
        len  = check_single_city(args.country)
        print(len)
    else:
        print("Invalid file")
        return


if __name__ == '__main__':
    total_len = 0
    main()