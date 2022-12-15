import json


def create(file=None):
    if file is None:
        file = open("myFile.txt", "w")
    else:
        file = open("myFile.txt", "a")

    while True:
        myDict = {"name": input("Name: "), "age": input("Age: "), "contact": input("Contact: ")}

        if not myDict["name"].isalpha() or not myDict["age"].isdigit() or not myDict["contact"].isnumeric():
            print("Incorrect")
        else:
            print("Correct")
            break

    file.write(str(myDict) + "\n")


def read(file=None):
    if file is None:
        print("Database is not exist")
        return
    else:
        file = open("myFile.txt", "rt")

    for f in file:
        print(f, end="")


def update(file=None):
    if file is None:
        print("Database is not exist")
        return
    file = open("myFile.txt", "rt")

    lst = []
    for f in file:
        f = json.loads(f.replace("'", '"').replace("\n", ""))
        lst.append(f)

    read(file)
    name = input("which one of the data do you want to update? Enter the Name: ")
    for i in range(len(lst)):
        if lst[i]["name"] != name:
            continue
        else:
            lst[i] = {"name": input("Name: "), "age": input("Age: "), "contact": input("Contact: ")}
            break
    else:
        print("the key is not exist")

    file = open("myFile.txt", "w")
    for i in lst:
        file.write(str(i) + "\n")


def delete(file=None):
    if file is None:
        print("Database is not exist")
        return
    lst = []
    file = open("myFile.txt", "rt")
    for f in file:
        f = json.loads(f.replace("'", '"').replace("\n", ""))
        lst.append(f)

    read(file)
    name = input("which one of the data do want to delete? Name: ")
    for i in range(len(lst)):
        if lst[i]["name"] != name:
            continue
        else:
            del lst[i]
            break
    else:
        print("the key is not exist")

    file = open("myFile.txt", "w")
    for i in lst:
        file.write(str(i) + "\n")


if __name__ == "__main__":
    myLst = []
    file = open("myFile.txt", "a")
    while True:
        print("MENU")
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")
        menu = int(input("Menu (1/2/3/4) : "))

        if menu == 1:
            create(file)
        elif menu == 2:
            read(file)
        elif menu == 3:
            update(file)
        elif menu == 4:
            delete(file)
        elif menu == 5:
            print("exit program")
            break
        else:
            print("error input")
            continue

        file.close()
