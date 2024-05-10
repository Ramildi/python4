class ListSums:
    def add_numbers(self, numbers):
        mylist = []
        for num in numbers:
            mylist.append(num)
        return mylist

    def listCem(self, mylist, target):
        indices = []
        for i in range(len(mylist)):
            for j in range(i + 1, len(mylist)):
                if mylist[i] + mylist[j] == target:
                    indices.append((i, j))
        if indices:
            return indices
        else:
            return -1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 13

Metod = ListSums()
mylist = Metod.add_numbers(numbers)
result = Metod.listCem(mylist, target)

print("List:", mylist)
print("Target:", target)
print("Indices of sum:", result)
