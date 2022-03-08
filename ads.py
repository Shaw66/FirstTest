import csv


def read_file(filename):
    f = open(filename, 'r', encoding='utf-8')
    reader = csv.reader(f)
    reader.__next__()
    data = []
    name = []
    num = []
    type = []

    for line in reader:
        num.append(line[0])
        name.append(line[1])
        data.append(line[2:-1])
        type.append(line[-1])

    return data, name, num, type


def write_file(filename, data, num, name, type):
    f = open(filename, 'w', newline='')
    csv_writer = csv.writer(f)
    csv_writer.writerow(["代码", "名称", "year", "data", "行业"])
    for i in range(len(data)):
        for j in range(len(data[i])):
            csv_writer.writerow([num[i], name[i], 2011+j, data[i][j], type[i]])


if __name__ == "__main__":
    data, name, num, type = read_file('沪深A股上市公司广告宣传推广费(销售费用)+2011-2020年-皮皮侠.csv')
    write_file('沪深A股上市公司广告宣传推广费(销售费用)+2011-2020年-皮皮侠-修改.csv', data, num, name, type)

