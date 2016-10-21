/*
    Universidad Simon Bolivar
    CI-5437
    Edward Fernandez 10-11121
    Jirlfe ...
    Stefani Castellanos 11-11394

    This file contains the implementation for Iterative Deepening DFS algorithm
    for the activity 3.
*/

#include <stdio.h>
#include <iostream>
#include <string>
#include <sstream>
#include <stdlib.h>
#include <assert.h>
#include <fstream>
#include <ctime>

using namespace std;

int cost = -1;  /* Contain the cost to find the goal. */
time_t start;
time_t aux_time;
time_t endwait;

// Let you convert an integer to string.
string convertInt(int number){
  ostringstream ss; // Create a stringstream.
  ss << number;     // Add number to the stream
  return ss.str();  // Return a string with the content of the stream.
}

// Let you obtain the total nodes on the actual label.
int64_t bounded_dfs_visit(state_t* state, int deep, int bound, int history){
  int ruleid;
  state_t child;
  ruleid_iterator_t iter;
  int64_t numNodoAct = 0;

  cost = -1;

  if (start < endwait){
    if (deep > bound) return numNodoAct + 1;
    if (is_goal(state)){
      cost = deep;
      return numNodoAct + 1;
    }

    init_bwd_iter(&iter, state);
    while( (ruleid = next_ruleid(&iter)) >= 0 ){
      if (bwd_rule_valid_for_history(history, ruleid) != 0){
        apply_bwd_rule(ruleid, state, &child);
        int nextHistory = next_bwd_history(history, ruleid);
        int64_t totalAux = bounded_dfs_visit(&child, deep + 1, bound, nextHistory);
        numNodoAct += totalAux;
        start = time(NULL);

        if (cost != -1) return numNodoAct + 1;
      }
    }

    return numNodoAct + 1;
  }
  else{
    cost = -1;
    return -1;
  }
}

// Let you use the Iterative Deepening DFS.
int64_t iterative_deepening_depth_first_search(state_t* state)
{
  int bound = 0;

  start = time(NULL);
  aux_time = start;

  time_t seconds = 300; // after 10min, end loop.
  endwait = start + seconds;

  int64_t totalNodes = 0;

  // Perform depth-bounded searches with increasing depth bounds.
  while (true){
      int history = init_history;
      totalNodes += bounded_dfs_visit(state, 0, bound, history);
      if (cost != -1) return totalNodes;

      bound += 1;
  }

  return totalNodes;
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

  if (argc != 5)
  {
    cout << "WRONG FORMAT!\n\n";
    cout << "THE RIGHT FORMAT IS: .\\<.IDDFS> <input file.txt> <output file.txt> <algorithm> <domain> \n";
    exit(1);
  }

  /* Header for the out file. */
  fprintf(fileOut, "grupo, algorithm, domain, instance, cost, generated, time, gen_per_sec\n");

  /* While exist states to read... */
  while (fgets(state_line, sizeof(state_line), fileIn))  {
      cost = 0;   /* On the beginning, the cost will be 0. */

      /* Convert the string to an actual state. */
      read_state(state_line, &state);

      int64_t totalNodes = iterative_deepening_depth_first_search(&state);

      /* Time when find the goal. */
      goalTime = (float)(endwait - aux_time)/CLOCKS_PER_SEC;

      strtok(state_line, "\n");
      if (cost != -1)
        fprintf(fileOut, "X, %s, %s, \"%s\", %d, %d, %.5e, %.5e\n", argv[3], argv[4], state_line, cost, totalNodes, goalTime, (float)totalNodes/goalTime);
      else
        fprintf(fileOut, "X, %s, %s, \"%s\", na, na, na, na\n", argv[3], argv[4], state_line);

  }

  fclose(fileIn);
  fclose(fileOut);
}
