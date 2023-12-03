def hello():
    print("Hello, user!")

hello() 

def pack(arg1, arg2, arg3):
    packed_list = [arg1, arg2, arg3]
    return packed_list

result = pack("apple", 42, [1, 2, 3])
print(result)

def eat_lunch(food_list):
    if not food_list:
        print("My lunchbox is empty!")
    else:
        print("First I eat {}".format(food_list[0]))
        for item in food_list[1:]:
            print("Next I eat {}".format(item))

food_items = ["sandwich", "chips", "apple"]
eat_lunch(food_items)




