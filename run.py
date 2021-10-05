def fibonacci_linear(number):
    if type(number) == float:
        return 'Choose a intenger'
    if number < 0:
        return "Choose a natural number"
    if number == 0:
        return 0
    elif number == 1:
        return 1
    position_0 = 0
    position_1 = 1
    for iteration in range(2, number + 1, 1):
        position_new = position_0 + position_1
        position_0 = position_1
        position_1 = position_new
        
    return position_1
    
def fibonacci_recursive(number):
    if type(number) == float:
        return 'Choose a intenger'
    if number < 0:
        return "Choose a natural number"
    if number == 0:
        return 0
    if number == 1:
        return 1
    return fibonacci_recursive(number-1) + fibonacci_recursive(number-2)

def prime_linear(number):
    if type(number) == float:
        return 'Choose a intenger'
    if number < 2:
        return "Choose a number higher than one"
    prime_list = []
    for position in range(2, number+1, 1):
        if position == 2:
            prime_list.append(2)
            continue
        for divider in range(2, position, 1):
            if position % divider == 0:
                break
            if divider * divider > position:
                prime_list.append(position)
                break    
    return prime_list
    
def prime_recursive_checker(number, divider = 2):
    if number % divider == 0 :
        return False
    if divider * divider > number:
        return True
    
    return prime_recursive_checker(number, divider + 1)

def prime_recursive(number):
    if type(number) == float:
        return 'Choose a intenger'
    if number < 2:
        return "Choose a number higher than one"
    if number == 2:
        return [2]
    prime_list = [2]
    for position in range(3,number+1,1):
        if prime_recursive_checker(position):
            prime_list.append(position)
    
    return prime_list

def main():
    print("fibonacci position")
    print("Linear function:", fibonacci_linear(6))
    print("Recursive function:", fibonacci_recursive(6))
    print("")
    print("Prime number list")
    print("Linear function:", prime_linear(10))
    print("Recursive function:", prime_recursive(10))

if __name__ == "__main__":
    main()
