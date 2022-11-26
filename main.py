list1 =  [1, 5, 3, 4, 5, 7, 7, 180, 13, 130]
statements = ['\nMenu:','1.) Add an element','2.) Insert an element','3.) Modify an element','4.) Delete an element', '5.) Arrange in ascending order', '6.) Arrange in descending order']
line_break_list= '\n'.join(statements)
print('Array:', list1, line_break_list)

process = int(input('\nWhat do you want to do? (1-6): '))

if process == 1:
    add = int(input('Add this number to the end of the list: '))
    list1.append(add)
    print("The element has successfully been appended :)")
    print('this is the new array:',list1)

elif process == 2:
    ins = int(input('Insert this number: '))
    pos = int(input('In which position: '))-1
    list1.insert(pos,ins)
    print("The element has successfully been inserted :D")
    print('this is the new array:', list1)

elif process == 3:
    mod = int(input('Position of element to modify: '))-1
    new = int(input('Replace it with: '))
    list1[mod] = new
    print("The element has successfully been modified :0")
    print('this is the new array:', list1)

elif process == 4:
    print("1: Choose specific element\n2: Choose element in position #")
    remove = int(input('Selection:'))
    if remove == 1:
        rem = int(input('Input the element you want to remove: '))
        list1.remove(rem)
        print("The element has successfully been removed :(")
        print('this is the new array:', list1)
    elif remove == 2:
        pos = int(input('Input the position of the element: '))-1
        list1[pos] = (99999)
        list1.remove(99999)
        print("The element has successfully been removed :(")
        print('this is the new array:', list1)

elif process == 5:
    list1.sort()
    print("The list has been sorted in ascending order :>")
    print('this is the new array:', list1)

elif process == 6:
    list1.sort()
    list1.reverse()
    print("The list has been sorted in descending order :<")
    print('this is the new array:', list1)

else:
    print("ERROR! Please select an integer from 1-6 inclusive")

