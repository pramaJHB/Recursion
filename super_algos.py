
def find_min(element):
    """TODO: complete for Step 1"""
    try:
        if all(isinstance(i, int) for i in element) != True:
            return -1
        if len(element) == 0:
            return -1
        if len(element) == 1:
            return element[0]
        else:
            if element[0] < find_min(element[1:]):
                return element[0]
            else:
                return find_min(element[1:])
    except (ValueError, TypeError):
        return -1


def sum_all(element):
    """TODO: complete for Step 2"""
    try:
        if all(isinstance(i, int) for i in element) != True:
            return -1
        if len(element) == 0:
            return -1
        if len(element) == 1:
            return element[0]
        else:
            return element[0] + sum_all(element[1:])
    except (ValueError, TypeError):
        return -1


def find_possible_strings(character_set, n):
    """TODO: complete for Step 3"""
    try:
        if all(isinstance(i, str) for i in character_set) != True:
            return []
        if len(character_set) == 0 or n == 0:
            return []
        if n == 1:
            return character_set
        else:
            result_list = []
            for prefix in character_set:
                for next_character in find_possible_strings(character_set, n - 1):
                    result_list.append(prefix + next_character)
            return result_list
    except (ValueError, TypeError):
        return []

