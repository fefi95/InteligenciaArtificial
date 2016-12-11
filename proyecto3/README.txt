================================================================================
OVERVIEW:

minisat/        Contains minisat project
encode.cpp      Encoding the problem so it can be use by Minisat
decode.cpp      Decoding of the solution given by minisat
runproject.sh   Shell scrip that reads input file a gives a solution for all the
                problems in that file

================================================================================

You can execute this project entirely using the shell script runproject.sh but
first you have to execute the following commnads for it to work:

export MROOT=<minisat-dir>
chmod +x runproject.sh

and run it:
./runproject.sh

it writes into a file called output.txt
================================================================================
