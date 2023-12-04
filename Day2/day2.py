import re
def day2():
    input_file = "input.file"
    game_id = "Game (\d*):"
    blue = "(\d*) blue"
    red = "(\d*) red"
    green = "(\d*) green"

    max_blue = 14
    max_red = 12
    max_green = 13

    # Part 1
    with open(input_file, "r") as f:
        total = 0
        while line := f.readline():
            id = int(re.match(game_id, line).group(1))
            blue_ok = all([int(i)<=max_blue for i in re.findall(blue, line)])
            red_ok = all([int(i)<=max_red for i in re.findall(red, line)])
            green_ok = all([int(i)<=max_green for i in re.findall(green, line)])
            if blue_ok and green_ok and red_ok:
                total += id
        print(total)

    # Part 2
    with open(input_file, "r") as f:
        total = 0
        while line := f.readline():
            blue_needed = max([int(i) for i in re.findall(blue, line)])
            red_needed = max([int(i) for i in re.findall(red, line)])
            green_needed = max([int(i) for i in re.findall(green, line)])
            total += blue_needed * red_needed * green_needed
        print(total)

if __name__=="__main__":
    day2()