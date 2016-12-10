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
int numSegm; // Number of segments of the problem

/**
*    Function that represents a variable for the SATLIB format
*    for a segment
*    @param i: row position of the cell
*    @param j: column position of the cell
*    @param coord [n|s|e|w]: cardinal reference of the segment
*    return: a string that represents the number of variable of that segment
*/
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

/**
*   Function that represents a variable for the SATLIB format for interior
*   and exterior cells
*   @param i: row position of the cell
*   @param j: column position of the cell
*   return: a string that represents the number of variable of that restriction
*/
string z(int i, int j) {
    // The variables must not correspond to segments, hence they should
    // have another enumeration. Note that the number of segments are :
    // numVertical + numHorizontal so we use that as an offset for next variables

    int val = (i - 1) * M + j; // transforming de i,j position to a one dimensional array
    return std::to_string(numSegm + val);
}

/**
*   Function that represents a variable for the SATLIB format for the
*   reachability restrictions
*   @param i: row position of the cell
*   @param j: column position of the cell
*   @param c1_i: row position of the c1 cell
*   @param c1_j: column position of the c1 cell
*   return: a string that represents the number of variable of that restrictions
*/
string r(int i, int j, int c1_i, int c1_j ) {
    // The variables must not correspond to segments, hence they should
    // have another enumeration. Note that the number of segments are :
    // numVertical + numHorizontal and the number of variables for z(i,j)
    // are N * M so we use that as an offset for next variables

    // We use val_i and val_j as they were indexes of a (N*M)*(N*M) matrix.
    // val_i would be the row number (i) and val_j would be the column number (j)
    int val_i = (i - 1) * M + j; // transforming de i,j position to a one dimensional array
    int val_j = (c1_i - 1) * M + c1_j; // transforming de c1_i,c1_j position to a one dimensional array

    // transforming de val_i,val_j position to a one dimensional array
    int val = (val_i -1)* N * M + val_j;

    return std::to_string(numSegm + N * M + val);
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
    int numHorizontal = (N + 1) * M; // number of horizontal segments
    int numVertical = (M + 1) * N;   // number of vertical segments
    numSegm = numHorizontal + numVertical;
    // Number of segments + Number of z(i,j) + number of r(c,c')
    int numVar = numSegm + N * M + N * M * N * M;
    int numClauses = 0; // FIX!

    encode << "p cnf " << numVar << " " << numClauses << std::endl;
    // std::cout << N << M << std::endl;
    char cell;
    string clause; // all clauses represents a CNF problem.
    char n = 'n';
    char e = 'e';
    char s = 's';
    char w = 'w';

    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            clause = "";
            input >> cell;
            /******************************************************************
                Type 0 clauses (are implied because of the enumeration function
                q(i,j,[n,s,e,w]))
            ******************************************************************/

            /******************************************************************
                Type 1 clauses
                exactly n segment surrounds the cell for n = 0, 1, 2, 3, 4
            ******************************************************************/
            switch (cell) {
                case '0':
                        encode << "c TYPE 1 CLAUSES:" << std::endl;
                        encode << "c rules for 0:" << std::endl;

                        // all surrounding segments are false
                        clause += "-" + q(i,j,n) + " 0\n";
                        clause += "-" + q(i,j,e) + " 0\n";
                        clause += "-" + q(i,j,s) + " 0\n";
                        clause += "-" + q(i,j,w) + " 0\n";
                    break;
                case '1':
                        encode << "c TYPE 1 CLAUSES:" << std::endl;
                        encode << "c rules for 1:" << std::endl;

                        // a segment is true and the rest are false
                        clause += q(i,j,n) + " " + q(i,j,e) + " " + q(i,j,s) + " " + q(i,j,w) + " 0\n";
                        clause += "-" + q(i,j,n) + " -" + q(i,j,e) + " 0\n";
                        clause += "-" + q(i,j,n) + " -" + q(i,j,s) + " 0\n";
                        clause += "-" + q(i,j,n) + " -" + q(i,j,w) + " 0\n";
                        clause += "-" + q(i,j,e) + " -" + q(i,j,s) + " 0\n";
                        clause += "-" + q(i,j,e) + " -" + q(i,j,w) + " 0\n";
                        clause += "-" + q(i,j,s) + " -" + q(i,j,w) + " 0\n";
                    break;
                case '2':
                        encode << "c TYPE 1 CLAUSES:" << std::endl;
                        encode << "c rules for 2:" << std::endl;

                        // up and down segment are true and the rest are false
                        clause +=  "-" + q(i,j,n) + " -" + q(i,j,s) + " -"+ q(i,j,w) + " 0\n";
                        clause +=  "-" + q(i,j,n) + " -" + q(i,j,s) + " -"+ q(i,j,e) + " 0\n";
                        clause +=  q(i,j,e) + " " + q(i,j,w) + " " + q(i,j,s) + " 0\n";
                        clause +=  q(i,j,e) + " " + q(i,j,w) + " " + q(i,j,n) + " 0\n";

                        // up and left segment are true and the rest are false
                        clause +=  "-" + q(i,j,n) + " -" + q(i,j,w) + " -"+ q(i,j,e) + " 0\n";
                        clause +=  q(i,j,e) + " " + q(i,j,s) + " " + q(i,j,n) + " 0\n";

                        // up and right segment are true and the rest are false
                        clause +=  q(i,j,w) + " " + q(i,j,s) + " " + q(i,j,n) + " 0\n";

                        // down and left segment are true and the rest are false
                        clause +=  "-" + q(i,j,s) + " -" + q(i,j,w) + " -"+ q(i,j,e) + " 0\n";
                        clause +=  q(i,j,n) + " " + q(i,j,e) + " " + q(i,j,w) + " 0\n";


                    break;
                case '3':
                        encode << "c TYPE 1 CLAUSES:" << std::endl;
                        encode << "c rules for 3:" << std::endl;

                        clause +=  "-" + q(i,j,n) + " -" + q(i,j,s) + " -"+ q(i,j,w) + " -"+ q(i,j,e) +" 0\n";

                        // up, down and left segments are true and right is false
                        clause +=  q(i,j,e) + " " + q(i,j,n) + " 0\n";
                        clause +=  q(i,j,e) + " " + q(i,j,s) + " 0\n";
                        clause +=  q(i,j,e) + " " + q(i,j,w) + " 0\n";

                        // up, down and right segments are true and left is false
                        clause +=  q(i,j,w) + " " + q(i,j,n) + " 0\n";
                        clause +=  q(i,j,w) + " " + q(i,j,s) + " 0\n";

                        // up, left and right segments are true and down is false
                        clause +=  q(i,j,s) + " " + q(i,j,n) + " 0\n";
                    break;
                case '4':
                        encode << "c TYPE 1 CLAUSES:" << std::endl;
                        encode << "c rules for 4:" << std::endl;

                        // all surrounding segments are true
                        clause  =  q(i,j,n) + " 0\n";
                        clause +=  q(i,j,s) + " 0\n";
                        clause +=  q(i,j,w) + " 0\n";
                        clause +=  q(i,j,e) + " 0\n";
                    break;
            }
            encode << clause;
            clause = "";

            /******************************************************************
                Type 2 clauses
                Interior cells are within the perimeter of the solution and
                exterior cells are not
            ******************************************************************/
            encode << "c TYPE 2 CLAUSES:" << std::endl;
            // Upper border
            if (i == 1) {
                clause +=  q(i,j,n) + " -" + z(1,j) + " 0\n";
                clause += "-" + q(i,j,n) + " " + z(1,j) + " 0\n";
            }

            // Lower border
            else if (i == N) {
                clause +=  q(N,j,s) + " -" + z(N,j) + " 0\n";
                clause += "-" + q(N,j,s) + " " + z(N,j) + " 0\n";
            }

            // Left border
            else if (j == 1) {
                clause +=  q(i,1,w) + " -" + z(i,1) + " 0\n";
                clause += "-" + q(i,1,w) + " " + z(i,1) + " 0\n";
            }

            // Right border
            else if (j == N) {
                clause +=  q(i,M,e) + " -" + z(i,M) + " 0\n";
                clause += "-" + q(i,M,e) + " " + z(i,M) + " 0\n";
            }

            // Cells that are not in the border
            else {
                clause += "-" + z(i,j) + " -" + q(i,j,n) + " -" + q(i,j,e) + " -" + q(i,j,s) + " -" + q(i,j,w) + " 0\n";
                clause += "-" + z(i,j) + " -" + q(i,j,n) + " -" + q(i,j,e) + " -" + q(i,j,s) + " " +  z(i-1,j) + " 0\n";
                clause += "-" + z(i,j) + " -" + q(i,j,n) + " -" + q(i,j,e) + " " + z(i,j-1) + " -" + q(i,j,w) + " 0\n";
                clause += "-" + z(i,j) + " -" + q(i,j,n) + " -" + q(i,j,e) + " " + z(i,j-1) + " " + z(i-1,j) + " 0\n";
                clause += "-" + z(i,j) + " -" + q(i,j,n) + " " + z(i+1,j) + " -" + q(i,j,s) + " -" + q(i,j,w) + " 0\n";
                clause += "-" + z(i,j) + " -" + q(i,j,n) + " " + z(i+1,j) + " -" + q(i,j,s) + " " + z(i-1,j) + " 0\n";
                clause += "-" + z(i,j) + " -" + q(i,j,n) + " " + z(i+1,j) + " -" + z(i,j-1) + " -" + q(i,j,w) + " 0\n";
                clause += "-" + z(i,j) + " -" + q(i,j,n) + " " + z(i+1,j) + " -" + z(i,j-1) + " " + z(i-1,j) + " 0\n";
                clause += "-" + z(i,j) + " " + q(i,j,n) + " -" + q(i,j,e) + " -" + q(i,j,s) + " -" + q(i,j,w) + " 0\n";
                clause += "-" + z(i,j) + " " + q(i,j,n) + " -" + q(i,j,e) + " -" + q(i,j,s) + " " + z(i-1,j) + " 0\n";
                clause += "-" + z(i,j) + " " + q(i,j,n) + " -" + q(i,j,e) + " " + z(i,j-1) + " -" + q(i,j,w) + " 0\n";
                clause += "-" + z(i,j) + " " + q(i,j,n) + " -" + q(i,j,e) + " " + z(i,j-1) + " " + z(i-1,j) + " 0\n";
                clause += "-" + z(i,j) + " " + q(i,j,n) + " " + z(i+1,j) + " -" + q(i,j,s) + " -" + q(i,j,w) + " 0\n";
                clause += "-" + z(i,j) + " " + q(i,j,n) + " " + z(i+1,j) + " -" + q(i,j,s) + " " + z(i-1,j) + " 0\n";
                clause += "-" + z(i,j) + " " + q(i,j,n) + " " + z(i+1,j) + " " + z(i,j-1) + " -" + q(i,j,w) + " 0\n";
                clause += "-" + z(i,j) + " " + q(i,j,n) + " " + z(i+1,j) + " " + z(i,j-1) + " " + z(i-1,j) + " 0\n";
                clause += " " + z(i,j) + " " + q(i,j,n) + " -" + q(i,j,n) + " 0\n";
                clause += " " + z(i,j) + " " + q(i,j,e) + " -" + z(i+1,j) + " 0\n";
                clause += " " + z(i,j) + " " + q(i,j,s) + " -" + z(i,j-1) + " 0\n";
                clause += " " + z(i,j) + " " + q(i,j,w) + " -" + z(i-1,j) + " 0\n";
            }
            encode << clause;
            clause = "";

            /******************************************************************
                Type 3 clauses
                Reachability
            ******************************************************************/
            encode << "c TYPE 3 CLAUSES:" << std::endl;

            // Every cell is reachable from itself
            clause += r(i,j,i,j) + " 0\n";

            // i,j is reachable form c1_i,c1_j and another cell is adjacent to it,
            // say c'', and there is not segment between them then i,j is reachable
            // from c''
            for (int c1_i = 1; c1_i <= N; c1_i++) {
                for (int c1_j = 1; c1_j <= M; c1_j++) {
                    if (c1_i - 1 > 1) {
                        clause += "-" + r(i,j,c1_i,c1_j) + " " + q(c1_i,c1_j,n) + " " + r(i,j,c1_i-1,c1_j) + " 0\n";
                    }
                    if (c1_j + 1 < M) {
                        clause += "-" + r(i,j,c1_i,c1_j) + " " + q(c1_i,c1_j,e) + " " + r(i,j,c1_i,c1_j+1) + " 0\n";
                    }
                    if (c1_i + 1 < N ) {
                        clause += "-" + r(i,j,c1_i,c1_j) + " " + q(c1_i,c1_j,s) + " " + r(i,j,c1_i+1,c1_j) + " 0\n";
                    }
                    if (c1_j - 1 > 1) {
                        clause += "-" + r(i,j,c1_i,c1_j) + " " + q(c1_i,c1_j,w) + " " + r(i,j,c1_i,c1_j-1) + " 0\n";
                    }
                }
            }
            encode << clause;
            clause = "";

            /******************************************************************
                Type 4 clauses
                All interior cells are reachable from each other
            ******************************************************************/
            encode << "c TYPE 4 CLAUSES:" << std::endl;

            for (int c1_i = 1; c1_i <= N; c1_i++) {
                for (int c1_j = 1; c1_j <= M; c1_j++) {
                    clause += z(i,j) + " " + z(c1_i,c1_j) + " " + r(i,j,c1_i,c1_j) + " 0\n";
                }
            }

            encode << clause;
            clause = "";
            // std::cout << "cell(" << i << ", " << j << ") =" << cell << std::endl;
        }
    }

    /******************************************************************
        Type 5 clauses
        Each dot on the grid must have zero or exactly 2 adjacent segments
    ******************************************************************/
    encode << "c TYPE 5 CLAUSES:" << std::endl;

    // Case: upper-left corner
    clause += "-" + q(1,1,n) + " " + q(1,1,w) + " 0\n";
    clause += "-" + q(1,1,w) + " " + q(1,1,n) + " 0\n";

    // Case upper-right corner
    clause += "-" + q(1,M,n) + " " + q(1,M,e) + " 0\n";
    clause += "-" + q(1,M,e) + " " + q(1,M,n) + " 0\n";

    // Case lower-left corner
    clause += "-" + q(N,1,s) + " " + q(N,1,w) + " 0\n";
    clause += "-" + q(N,1,w) + " " + q(N,1,s) + " 0\n";

    // Case lower-right corner
    clause += "-" + q(N,M,s) + " " + q(N,M,e) + " 0\n";
    clause += "-" + q(N,M,e) + " " + q(N,M,s) + " 0\n";

    for (int i = 0; i <= N; i++) {
        for (int j = 0; j <= M; j++) {
            // Upper border without corner
            if (i == 0 && j != 0 && j != M) {
                clause += "-" + q(1,j,n) + " " + q(1,j+1,n) + " " + q(1,j,e) + " 0\n";
                clause += q(1,j,n) + " -" + q(1,j+1,n) + " " + q(1,j,e) + " 0\n";
                clause += q(1,j,n) + " " + q(1,j+1,n) + " -" + q(1,j,e) + " 0\n";
                clause += "-" + q(1,j,n) + " -" + q(1,j+1,n) + " -" + q(1,j,e) + " 0\n";
            }

            // Lower border without corner
            else if (i == N && j != 0 && j != M) {
                clause += "-" + q(N,j,s) + " " + q(N,j+1,s) + " " + q(N,j,e) + " 0\n";
                clause += q(N,j,s) + " -" + q(N,j+1,s) + " " + q(N,j,e) + " 0\n";
                clause += q(N,j,s) + " " + q(N,j+1,s) + " -" + q(N,j,e) + " 0\n";
                clause += "-" + q(N,j,s) + " -" + q(N,j+1,s) + " -" + q(N,j,e) + " 0\n";
            }

            // Left border without corner
            if (j == 0 && i != 0 && i != N ){
                clause += "-" + q(i,1,w) + " " + q(i+1,1,w) + " " + q(i,1,s) + " 0\n";
                clause += q(i,1,w) + " -" + q(i+1,1,w) + " " + q(i,1,s) + " 0\n";
                clause += q(i,1,w) + " " + q(i+1,1,w) + " -" + q(i,1,s) + " 0\n";
                clause += "-" + q(i,1,w) + " -" + q(i+1,1,w) + " -" + q(i,1,s) + " 0\n";
            }

            // Right border without corner
            else if (j == M  && i != 0 && i != N){
                clause += "-" + q(i,M,e) + " " + q(i+1,M,e) + " " + q(i,M,s) + " 0\n";
                clause += q(i,M,e) + " -" + q(i+1,M,e) + " " + q(i,M,s) + " 0\n";
                clause += q(i,M,e) + " " + q(i+1,M,e) + " -" + q(i,M,s) + " 0\n";
                clause += "-" + q(i,M,e) + " -" + q(i+1,M,e) + " -" + q(i,M,s) + " 0\n";
            }

            if (i > 0 && i < N && j > 0 && j < M) {
                // If a segment is adjacent to the dot on the grid (i,j) then exist
                // another segment that is adjacent as well
                clause += "-" + q(i,j,e) + " " + q(i,j,s) + " " + q(i+1,j+1,w) + " " + q(i+1,j+1,n) + " 0\n";
                clause += q(i,j,e) + " -" + q(i,j,s) + " " + q(i+1,j+1,w) + " " + q(i+1,j+1,n) + " 0\n";
                clause += q(i,j,e) + " " + q(i,j,s) + " -" + q(i+1,j+1,w) + " " + q(i+1,j+1,n) + " 0\n";
                clause += q(i,j,e) + " " + q(i,j,s) + " " + q(i+1,j+1,w) + " -" + q(i+1,j+1,n) + " 0\n";

                // If there are two segments that are adjacent to the dot on the grid (i,j)
                // then the other two are not
                clause += "-" + q(i,j,e) + " -" + q(i,j,s) + " -" + q(i+1,j+1,w) + " 0\n";
                clause += "-" + q(i,j,e) + " -" + q(i,j,s) + " -" + q(i+1,j+1,n) + " 0\n";
                clause += "-" + q(i,j,e) + " -" + q(i+1,j+1,w) + " -" + q(i,j,s)  + " 0\n";
                clause += "-" + q(i,j,e) + " -" + q(i+1,j+1,w) + " -" + q(i+1,j+1,n) + " 0\n";
                clause += "-" + q(i,j,e) + " -" + q(i+1,j+1,n) + " -" + q(i,j,s) + " 0\n";
                clause += "-" + q(i,j,e) + " -" + q(i+1,j+1,n) + " -" + q(i+1,j+1,w)  + " 0\n";
                clause += "-" + q(i,j,s) + " -" + q(i+1,j+1,w) + " -" + q(i,j,e) + " 0\n";
                clause += "-" + q(i,j,s) + " -" + q(i+1,j+1,w) + " -" + q(i+1,j+1,n) + " 0\n";
                clause += "-" + q(i,j,s) + " -" + q(i+1,j+1,n) + " -" + q(i,j,e) + " 0\n";
                clause += "-" + q(i,j,s) + " -" + q(i+1,j+1,n) + " -" + q(i+1,j+1,w) + " 0\n";
                clause += "-" + q(i+1,j+1,w) + " -" + q(i+1,j+1,n) + " -" + q(i,j,e) + " 0\n";
                clause += "-" + q(i+1,j+1,w) + " -" + q(i+1,j+1,n) + " -" + q(i,j,s) + " 0\n";
            }
            encode << clause;
            clause = "";
        }
    }

    encode << "\n";
    
    input.close();
    encode.close();
    return 0;
}
