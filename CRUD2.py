def create(myLst=None):
    if myLst is None:
        myLst = []

    while True:
        myDict = {"name": input("Name: "), "age": input("Age: "), "contact": input("Contact: ")}

        if not myDict["name"].isalpha() or not myDict["age"].isdigit() or not myDict["contact"].isnumeric():
            print("Incorrect")
        else:
            print("Correct")
            break

    myLst.append(myDict)


def read(myLst=None):
    if len(myLst) == 0:
        print("Database is not exist")
        myLst = []
        return

    for i in myLst:
        print(i)


def update(myLst=None):
    if len(myLst) == 0:
        print("Database is not exist")
        myLst = []
        return

    print("which one of the data do want to update? ")
    name = input("Enter the Name: ")
    for i in range(len(myLst)):
        if name == myLst[i]["name"]:
            myLst[i] = {"name": input("Name: "), "age": int(input("Age: ")), "contact": input("Contact: ")}
            break
    else:
        print("the key is not exist")


def delete(myLst=None):
    if len(myLst) == 0:
        print("Database is not exist")
        myLst = []
        return

    read(myLst)

    print("which one of the data do want to delete? ")
    name = input("Enter the Name: ")

    for i in range(len(myLst)):
        if name == myLst[i]["name"]:
            del myLst[i]
            break
    else:
        print("the key is not exist")


if __name__ == "__main__":
    myLst = []
    while True:
        print("MENU")
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")
        menu = int(input("Menu (1/2/3/4) : "))

        if menu == 1:
            create(myLst)
        elif menu == 2:
            read(myLst)
        elif menu == 3:
            update(myLst)
        elif menu == 4:
            delete(myLst)
        else:
            break

