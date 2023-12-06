def isValidNumber(matrix, x_pos, y_pos) -> bool:
    length = len(matrix)
    width = len(matrix[0])
    if (x_pos < 0 or y_pos < 0 or x_pos > width - 1 or y_pos > length - 1):
        return False
    if matrix[y_pos][x_pos].isnumeric():
        return True
    return False

def propagate(matrix, x_pos, y_pos, propagated) -> str:
    if x_pos < 0 or x_pos > len(matrix[0])-1:
        return ""
    if matrix[y_pos][x_pos] == ".":
        return ""
    if propagated[y_pos][x_pos]:
        return ""
    propagated[y_pos][x_pos] = True
    return f"{propagate(matrix, x_pos-1, y_pos, propagated)}{matrix[y_pos][x_pos]}{propagate(matrix, x_pos+1, y_pos, propagated)}"

def around(matrix, x_pos, y_pos, propagated) -> list:
    result = []
    if isValidNumber(matrix, x_pos- 1, y_pos- 1):
        result.append(propagate(matrix, x_pos- 1,y_pos- 1, propagated))
    if isValidNumber(matrix, x_pos- 1, y_pos):
        result.append(propagate(matrix, x_pos- 1, y_pos, propagated))
    if isValidNumber(matrix, x_pos- 1, y_pos+ 1):
        result.append(propagate(matrix, x_pos- 1, y_pos+ 1, propagated))
    if isValidNumber(matrix, x_pos, y_pos- 1):
        result.append(propagate(matrix, x_pos, y_pos- 1, propagated))
    if isValidNumber(matrix, x_pos, y_pos+ 1):
        result.append(propagate(matrix, x_pos, y_pos+ 1, propagated))
    if isValidNumber(matrix, x_pos+ 1, y_pos- 1):
        result.append(propagate(matrix, x_pos+ 1, y_pos- 1, propagated))
    if isValidNumber(matrix, x_pos+ 1, y_pos):
        result.append(propagate(matrix, x_pos+ 1, y_pos, propagated))
    if isValidNumber(matrix, x_pos+ 1, y_pos+ 1):
        result.append(propagate(matrix, x_pos+ 1, y_pos+ 1, propagated))
    print(f"For char {matrix[y_pos][x_pos]} at {x_pos}, {y_pos} : {result=}")
    return filter(len, result)

def find_special_char(line):
    special_char_position = []
    for e, char in enumerate(line):
        if not (char.isnumeric() or char == "." or char == "\n"):
            special_char_position.append(e)
    return special_char_position
 
def day3():
    input_file = "input.file"
    matrix = []
    total = 0
    
    # Part 1
    with open(input_file, "r") as f:
        while line := f.readline():
          matrix.append(line)
    
    propagated = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for y_pos, line in enumerate(matrix):
        for x_pos in find_special_char(line):
            propagated[y_pos][x_pos] = True
            line_result = around(matrix, x_pos, y_pos, propagated)
            total += sum(map(int, line_result))
    
    print(total)

    

if __name__=="__main__":
    day3()