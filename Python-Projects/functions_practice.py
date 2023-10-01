def hello(user_name):
    return f"Hello, {user_name}! how are you today?"

def pack(arg_0, arg_1, arg_2):
    return [arg_0, arg_1, arg_2]

def eat_lunch(lunch_items):
    if len(lunch_items) == 0:
        print("My lunch box is empty")
    else:
        for index in range(len(lunch_items)):
            if index == 0:
                print(f"First I eat {lunch_items[index]}")
            else:
                print(f"Next I eat {lunch_items[index]}")


hello("Jason")
print(pack("apples", "oranges", "bananas"))
eat_lunch(pack("apples", "oranges", "bananas"))