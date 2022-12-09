# AoC Day 5


def load_crates(raw_crate_data) -> list:
    """Convert the text crate info into a list."""
    columns = [[] for _ in range(int(raw_crate_data[-1][-2]))]
    
    for row in raw_crate_data[:-1]:
        for i in range(1, len(row), 4):
            if row[i] != " ":
                columns[(i-1)//4].insert(0, row[i])

    return columns

def load_instructions(raw_instructinos) -> list:
    """Convert the text instructions into numeric instructions."""
    instructions = []
    
    for instruction in raw_instructinos:
        instruction = instruction.split(" ")
        instructions.append([int(instruction[i]) for i in [1, 3, 5]])
        
    return instructions


def load_data(file):
    """Load the input data.
    
    The top section of the data represents the crates.
    The bottom section represents the instructions.
    
    The instructions are separated by a blank line.
    
    Each crate item is bracketed. An empty space on a crate column is represented
    by three spaces.
    """
    crates = []
    instructions = []
    data = [line.strip("\n") for line in open(file).readlines()]
    
    separator = data.index("")
    
    crates = load_crates(data[:separator])
    instructions = load_instructions(data[separator+1:])
    
    return crates, instructions



def solution_1_2(crates, instructions, CrateMover9001 = False):
    """Solve part 1.
    
    Rearrange the crates according to the instructions.
    
    The first index of the instruction indicates how many crates to move.
    The second index indicates which column to move crates from. 
    The third index indicates which column to move the crates to.
    """
    for instruction in instructions:
        number_of_crates, source, target = instruction

        # Get the crates to move
        crates_to_move = crates[source-1][-number_of_crates:]
        del(crates[source-1][-number_of_crates:])
        
        # CrateMover 9000 vs 9001
        if not CrateMover9001:
            crates_to_move.reverse()
        
        # Add them to the new column
        crates[target-1].extend(crates_to_move)
        
    # Now get the top create letter for each column, if it exists
    letters = []
    for column in crates:
        if column:
            letters.append(column[-1])
    return "".join(letters)


def solve(file):
    """Solve day 5 of the AoC.
    
    """
    crates, instructions = load_data(file)
    answer_1 = solution_1_2(crates, instructions)
    print(answer_1)
    
    crates, instructions = load_data(file)
    answer_2 = solution_1_2(crates, instructions, CrateMover9001=True)
    print(answer_2)
    
    return

if __name__ == "__main__":
    solve("data/05.txt")