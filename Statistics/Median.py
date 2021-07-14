from Statistics.Mean import mean


def median(data):
    index = 0
    result = []
    data.sort()
    counter = len(data)

    # throw exception if list is empty
    if counter == 0:
        raise ValueError('Can not have an empty list')

    if counter % 2 == 0:
        index = counter // 2
        result.append(data[index - 1])
        result.append(data[index])
        return mean(result)
    else:
        return data[counter // 2]