#include <stdio.h>
#include <iostream>
#include <string>
#include <sstream>
#include <stdlib.h>
#include <assert.h>
#include <fstream>
#include <ctime>

using namespace std;

// Let you convert an integer to string.
string convertInt(int number){
  ostringstream ss; // Create a stringstream.
  ss << number;     // Add number to the stream
  return ss.str();  // Return a string with the content of the stream.
}

// Let you obtain the total nodes on the actual label.
int bounded_dfs_visit(state_t* state, int deep, int bound, int history){

  int ruleid;
  state_t child;
  ruleid_iterator_t iter;

  if (deep > bound) return -1;
  if (is_goal(state)) return deep;

  init_bwd_iter(&iter, state);
  while( (ruleid = next_ruleid(&iter)) >= 0 ){
    if (bwd_rule_valid_for_history(history, ruleid) != 0){
      apply_bwd_rule(ruleid, state, &child);
      int nextHistory = next_bwd_history(history, ruleid);
      int costAux = bounded_dfs_visit(&child, deep + 1, bound, nextHistory);
      if (costAux != -1) return costAux;
    }
  }

  return -1;
}

// Let you use the Iterative Deepening DFS.
int iterative_deepening_depth_first_search(state_t* state)
{
  //int goal_num;                               // ID of the goal condition.
  unsigned long long int totalNodes = 0;       // Total nodes on the actual bound.
  unsigned long long int oldTotalNodes = 0;    // Total nodes on the last bound.
  int bound = 0;
  int cost = -1;

  time_t endwait;
  time_t start = time(NULL);
  time_t seconds = 600; // after 20s, end loop.
  endwait = start + seconds;

  // Perform depth-bounded searches with increasing depth bounds.
  while (start < endwait){
      int history = init_history;
      cost = bounded_dfs_visit(state, 0, bound, history);
      if (cost != -1) return cost;
      bound += 1;
      start = time(NULL);
      printf("loop time is : %s", ctime(&start));
  }

  return -1;
}

int main(int argc, char **argv){

  // Input file.
  char const* const fileName = argv[1]; /* should check that argc > 1 */
  FILE* fileIn = fopen(fileName, "r");
  char state_line[500];                 /* The state to use. */

  // Output file
  ofstream fileOut;
  fileOut.open(argv[2]);

  ssize_t nchars;     /* Char amount readed */
  state_t state;      /* Initial State. */

  int bound;          /* Limit deep. */
  char buffer[1000];  /* FOR TESTING. */
  int cost;

  /* Header for the out file. */
  fileOut << "grupo, algorithm, domain, instance, cost, generated, time, gen_per_sec\n";

  /* While exist states to read... */
  while (fgets(state_line, sizeof(state_line), fileIn))  {
      sprintf(buffer, "%s", state_line);
      cout << buffer;

      /* Convert the string to an actual state. */
      nchars = read_state(state_line, &state);
      bound = 0;

      // fileOut << "X, dfid, pancake16, \"";
      // fileOut << buffer;
      // fileOut << "\",";

      cost = iterative_deepening_depth_first_search(&state);
      cout << "cost: " + convertInt(cost) + "\n";
  }

  fclose(fileIn);
  fileOut.close();
}
