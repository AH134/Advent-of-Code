
def get_input():
    file = open(r".\input.txt", "r")
    read = file.readlines()
    read = [x.rstrip("\n") for x in read]
    file.close()

    return read

def check_possibilities(file):
    sum = 0;
    cube_map = {
        "red": 12,
        "green": 13,
        "blue": 14,
        }


    for game in file:
        game_list = game.split(":") # splits game number into its own element
        game_subsets = game_list[1].strip().split(";") # splits every subset into its own list
        game_subsets = [x.strip().split(",") for x in game_subsets] # splits subsets color and number into its own element
        game_num = game_list[0].split(" ")[1]
        
        cube_set = []
        
        # creates a map for each subset
        for subset in game_subsets:
            s = {}
            for i in range(len(subset)):
                split_s = subset[i].strip().split(" ")
                s[split_s[1]] = int(split_s[0])
                
            cube_set.append(s)
        
        is_possible = True
        for s in cube_set:
            for key in dict(s).keys():
                if s[key] > cube_map[key]:
                    is_possible = False
                    break
        
        if is_possible:
            sum += int(game_num)
    
    return sum


def minimun_cubes_needed(file):
    sum = 0;

    for game in file:
        game_list = game.split(":") # splits game number into its own element
        game_subsets = game_list[1].strip().split(";") # splits every subset into its own list
        game_subsets = [x.strip().split(",") for x in game_subsets] # splits subsets color and number into its own element
        game_num = game_list[0].split(" ")[1]
        
        cube_set = []
        
        # creates a map for each subset
        for subset in game_subsets:
            s = {}
            for i in range(len(subset)):
                split_s = subset[i].strip().split(" ")
                s[split_s[1]] = int(split_s[0])
                
            cube_set.append(s)
            
        cube_map = {
        "red": 0,
        "green": 0,
        "blue": 0,
        }
        
        for s in cube_set:
            for key in dict(s).keys():
                if s[key] > cube_map[key]:
                    cube_map[key] = s[key]
        
        cube_product = 1
        for key in cube_map:
            cube_product *= cube_map[key]
            
        sum += cube_product
        
    return sum

def main():
    file = get_input()
    sum = check_possibilities(file)
    sum2 = minimun_cubes_needed(file)
    print(sum)
    print(sum2)

if __name__ == "__main__":
    main()