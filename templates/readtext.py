
with open('popular_foods.txt','r') as f:
    data = f.readlines()
    ss = 'American'
    lists = []
    for line in data:
        result = ss in line.split()
        print(line)
        print(result)
        if result is True :
            lists.append(line[0:len(line)-1])

    print(lists)