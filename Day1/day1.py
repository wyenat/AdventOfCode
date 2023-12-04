corresponding_table = {
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5, 
        "six" : 6,
        "seven" : 7,
        "eight" : 8, 
        "nine" : 9
    } 

def find_number(line, reversed:bool):
    global corresponding_table
    buffer = "" 
    for c in line:
        if reversed:
            buffer = c + buffer
        else:
            buffer += c
        print(f"Buffer is {buffer}, Line is {line}")
        if c.isnumeric():
            return int(c)
        for key in corresponding_table.keys():
            if key in buffer:
                print(f"Found key={corresponding_table[key]} one in {buffer}")
                return corresponding_table[key]

def day1():
    input_file = "input.file" # I didn't get how to get through API
    total = 0
   
    with open(input_file, "r") as f:
        while line := f.readline():
            num1 = find_number(line, False)
            num2 = find_number(reversed(line), True)
            num = 10*num1 + num2
            print(line, num)
            total += num
    print(total)

if __name__=="__main__":
    day1()