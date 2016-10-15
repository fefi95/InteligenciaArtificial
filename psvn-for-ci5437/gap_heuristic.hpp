/*
    Universidad Simon Bolivar
    CI-5437
    Edward Fernandez 10-...
    Jirlfe ...
    Stefani Castellanos 11-11394

    This file contains the implementation for gap's heuristic
*/

#include <vector>

int gap_heuristic(state_t *state) {

    int cost = 0;
    //iterate through state's coordenates
    for (int i = 0; i < NUMVARS - 1; i++) {
        printf("%s\n", state.vars[i]);
        statei = atoi(state.vars[i]);
        statei1 = atoi(state.vars[i + 1]);
        if (abs(statei - statei1) > 1){
            cost++;
        }
    }
    return cost;
}
