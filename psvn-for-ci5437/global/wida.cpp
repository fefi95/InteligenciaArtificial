/*
    Universidad Simon Bolivar
    CI-5437
    Edward Fernandez 10-11121
    Jirlfe ...
    Stefani Castellanos 11-11394

    This file contains the implementation for WIDA*
*/

#include <stdio.h>
#include <iostream>
#include <string>
#include <sstream>
#include <stdlib.h>
#include <assert.h>
#include <fstream>
#include <ctime>
#include "heuristic.hpp"

using namespace std;

clock_t clockStart;
clock_t clockEnd;
time_t timeStart;
time_t timeEnd;
double timeElapsed;
float weight;
int64_t totalNodes;

// Let you convert an integer to string.
string convertInt(int number){
  ostringstream ss; // Create a stringstream.
  ss << number;     // Add number to the stream
  return ss.str();  // Return a string with the content of the stream.
}

// Let you obtain the total nodes on the actual label.
std::pair<int,int> f_bounded_dfs_visit(state_t state, int bound, int history, int g){

    int ruleid;
    state_t child;
    ruleid_iterator_t iter;
    int64_t numNodoAct = 0;
    std::pair<int,int> n;

    int f = g + weight*heuristic(&state);

    timeEnd = time(NULL);
    timeElapsed = difftime(timeEnd, timeStart);
    // printf("%f\n", timeElapsed);
    if (timeElapsed > 300){
        assert("timeout");
    }

    if (f > bound) {
        n.first = -1;
        n.second = f;
        return n;
    }
    if (is_goal(&state)){
        n.first = 0;
        n.second = g;
        return n;
    }

    int t = 2000000; //infinity
    init_fwd_iter(&iter, &state);
    while( (ruleid = next_ruleid(&iter)) >= 0 ){
        if (fwd_rule_valid_for_history(history, ruleid) != 0){
            apply_fwd_rule(ruleid, &state, &child);
            int nextHistory = next_fwd_history(history, ruleid);
            totalNodes++;
            std::pair<int,int> p = f_bounded_dfs_visit(child, bound, nextHistory, g+1);
            if (p.first != -1) return p;
            t = min(t, p.second);
        }
    }
    n.first = -1;
    n.second = t;
    return n;
}


int main(int argc, char **argv){

    // Input file.
    char const* const fileNameIn = argv[1]; /* should check that argc > 1 */
    FILE* fileIn = fopen(fileNameIn, "r");

    // Output file
    char const* const fileNameOut = argv[2]; /* should check that argc > 1 */
    FILE* fileOut = fopen(fileNameOut, "w");
    char state_line[500];                 /* The state to use. */
    state_t state;                        /* Initial State. */
    char buffer[1000];
    float goalTime;

    int cost = 0;  /* Contain the cost to find the goal. */
    int h0;  /* Contain the cost to find the goal. */

    weight = atof(argv[5]);

    if (argc != 7)
    {
    cout << "WRONG FORMAT!\n\n";
    cout << "THE RIGHT FORMAT IS: .\\<.IDDFS> <input file.txt> <output file.txt> <algorithm> <heuristic> <weight> <domain>\n";
    exit(1);
    }

    /* Header for the out file. */
    fprintf(fileOut, "grupo, algorithm, heuristic, weight, domain, instance, cost, h0, generated, time, gen_per_sec\n");

    /* While exist states to read... */
    while (fgets(state_line, sizeof(state_line), fileIn))  {

        clockStart = clock();
        timeStart = time(NULL);
        /* Convert the string to an actual state. */
        read_state(state_line, &state);

        printf("Solving :");
        print_state(stdout, &state);
        printf("...\n");

        try {
            int bound = weight*heuristic(&state);
            h0 = bound;
            totalNodes = 0;
            // Perform depth-bounded searches with increasing depth bounds.
            while (true){
                int history = init_history;
                std::pair<int,int> p = f_bounded_dfs_visit(state, bound, history, 0);
                if (p.first != -1) {
                    cost = p.second;
                    break; //costo
                }
                bound += p.second;
            }
        }
        catch (std::exception& e) {
            fprintf(fileOut, "X, %s, %s, %.1f, %s, \"%s\", na, na, na, na\n", argv[3], argv[4], weight, argv[6], state_line);
            continue;
        }

        /* Time when find the goal. */
        clockEnd = clock();
        goalTime = (float)(clockEnd - clockStart)/CLOCKS_PER_SEC;

        strtok(state_line, "\n");
        if (cost != -1)
        fprintf(fileOut, "X, %s, %s, %.1f, %s \"%s\", %d, %d, %d, %.5f, %.5e\n", argv[3], argv[4], weight, argv[6], state_line, cost, h0, totalNodes, goalTime, (float)totalNodes/goalTime);
        else
        fprintf(fileOut, "X, %s, %s, %.1f, %s, \"%s\", na, na, na, na\n", argv[3], argv[4], weight, argv[6], state_line);
    }
    fclose(fileIn);
    fclose(fileOut);
}
