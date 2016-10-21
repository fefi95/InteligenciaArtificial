#! /bin/bash

filename="../../instances/pancake28.txt"

make pancake28.A*
./pancake28.A* $filename "pancake16_A*_result.csv" gap
