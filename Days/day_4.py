"""--- Day 4: Secure Container ---
You arrive at the Venus fuel depot only to discover it's protected by a password.
The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?

Your puzzle answer was 1063.

--- Part Two ---
An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
How many different passwords within the range given in your puzzle input meet all of the criteria?

Your puzzle answer was 686.

Both parts of this puzzle are complete! They provide two gold stars: **"""

puzzle_input = (246540, 787419)

my_l = [str(x) for x in range(puzzle_input[0], puzzle_input[1] + 1)]


# PART 1 #
def is_password(num):
    if num.count(num[0]) == 6:
        return 1
    else:
        sequence = 0

        for i in range(len(num) - 1):
            if num[i] < num[i + 1]:
                continue
            elif num[i] > num[i + 1]:
                return 0
            elif num[i] == num[i + 1]:
                sequence += 1
                continue

        if sequence >= 1:
            return 1
        elif sequence == 0:
            return 0


output_11 = list(map(is_password, my_l))
output_21 = list(filter(lambda x: x > 0, output_11))
output_121 = [(my_l[x], output_11[x]) for x in range(len(output_11))]
output_121 = list(filter(lambda x: x[1] > 0, output_121))
print(len(output_121))


# PART 2 #
def is_password_2(num):
    if num.count(num[0]) == 6:
        return 0
    else:
        doubled = list()

        for i in range(len(num) - 1):
            if num[i] < num[i + 1]:
                continue
            elif num[i] > num[i + 1]:
                return 0
            elif num[i] == num[i + 1]:
                doubled.append((num[i]))
                continue
            else:
                return 0

        if len(doubled) > 0:
            new_doubled = [True if doubled.count(doubled[-1]) == 1 or doubled.count(doubled[0]) == 1 else None for _ in
                           doubled]

            if all(new_doubled):
                return 1
            else:
                return 0
        else:
            return 0


output_1 = list(map(is_password_2, my_l))
output_2 = list(filter(lambda x: x > 0, output_1))
output_12 = [(my_l[x], output_1[x]) for x in range(len(output_1))]
output_12 = list(filter(lambda x: x[1] > 0, output_12))
print(len(output_12))
