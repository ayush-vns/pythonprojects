data = {}
while True:
    print("0-Exit,1-add,2-search,3-delete,4-all,5-deposit,6-withdrawal")
    option = int(input())
    if option == 0:
        break
    if option == 1:
        print("add")
        name = input("Enter your name  ")
        account_no = int(input(" Enter your account_no "))
        if data.get(account_no) is not None:
            print("already have a account ")
            continue
        deposit = int(input("deposit money "))
        data[account_no] = {"name": name, "balance": deposit}
        continue
    if option == 2:
        print("search")
        account_no = int(input("Enter account_no "))
        if data.get(account_no) is not None:
            value = data[account_no]
            print(account_no, value)
        else:
            print("Not Found")
            continue
    if option == 4:
        print(data)
        continue
    if option == 5:
        print("deposit")
        account_no = int(input("Enter account_no "))
        if data.get(account_no) is None:
            print("Invalid Account No")
            continue
        deposit = int(input("Enter deposit money "))
        if data.get(deposit == -1 or deposit == 0) is None:
            print("invalid ")
            continue
        balance = data[account_no]["balance"]
        new_balance = balance + deposit
        data[account_no]["balance"] = new_balance
        continue
    if option == 6:
        print("withdrawal")
    account_no = int(input("Enter account_no "))
    if data.get(account_no) is None:
        print("Invalid Account No")
        continue
    withdrawal = int(input("Enter withdrawal money "))
    balance = data[account_no]["balance"]
    new_balance = balance - withdrawal
    data[account_no]["balance"] = new_balance
    continue
