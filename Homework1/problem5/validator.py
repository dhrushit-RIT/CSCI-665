def validate_sequence(sequence):
    prev = sequence[0]
    for i in sequence:
        if i < prev:
            print("problem with sorting")
            print(sequence)
            return False
        else:
            prev = i
    print("Sorting is valid")
    return True
