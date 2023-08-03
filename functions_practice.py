def Hello():
    print("Hello")

Hello()



def Pack(x,y,z):
    my_list = [x,y,z]
    print(my_list)

Pack(4,56,7)


def eat_lunch(my_list):
    if len(my_list) == 0:
        print("My Lunchbox is Empty!")
    
    for index, value in enumerate(my_list):
        if index == 0:
            print("First I eat " + value)
        else:
            print("Then I eat " + value)


eat_lunch(["Apple", "Sandwich", "Peanuts", "Chicken", "Ice Cream"])

eat_lunch([])