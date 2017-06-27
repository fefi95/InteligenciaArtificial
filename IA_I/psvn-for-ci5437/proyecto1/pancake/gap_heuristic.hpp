/*
    Universidad Simon Bolivar
    CI-5437
    Edward Fernandez 10-...
    Jirlfe ...
    Stefani Castellanos 11-11394

    This file contains the implementation for gap heuristic
*/

#include <vector>

/**
    Implementation of gap heuristic for N pancakes
    @param state: which heuristic's cost you want to compute
    @return cost: cost of the heuristic in state.
*/
int heuristic(state_t *state) {

    int cost = 0;
    int statei, statei1;

    //iterate through state's coordenates
    for (int i = 0; i < NUMVARS - 1; i++) {
        statei = state -> vars[i];
        statei1 = state -> vars[i + 1];
        if (abs(statei - statei1) > 1){
            // printf("incremented cost with %d and %d \n", statei, statei1 );
            cost++;
        }
    }

    statei = state -> vars[NUMVARS - 1]; // Last pancake
    if (abs(statei - NUMVARS) > 1){
        // printf("incremented cost with %d and %d \n", statei, statei1 );
        cost++;
    }

    return cost;
}
