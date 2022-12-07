# AoC Day 4


def load_data(file): 
    data = [line.strip() for line in open(file).readlines()]
    return data


def get_range(elf):
    """Return the upper and lower limits of the ranges for an elf's section."""
    lower, upper = elf.split("-")
    return int(lower), int(upper)


def solution_1(data) -> int:
    """Solve part 1.
    
    Find the number of pairs where one of the ranges fully contains the other.
    
    Two possibilities for containments:
        - Elf 2 range in elf 1 range:
            e_1_lower <= e_2_lower and e_1_upper >= e_2_upper
        - Elf 1 range in elf 2 range:
            e_1_lower >= e_2_lower and e_1_upper <= e_2_upper
    """
    fully_contained_groups = 0
    
    for group in data:
        elf_1, elf_2 = group.split(",")
        elf_1_lower, elf_1_upper = get_range(elf_1)
        elf_2_lower, elf_2_upper = get_range(elf_2)
        
        # Check condition 1
        if elf_1_lower <= elf_2_lower and elf_1_upper >= elf_2_upper:
            fully_contained_groups += 1
        elif elf_1_lower >= elf_2_lower and elf_1_upper <= elf_2_upper:
            fully_contained_groups += 1
    
    return fully_contained_groups


def solution_2(data) -> int:
    """Solve part 2.
    
    Now, find the number of assignment pairs where the ranges overlap.
    
    There are two possibilites for overlaps:
        - Elf 1 range in bottom of elf 2 range:e
             e_1_lower < e_2_lower and e_1_upper <= e_2_upper
        - Elf 1 range in top of elf 2 range:
            e_1_lower >= e_2_lower and e_1_upper > e_2_upper 
        
    We should also check the previous encompassing conditions.
    
    61-79,49-78
    """
    overlapping_groups = 0
    
    for group in data:
        elf_1, elf_2 = group.split(",")
        elf_1_lower, elf_1_upper = get_range(elf_1)
        elf_2_lower, elf_2_upper = get_range(elf_2)
        
        # Check previous encompassing conditions and then our new conditions
        # if elf_1_lower <= elf_2_lower and elf_1_upper >= elf_2_upper:
        #     overlapping_groups += 1
        # elif elf_1_lower >= elf_2_lower and elf_1_upper <= elf_2_upper:
        #     overlapping_groups += 1
        # elif elf_1_lower <= elf_2_lower and elf_1_upper >= elf_2_lower:
        #     overlapping_groups += 1
        # elif elf_1_lower <= elf_2_upper and elf_1_upper >= elf_2_upper:
        #     overlapping_groups += 1
        if elf_1_lower <= elf_2_upper and elf_2_lower <= elf_1_upper:
            overlapping_groups += 1
            
    return overlapping_groups
    

def solve(file):
    """Solve day 4 of the AoC.
    
    Each section of the camp has an ID number, and each Elf is assigned to a
    range of sections.
    
    The elves have overlapping assignments. They pair up in groups of 
    two. 
    """
    data = load_data(file)
    
    answer_1 = solution_1(data)
    print(answer_1)
    
    answer_2 = solution_2(data)
    print(answer_2)
    
    return


if __name__ == "__main__":
    solve("data/04.txt")