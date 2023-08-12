from itertools import permutations

def allCombinations(list, source, destination):
    result = []
    for combo in permutations(list, len(list)):
        if len(combo) == len(list) and str(combo[0]) == source and str(combo[len(list)-1]) == destination:
            result.append(combo)

    return result
