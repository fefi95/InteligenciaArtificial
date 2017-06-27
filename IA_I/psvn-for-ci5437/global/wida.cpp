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
#include <algorithm>

using namespace std;

unsigned long long int totalNodes;
unsigned long long int lqs;

int cost = -1;  /* Contains the cost to find the goal. */
int h0;  /* Contains the cost to find the goal. */
clock_t clockStart;
clock_t clockEnd;
time_t timeStart;
time_t timeEnd;
double timeElapsed;
float weight;

// Lets you convert an integer to string.
string convertInt(int number){
  ostringstream ss; // Create a stringstream.
  ss << number;     // Add number to the stream
  return ss.str();  // Return a string with the content of the stream.
}


pair<int,int> bounded_dfs_visit(state_t* state, int history, int g, int bound){

    int ruleid;
    state_t child;
    ruleid_iterator_t iter;

    pair<int,int>act_node;
    pair<int,int>result;

    int nextHistory;

    int f = g + weight*heuristic(state);

    timeEnd = time(NULL);
    timeElapsed = difftime(timeEnd, timeStart);
    // printf("%f\n", timeElapsed);
    if (timeElapsed > 300){
        assert("timeout");
    }

    if (f > bound) {
        act_node.first = -1;
        act_node.second = f;
        return act_node;
    }
    if (is_goal(state)){
        act_node.first = 0;
        act_node.second = g;
        return act_node;
    }

    int mint = 200000; /* infinity */
    init_fwd_iter(&iter, state);
    while ( (ruleid = next_ruleid(&iter)) >= 0 ){
        if (fwd_rule_valid_for_history(history, ruleid) != 0){

            nextHistory = next_fwd_history(history, ruleid);
            apply_fwd_rule(ruleid, state, &child);
            ++totalNodes;
            result = bounded_dfs_visit(&child, nextHistory, g+1, bound);
            if (result.first >=  0) {result.first = result.first + 1; return result;};
            mint = min(mint, result.second);

        }
    }

    act_node.first = -1;
    act_node.second = mint;
    return act_node;
}

// Lets you use the Iterative Deepening DFS.
pair<int,int> IDA_search(state_t* state)
{

  pair<int,int> result;
  int bound = weight*heuristic(state);
  h0 = bound;

  ++totalNodes;

  // Performs depth-bounded searches with increasing depth bounds.
  while (true){
      int history = init_history;
      result = bounded_dfs_visit(state, history, 0, bound);
      if (result.first >=  0) return result;
      bound = result.second;
  }

  return result;
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

    std::pair<int,int> result;

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
        totalNodes = 0;
        cost = 0;   /* On the beginning, the cost will be 0. */
        clockStart = clock();
        timeStart = time(NULL);
        /* Convert the string to an actual state. */
        ++totalNodes;
        read_state(state_line, &state);

        printf("Solving :");
        print_state(stdout, &state);
        printf("...\n");

        try {
            result = IDA_search(&state);
            cost   = result.first;
        }
        catch (std::exception& e) {
            fprintf(fileOut, "X, %s, %s, %.1f, %s, \"%s\", na, na, na, na\n", argv[3], argv[4], weight, argv[6], state_line);
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
