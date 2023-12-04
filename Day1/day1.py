def day1():
    input_file = "input.file" # I didn't get how to get through API
    total = 0
    with open(input_file, "r") as f:
        while line := f.readline():
            filter_input =[c for c in line if c.isnumeric()]
            value = int(f"{filter_input[0]}{filter_input[-1]}")
            print(value)
            total += value
    print(total)

if __name__=="__main__":
    day1()