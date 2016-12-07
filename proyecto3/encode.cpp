/*
    Universidad Simon Bolivar
    CI-5437
    Edward Fernandez 10-11121
    Stefani Castellanos 11-11394

    This file contains the encoding for the SAT problem especified
    It outputs a file in SATLIB format to be use with minisat
*/

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int N, M; // dimensions (row, columns) of the problem

string q(int i, int j, char coord) {

    int val = (i - 1) * M + j; // transforming de i,j position to a one dimensional array
    switch (coord) {
        case 'n': return std::to_string(val);
                break;
        case 's': return std::to_string(i * M + j);
                break;
        case 'e': return std::to_string(val + i + N * (M + 1));
                break;
        case 'w': return std::to_string(val + i + N * (M + 1) - 1);
                break;
    }
    return "";
}

int main(int argc, const char **argv) {
    if( argc < 2 ) {
        std::cout << "input file missing!" << std::endl;
        return 1;
    }
    ifstream input; // input file
    ofstream encode; // output encode SAT file

    input.open(argv[1]);
    encode.open("encode.cnf");
    input >> N;
    input >> M;

    //WARNING: NUMBER OF VARIABLES AND CLAUSES WITHOUT CONSIDERING THAT IS A COMPLETE CYCLE. FIX
    int numVar = (N + 1) * N * 2;
    int numClauses = 0;

    encode << "p cnf " << numVar << " " << numClauses << std::endl;
    // std::cout << N << M << std::endl;
    char cell;
    string clause; // all clauses represents a CNF problem.

    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            clause = "";
            input >> cell;
            // Type 0 clauses (are implied because of the enumeration function q(i,j,[n,s,e,w]))

            // Type 1 clauses
            switch (cell) {
                case '0':
                        encode << "c rules for 0:" << std::endl;
                        // all surrounding segments are false
                        clause += "-" + q(i,j,'n') + " 0\n";
                        clause += "-" + q(i,j,'e') + " 0\n";
                        clause += "-" + q(i,j,'s') + " 0\n";
                        clause += "-" + q(i,j,'w') + " 0\n";
                    break;
                case '1':
                        encode << "c rules for 1:" << std::endl;
                        // a segment is true and the rest are false
                        clause += q(i,j,'n') + " " + q(i,j,'e') + " " + q(i,j,'s') + " " + q(i,j,'w') + " 0\n";
                        clause += "-" + q(i,j,'n') + " -" + q(i,j,'e') + " 0\n";
                        clause += "-" + q(i,j,'n') + " -" + q(i,j,'s') + " 0\n";
                        clause += "-" + q(i,j,'n') + " -" + q(i,j,'w') + " 0\n";
                        clause += "-" + q(i,j,'e') + " -" + q(i,j,'s') + " 0\n";
                        clause += "-" + q(i,j,'e') + " -" + q(i,j,'w') + " 0\n";
                        clause += "-" + q(i,j,'s') + " -" + q(i,j,'w') + " 0\n";
                    break;
                case '2':
                        encode << "c rules for 2:" << std::endl;

                        // up and down segment are true and the rest are false
                        clause +=  "-" + q(i,j,'n') + " -" + q(i,j,'s') + " -"+ q(i,j,'w') + " 0\n";
                        clause +=  "-" + q(i,j,'n') + " -" + q(i,j,'s') + " -"+ q(i,j,'e') + " 0\n";
                        clause +=  q(i,j,'e') + " " + q(i,j,'w') + " " + q(i,j,'s') + " 0\n";
                        clause +=  q(i,j,'e') + " " + q(i,j,'w') + " " + q(i,j,'n') + " 0\n";

                        // up and left segment are true and the rest are false
                        // clause +=  "-" + q(i,j,'n') + " -" + q(i,j,'w') + " -"+ q(i,j,'s') + " 0\n";
                        clause +=  "-" + q(i,j,'n') + " -" + q(i,j,'w') + " -"+ q(i,j,'e') + " 0\n";
                        // clause +=  q(i,j,'e') + " " + q(i,j,'s') + " " + q(i,j,'w') + " 0\n";
                        clause +=  q(i,j,'e') + " " + q(i,j,'s') + " " + q(i,j,'n') + " 0\n";

                        // up and right segment are true and the rest are false
                        // clause +=  "-" + q(i,j,'n') + " -" + q(i,j,'e') + " -"+ q(i,j,'s') + " 0\n";
                        // clause +=  "-" + q(i,j,'n') + " -" + q(i,j,'e') + " -"+ q(i,j,'w') + " 0\n";
                        // clause +=  q(i,j,'w') + " " + q(i,j,'s') + " " + q(i,j,'e') + " 0\n";
                        clause +=  q(i,j,'w') + " " + q(i,j,'s') + " " + q(i,j,'n') + " 0\n";

                        // down and left segment are true and the rest are false
                        // clause +=  "-" + q(i,j,'s') + " -" + q(i,j,'w') + " -"+ q(i,j,'n') + " 0\n";
                        clause +=  "-" + q(i,j,'s') + " -" + q(i,j,'w') + " -"+ q(i,j,'e') + " 0\n";
                        // clause +=  q(i,j,'n') + " " + q(i,j,'e') + " " + q(i,j,'s') + " 0\n";
                        clause +=  q(i,j,'n') + " " + q(i,j,'e') + " " + q(i,j,'w') + " 0\n";

                        // down and right segment are true and the rest are false
                        // clause +=  "-" + q(i,j,'s') + " -" + q(i,j,'e') + " -"+ q(i,j,'n') + " 0\n";
                        // clause +=  "-" + q(i,j,'s') + " -" + q(i,j,'e') + " -"+ q(i,j,'w') + " 0\n";
                        // clause +=  q(i,j,'n') + " " + q(i,j,'w') + " " + q(i,j,'s') + " 0\n";
                        // clause +=  q(i,j,'n') + " " + q(i,j,'w') + " " + q(i,j,'e') + " 0\n";

                        // left and right segment are true and the rest are false
                        // clause +=  "-" + q(i,j,'w') + " -" + q(i,j,'e') + " -"+ q(i,j,'n') + " 0\n";
                        // clause +=  "-" + q(i,j,'w') + " -" + q(i,j,'e') + " -"+ q(i,j,'s') + " 0\n";
                        // clause +=  q(i,j,'n') + " " + q(i,j,'s') + " " + q(i,j,'w') + " 0\n";
                        // clause +=  q(i,j,'n') + " " + q(i,j,'s') + " " + q(i,j,'e') + " 0\n";
                    break;
                case '3':
                        encode << "c rules for 3:" << std::endl;
                        clause +=  "-" + q(i,j,'n') + " -" + q(i,j,'s') + " -"+ q(i,j,'w') + " -"+ q(i,j,'e') +" 0\n";

                        // up, down and left segments are true and right is false
                        clause +=  q(i,j,'e') + " " + q(i,j,'n') + " 0\n";
                        clause +=  q(i,j,'e') + " " + q(i,j,'s') + " 0\n";
                        clause +=  q(i,j,'e') + " " + q(i,j,'w') + " 0\n";

                        // up, down and right segments are true and left is false
                        clause +=  q(i,j,'w') + " " + q(i,j,'n') + " 0\n";
                        clause +=  q(i,j,'w') + " " + q(i,j,'s') + " 0\n";
                        // clause +=  q(i,j,'w') + " " + q(i,j,'e') + " 0\n";

                        // up, left and right segments are true and down is false
                        clause +=  q(i,j,'s') + " " + q(i,j,'n') + " 0\n";
                        // clause +=  q(i,j,'s') + " " + q(i,j,'w') + " 0\n";
                        // clause +=  q(i,j,'s') + " " + q(i,j,'e') + " 0\n";

                        // down, left and right segments are true and up is false
                        // clause +=  up + " " + q(i,j,'s') + " 0\n";
                        // clause +=  q(i,j,'n') + " " + q(i,j,'w') + " 0\n";
                        // clause +=  q(i,j,'n') + " " + q(i,j,'e') + " 0\n";
                    break;
                case '4':
                        // all surrounding segments are true
                        clause  =  q(i,j,'n') + " 0\n";
                        clause +=  q(i,j,'s') + " 0\n";
                        clause +=  q(i,j,'w') + " 0\n";
                        clause +=  q(i,j,'e') + " 0\n";

                    break;
            }
            encode << clause;
            // std::cout << "cell:" << cell << std::endl;
        }
    }


    input.close();
    encode.close();
    return 0;
}
