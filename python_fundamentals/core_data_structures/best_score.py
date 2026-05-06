#!/usr/bin/env python3

def best_score(a_dictionary):

    if a_dictionary is None:
        return None

    zabestkey = next(iter(a_dictionary))
    hbomax = a_dictionary[zabestkey]

    for actual_max_key in a_dictionary:
        if a_dictionary[actual_max_key] > hbomax:
            zabestkey = actual_max_key
            hbomax = a_dictionary[zabestkey]
    return zabestkey


if __name__ == "__main__":
    scores = {'John': 12, 'Bob': 14, 'Mike': 15, 'Molly': 16, 'Adam': 10}
    print(best_score(scores))
    print(best_score(None))
