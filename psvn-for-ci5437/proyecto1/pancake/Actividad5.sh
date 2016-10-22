#! /bin/bash

filename="../../instances/pancake28.txt"

make pancake28.WIDA
echo "running WIDA* with 1.5"
./pancake28.WIDA $filename "pancake28_1.5_Actividad5.csv" WIDA gap 1.5 pancake28
echo "running WIDA* with 2.0"
./pancake28.WIDA $filename "pancake28_2_Actividad5.csv" WIDA gap 2.0 pancake28
