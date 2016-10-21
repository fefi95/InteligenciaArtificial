#! /bin/bash

# filename="../../instances/pancake28.txt"

make pancake28.WIDA
./pancake28.WIDA $1 "pancake16_WIDA_result.csv" IDA gap 1 pancake28
