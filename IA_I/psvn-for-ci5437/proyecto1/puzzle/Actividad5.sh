#! /bin/bash

filename="../../instances/15puzzle_korf.txt"

make 15Puzzle.WIDA
echo "running WIDA* with 1.5"
./15Puzzle.WIDA $filename "15puzzle_1.5_Actividad5.csv" WIDA manhattan 1.5 15puzzle
echo "running WIDA* with 2.0"
./15Puzzle.WIDA $filename "15puzzle_2.0_Actividad5.csv" WIDA manhattan 2.0 15puzzle
