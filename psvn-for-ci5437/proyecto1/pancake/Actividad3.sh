#! /bin/bash

filenameIn="../../instances/pancake16.txt"
filenameOut="pancake16_IDDFS_result.csv"

make pancake16.IDDFS2

./pancake16.IDDFS2 $filenameIn $filenameOut dfid pancake16 
