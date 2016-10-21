#! /bin/bash

# filename="../../instances/15Puzzle.txt"

make 15Puzzle.WIDA
./15Puzzle.WIDA $1 "pancake16_WIDA_result.csv" WIDA manhattan 1.5 15puzzle
