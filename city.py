import csv


def read_file(filename):
    f = open(filename, 'r')
    reader = csv.reader(f)
    reader.__next__()
    data = []
    city = []

    for line in reader:
        city.append(line[0])
        data.append(line[1:])

    return data, city


def write_file(filename, data, city):
    f = open(filename, 'w', newline='')
    csv_writer = csv.writer(f)
    csv_writer.writerow(["城市", "year", "data"])
    for i in range(len(data)):
        for j in range(len(data[i])):
            csv_writer.writerow([city[i], 2010+j, data[i][j]])


if __name__ == "__main__":
    data, city = read_file('城市信用指数.csv')
    write_file('城市信用指数-修改.csv', data, city)

