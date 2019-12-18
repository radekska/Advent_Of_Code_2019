"""--- Day 3: Crossed Wires ---
The gravity assist was successful, and you're well on your way to the Venus refuelling station.
During the rush back on Earth, the fuel management system wasn't completely installed, so that's next on the priority list.

Opening the front panel reveals a jumble of wires. Specifically, two wires are connected to a central port and extend outward on a grid.
You trace the path each wire takes as it leaves the central port, one wire per line of text (your puzzle input).

The wires twist and turn, but the two wires occasionally cross paths. To fix the circuit, you need to find the intersection point closest to the central port.
Because the wires are on a grid, use the Manhattan distance for this measurement.
While the wires do technically cross right at the central port where they both start, this point does not count, nor does a wire count as crossing with itself.

For example, if the first wire's path is R8,U5,L5,D3, then starting from the central port (o), it goes right 8, up 5, left 5, and finally down 3:

...........
...........
...........
....+----+.
....|....|.
....|....|.
....|....|.
.........|.
.o-------+.
...........
Then, if the second wire's path is U7,R6,D4,L4, it goes up 7, right 6, down 4, and left 4:

...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
These wires cross at two locations (marked X), but the lower-left one is closer to the central port: its distance is 3 + 3 = 6.

Here are a few more examples:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = distance 159
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135
What is the Manhattan distance from the central port to the closest intersection?

Your puzzle answer was 293.

--- Part Two ---
It turns out that this circuit is very timing-sensitive; you actually need to minimize the signal delay.

To do this, calculate the number of steps each wire takes to reach each intersection; choose the intersection where the sum of both wires' steps is lowest.
If a wire visits a position on the grid multiple times, use the steps value from the first time it visits that position when calculating the total value of a specific intersection.

The number of steps a wire takes is the total number of grid squares the wire has entered to get to that location,
including the intersection being considered. Again consider the example from above:

...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
In the above example, the intersection closest to the central port is reached after 8+5+5+2 = 20 steps by the first wire,
and 7+6+4+3 = 20 steps by the second wire for a total of 20+20 = 40 steps.

However, the top-right intersection is better: the first wire takes only 8+5+2 = 15
and the second wire takes only 7+6+2 = 15, a total of 15+15 = 30 steps.

Here are the best steps for the extra examples from above:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = 610 steps
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = 410 steps
What is the fewest combined steps the wires must take to reach an intersection?

Your puzzle answer was 27306.

Both parts of this puzzle are complete! They provide two gold stars: **"""


my_file = open('data_day_3.txt')

a = my_file.read()
a = a.replace('\n', '|')

wire_1 = a[0:a.find('|')].split(',')
wire_2 = a[a.find('|') + 1:].split(',')


# wire_1 = 'R8,U5,L5,D3'.split(',')
# wire_2 = 'U7,R6,D4,L4'.split(',')

# wire_1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(',')
# wire_2 = 'U62,R66,U55,R34,D71,R55,D58,R83'.split(',')


# wire_1 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(',')
# wire_2 = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(',')


def generate_cords(w):
    w_cords = []
    begin = (0, 0)
    w_cords.append(begin)
    for path in w:
        r = int(path[1:])
        if path[0] == 'R':
            for x in range(1, r + 1):
                w_cords.append((begin[0] + x, begin[1]))
            begin = (r + begin[0], begin[1])

        elif path[0] == 'L':
            for x in range(1, r + 1):
                w_cords.append((begin[0] - x, begin[1]))
            begin = (begin[0] - r, begin[1])

        elif path[0] == 'U':
            for y in range(1, r + 1):
                w_cords.append((begin[0], begin[1] + y))
            begin = (begin[0], begin[1] + r)

        elif path[0] == 'D':
            for y in range(1, r + 1):
                w_cords.append((begin[0], begin[1] - y))
            begin = (begin[0], begin[1] - r)
    return w_cords


def find_min():

    # PART 1 #
    snake_1 = set(generate_cords(wire_1))
    snake_2 = set(generate_cords(wire_2))
    snake_12 = snake_1 & snake_2
    snake_12 = list(filter(lambda a: a > 0, map(lambda x: abs(abs(x[0]) + abs(x[1])), snake_12)))

    # PART 2 #
    snake_1_ = generate_cords(wire_1)
    snake_2_ = generate_cords(wire_2)

    s1_cpy = snake_1_.copy()
    s2_cpy = snake_2_.copy()

    snake_1_ = set(snake_1_)
    snake_2_ = set(snake_2_)

    snake_12_ = snake_1_ & snake_2_
    snake_12_ = list(filter(lambda x: x is not None, snake_12_))
    founded_len_1 = list(filter(lambda x: x > 0, map(lambda x: s1_cpy.index(x), snake_12_)))
    founded_len_2 = list(filter(lambda x: x > 0, map(lambda x: s2_cpy.index(x), snake_12_)))

    final_l_1 = [(s1_cpy[x], x) for x in founded_len_1]
    final_l_2 = [(s2_cpy[x], x) for x in founded_len_2]

    min_sum = min([final_l_1[x][1] + final_l_2[x][1] for x in range(len(final_l_1))])

    return min(snake_12), min_sum


print(find_min())
