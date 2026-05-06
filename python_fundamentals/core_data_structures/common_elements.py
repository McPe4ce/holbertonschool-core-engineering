#!/usr/bin/env python3

def common_elements(set_1, set_2):
    common_set = set()

    for valor in set_1:
        if valor in set_2:
            common_set.add(valor)
    return common_set


if __name__ == "__main__":
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    print(sorted(list(common_elements(set_1, set_2))))
