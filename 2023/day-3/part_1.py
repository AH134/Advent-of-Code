

def get_input():
    file = open(r"input.txt", "r")
    read = file.readlines()
    read_list = []
    dummy = ""
    for _ in range(len(read[0])+1):
        dummy += "."
        
    read_list.append(dummy)
    for line in read:
        stripped_line = line.rstrip("\n")
        read_list.append(f'.{stripped_line}.')
    read_list.append(dummy)
    
    
    for line in read_list:
        print(line)
    print("\n")
    
    file.close()
    
    return read_list
    

def is_symbol(row, col, input, num):
    symbol_exists = False
    
    for i in range(col - len(num) - 1, col+1):
        if input[row-1][i] != ".":
            symbol_exists = True
        print(input[row-1][i], end="")
    print()
    
    for i in range(col - len(num) - 1, col+1):
        print(input[row][i], end="")
    print()
    
    if input[row][col - len(num) - 1] != ".":
            symbol_exists = True
            
    if input[row][col] != ".":
        symbol_exists = True

    for i in range(col - len(num) - 1, col+1):
        if input[row+1][i] != ".":
            symbol_exists = True
        print(input[row+1][i], end="")
        
    print("\n")
    return symbol_exists
    
    


def main():
    input = get_input()
    sum = 0
    
    row = 0
    for line in input:
        num = ""
        col = 1
        for i in range(len(line)):
            if line[i].isdigit():
                num += line[i]
                col = i + 1
            # check when line is a symbol
            elif line[i] != "." and num != "" and line[i].isdigit() == False:
                    if is_symbol(row, col, input, num) == True:
                        sum += int(num)
                        num = ""
            # check when line is a "."
            elif i != 0 and line[i] == "."  :
                if num != "":
                    if is_symbol(row, col, input, num) == True:
                        sum += int(num)
                    num = ""    
                    
        col = 1
        row += 1

    print(sum)
    
    
    
if __name__ == "__main__":
    main()