#! /bin/bash

filename="../../instances/15puzzle_korf.txt"

make 15Puzzle.A*
echo "group, algorithm, heuristic, domain, instance, cost, h0, generated, time, gen_per_sec" > 15Puzzle_A*_result.txt

while read -r line
do
    ./15Puzzle.A* manhattan "$line"
    printf "$line\n"
done < "$filename"
