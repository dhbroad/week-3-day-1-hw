# Write a function that accepts a sequence of unique integers between 0 and 9 (inclusive), and returns the missing element.
a = [0, 5, 1, 3, 2, 9, 7, 6, 4] #--> 8
b = [9, 2, 4, 5, 7, 0, 8, 6, 1] #--> 3
c = [0, 1, 2, 3, 4, 5, 6, 7, 8] #--> 9

def missingInteger(list):
    list.sort() 
    for index in range(len(list)):
        if index == len(list)-1:
            return list[index]+1
        if list[index]+1 == list[index+1]:
            continue
        else:
            return list[index]+1

print(missingInteger(a))