# AoC Day 6


def load_data(file):
    data = open(file).readlines()[0]

    return data


def solution_1_2(data, packet_length=4):
    """Solve part 1.
    Given a string of letters, iterate and find the first window of four letters
    that are unique.
    
    Return the index after the end of the window.
    
    E.g.,
    
    aabcde
     ^--^
    012345
    
    Index is 5.
    """
    # Run a sliding window over the message
    for i in range(len(data)):
        characters = data[i:i+packet_length]
        character_count = len(set(characters))
        
        if character_count == packet_length:
            break
    
    return i+packet_length


def solve(file):
    """Solve day 6 of the AoC.
    
    """
    data = load_data(file)
    
    answer_1 = solution_1_2(data, packet_length=4)
    print(answer_1)
    
    answer_2 = solution_1_2(data, packet_length=14)
    print(answer_2)
    
    return



if __name__ == "__main__":
    solve("data/06.txt")