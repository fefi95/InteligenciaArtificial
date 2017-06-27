#! /bin/bash

filename="../../instances/15puzzle_korf.txt"

make 15Puzzle.WIDA
./15Puzzle.WIDA $filename "15puzzle_IDA_Actividad4.csv" IDA manhattan 1.0 15puzzle
