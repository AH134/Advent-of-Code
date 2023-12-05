

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
    
    file.close()
    
    return read_list
    

def is_symbol(row, col, input, num, gear_ratio):
    
    for i in range(col - len(num) - 1, col+1):
        if input[row-1][i] == "*":
            gear_coord = f'{row-1}:{i}'
            gear_ratio[gear_coord] = gear_ratio.get(gear_coord, [])
            gear_ratio[gear_coord].append(num)
        # print(input[row-1][i], end="")
    # print()
    
    # for i in range(col - len(num) - 1, col+1):
        # print(input[row][i], end="")
    # print()
    
    if input[row][col - len(num) - 1] == "*":
            gear_coord = f'{row}:{col-len(num) - 1}'
            gear_ratio[gear_coord] = gear_ratio.get(gear_coord, [])
            gear_ratio[gear_coord].append(num)
            
    if input[row][col] == "*":
        gear_coord = f'{row}:{col}'
        gear_ratio[gear_coord] = gear_ratio.get(gear_coord, [])
        gear_ratio[gear_coord].append(num)

    for i in range(col - len(num) - 1, col+1):
        if input[row+1][i] == "*":
            gear_coord = f'{row+1}:{i}'
            gear_ratio[gear_coord] = gear_ratio.get(gear_coord, [])
            gear_ratio[gear_coord].append(num)
        # print(input[row+1][i], end="")
    # print("\n")
    
    return gear_ratio
    


def main():
    input = get_input()
    gear_ratio = {
    }
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
                    gear_ratio = is_symbol(row, col, input, num, gear_ratio)
                    num = "" 
            # check when line is a "."
            elif i != 0 and line[i] == "."  :
                if num != "":
                    gear_ratio = is_symbol(row, col, input, num, gear_ratio)    
                    num = ""
        col = 1
        row += 1
        
        
    for val in gear_ratio.values():
        if len(val) == 2:
            product = int(val[0]) * int(val[1])
            sum += product
            
    print(sum)
    
    
    
if __name__ == "__main__":
    main()