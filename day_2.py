##Day-2

##Question 1

hw_list = ["apple", "banana", "melon", "watermelon"]

print(len(hw_list)) #length of this list is 4

hw_list_first = hw_list[0:2]
print(hw_list_first)
hw_list_last = hw_list[2:4]
print(hw_list_last)

hw_list_new = hw_list_last + hw_list_first
print(hw_list_new)



##Question 2

def even_numbers():
    usr_input = int(input("Please enter a number: "))
    
    if usr_input < 0:
        print("Enter a bigger number!")
    elif usr_input > 10:
        print("Enter a smaller number!")
    else:
        for i in range(usr_input + 1):
            if i % 2 == 0:
                print(i)

even_numbers()

