import os

'''
Notes

Part 1
- line either has 1 number
- line either has more than 1 number
- check at end of line to add into sum


Part 2
- letter word are either 3,4,5 letters
- get substr of word if letter digits found
'''

def get_input():
    file = open(r".\input.txt", "r")
    read = file.readlines()
    strip_file = [x.rstrip("\n") for x in read]
    file.close()

    return read, strip_file

def get_line_digits(input):
    sum = 0
    digits = ""

    for line in input:
        for i in range(len(line)):
            if line[i] == "\n":
                if len(digits) == 1:
                    sum += (int(digits[0] + digits[0]))
                elif len(digits) > 1:
                    sum += (int(digits[0] + digits[-1]))
                digits = ""
            if line[i].isnumeric():
                digits += line[i]

    if len(digits) == 1:
        sum += (int(digits[0] + digits[0]))
    else:
        sum += (int(digits[0] + digits[-1]))

    return sum

def get_line_digits_part_2(input):
    sum = 0
    digits = ""
    letter_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    for line in input:
        temp = line;
    
        while temp != "":
            if temp[0].isnumeric():
                digits += temp[0]
                temp = temp[1:]
            elif temp[0:3] in letter_map:
                digits += letter_map[temp[0:3]]
                temp = temp[2:] # save last letter in case of edge cases --> oneight --> one & eight
            elif temp[0:4] in letter_map:
                digits += letter_map[temp[0:4]]
                temp = temp[3:]
            elif temp[0:5] in letter_map:
                digits += letter_map[temp[0:5]]
                temp = temp[4:]
            else:
                temp = temp[1:]
        sum += int(digits[0] + digits[-1])
        digits = ""
    
    return sum                    



def main():
    [read, strip_file] = get_input()
    part_one = get_line_digits(read)
    part_two = get_line_digits_part_2(strip_file)
    print("part 1: ", part_one)
    print("part 2: ", part_two)


if __name__ == "__main__":
    main();