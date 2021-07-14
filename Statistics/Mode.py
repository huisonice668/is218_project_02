def mode(data):
    temp_list = []
    count = []
    if len(data) == 0:
        raise ValueError('Can not be an empty list')

    # remove duplicate then store the elements into temp_list
    for num in data:
        if num not in temp_list:
            temp_list.append(num)

    # count the appearance of elements in data
    for num in temp_list:
        counter = data.count(num)
        count.append(counter)

    # find the max count which is the mode
    max = count[0]
    max_index = 0
    for i in range(len(count)):
        if count[i] > max:
            max = count[i]
            max_index = i

    # throw exception if there is no mode aka max = 1
    if max == 1:
        raise StatisticsError('No Mode')

    return temp_list[max_index]
