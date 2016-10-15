/*
    Universidad Simon Bolivar
    CI-5437
    Edward Fernandez 10-...
    Jirlfe ...
    Stefani Castellanos 11-11394

    This file contains the implementation for manhattan distance heuristic
*/

#include <vector>

int manhattan_heuristic(state_t *state) {

    int cost = 0;
    int statei;
    div_t divresult;
    divresult = div (i - statei,n);

    //iterate through state's coordenates
    for (int i = 0; i < NUMVARS - 1; i++) {
        statei = state -> vars[i];
        cost += divresult.quot + divresult.rem;
    }
    return cost;
}
