data = {}
while True:
    print("0-Exit, 1-Add,2-Search,3-delete,4-all")
    option = int(input())
    if option == 0:
        break
    if option == 1:
        print("Add")
        rollno = input("Enter roll no = ")
        result = input("Enter result = ")
        data[rollno] = result
        continue
    if option == 2:
        print("Search")
        rollno = input("Enter roll no = ")
        result = data.get(rollno, "pass")
        print(result)
        continue
    if option == 3:
        rollno = input("Enter roll no = ")
        data.pop(rollno)
        continue
    if option == 4:
        print(data)
        continue
    print("Invalid")
