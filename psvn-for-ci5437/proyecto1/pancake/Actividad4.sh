#! /bin/bash

filename="../../instances/pancake28.txt"

make pancake28.A*
echo "group, algorithm, heuristic, domain, instance, cost, h0, generated, time, gen_per_sec" > pancake28_A*_result.csv

while read -r line
do
    ./pancake28.A* gap "$line"
    printf "$line\n"
done < "$filename"
