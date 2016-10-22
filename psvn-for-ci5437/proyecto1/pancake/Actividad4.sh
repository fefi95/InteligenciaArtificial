#! /bin/bash

filename="../../instances/pancake28.txt"

make pancake28.WIDA
./pancake28.WIDA $filename "pancake28_IDA_Actividad4.csv" IDA manhattan 1.0 15puzzle
