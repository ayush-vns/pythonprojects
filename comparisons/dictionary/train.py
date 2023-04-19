data = {}
while True:
    print("0-exit,1-add,2-search,3-delete,4-all,5-name,6-train")
    option = int(input())
    if option == 0:
        break
    if option == 1:
        print("add")
        train_no = input(" Enter train no =")
        train_name = input("Enter train name ")
        start_station = input("Enter start station ")
        End_station = input("Enter last station ")
        data[train_no] = (train_name, start_station, End_station)
        continue
    if option == 2:
        print("search")
        train_no = input("Enter train no ")
        if data.get(train_no) is not None:
            value = data[train_no]
            print(train_no, value)
        else:
            print("Not Found")
        # print(data)
        continue
    if option == 3:
        train_no = input("Enter train no ")
        data.pop(train_no)
        continue
    if option == 4:
        print(data)
        continue
    if option == 5:
        name = input("Enter your name  ")
        for item in data.values():
            if item[0] == name:
                print(item)
    if option == 6:
        start_station = input("Enter start station ")
        End_station = input("Enter last station ")
        for item in data.values():
            if item[1] == start_station and item[2]==End_station:
                print(item)
        continue


