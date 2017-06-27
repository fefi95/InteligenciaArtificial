/*
    Universidad Simon Bolivar
    CI-5437
    Edward Fernandez 10-...
    Jirlfe ...
    Stefani Castellanos 11-11394

    This file contains the implementation for manhattan distance heuristic
*/

#include <vector>

int heuristic(state_t *state) {

    int cost = 0;
    int statei;

    //15-puzzle (4x4)
    int n = 4;
    int m = 4;

    div_t coordStatei; // coordenate where I wish to move the tile
    div_t coordI;     // tile's coordenate
    int tileCost;


    for (int i = 0; i < NUMVARS; i++) {
        statei = state -> vars[i];
        if (statei != 0) {
            coordI = div (i, m);
            coordStatei = div (statei, m);
            tileCost = abs(coordI.quot - coordStatei.quot) + abs(coordI.rem - coordStatei.rem);
            cost += tileCost;
            // printf("the state var is %d and it's tileCost: %d\n", statei, tileCost);
        }

    }
    // printf("Manhattan cost: %d\n",cost);
    return cost;

}
