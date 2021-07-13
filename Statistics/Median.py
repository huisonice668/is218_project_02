from Statistics.Mean import Mean


def median(data):
    index = 0
    list = []
    data = data.sort()
    counter = len(data)
    if counter % 2 == 0:
        index = counter / 2
        list[0] = data[index - 1]
        list[1] = data[index]
        return mean(list)
    else:
        return data[counter // 2]