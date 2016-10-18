#include <stdio.h>
#include <iostream>
#include <string>
#include <sstream>
#include <stdlib.h>
#include <assert.h>
#include <fstream>

using namespace std;

// Let you convert an integer to string.
string convertInt(int number){
  ostringstream ss; // Create a stringstream.
  ss << number;     // Add number to the stream
  return ss.str();  // Return a string with the content of the stream.
}

// Let you obtain the total nodes on the actual label.
int64_t bounded_dfs_visit(state_t state, int deep, int bound, int history){
  int ruleid;
  state_t child;
  int64_t numNodoAct = 0;
  ruleid_iterator_t iter;

  if (deep == 0) return 0;
  else{

    init_bwd_iter(&iter, &state);

    while( (ruleid = next_ruleid(&iter)) >= 0 ){

      if (bwd_rule_valid_for_history(history, ruleid) != 0){
        apply_bwd_rule(ruleid, &state, &child);
        int nextHistory = next_bwd_history(history, ruleid);
        int64_t totalAux = bounded_dfs_visit(child, deep - 1, bound, nextHistory);
        numNodoAct += totalAux;
      }
    }
  }

  return numNodoAct + 1;
}

// Let you use the Iterative Deepening DFS.
void iterative_deepening_depth_first_search()
{
  state_t state;                // Actual state.
  int goal_num;                 // ID of the goal condition.
  int bound;                    // The deep bound.
  int64_t totalNodes = 0;       // Total nodes on the actual bound.
  int64_t oldTotalNodes = 0;    // Total nodes on the last bound.
  int64_t *array;               // Array to contain the totals node in every label.

  cout << "ENTER THE DEEP: ";
  cin >> bound;
  array = new int64_t[bound];

  // Perform depth-bounded searches with increasing depth bounds.
  for (int i = bound + 1; i >= 0; i--){
      int history = init_history;
      first_goal_state(&state, &goal_num);
      array[i-1] = bounded_dfs_visit(state, i, bound, history);
  }

  // Print the total nodes of every label.

  cout << "\n\nRESULT: \n";
  for (int i = 0; i < bound + 1; i++)
  {
    totalNodes = array[i];
    cout << "The total nodes in deep " + convertInt(i) + ": " +
            convertInt(totalNodes - oldTotalNodes) + "\n";
    oldTotalNodes = totalNodes;
  }
}

int main(int argc, char **argv){
  iterative_deepening_depth_first_search();
}
