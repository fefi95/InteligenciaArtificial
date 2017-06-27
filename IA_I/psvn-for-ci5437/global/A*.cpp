/*
    Universidad Simon Bolivar
    CI-5437
    Edward Fernandez 10-...
    Jirlfe ...
    Stefani Castellanos 11-11394

    This file contains the implementation for A* algorithm
*/
#include <vector>
#include <time.h>
#include "priority_queue.hpp"
#include "heuristic.hpp"

#define  MAX_LINE_LENGTH 999

PriorityQueue<state_t> open; // Priority Queue ordered by f-value: f (n) = g(n) + h(s)
state_map_t *map = new_state_map(); // contains the cost-to-goal for all states that have been generated
state_map_t *historyMap = new_state_map(); // contains the history of each node

// variables needed for information in output file
int g = 0; //cost of path to a state
int generated = 1;
int h0;
clock_t clockStart;
clock_t clockEnd;
time_t timeStart;
time_t timeEnd;
double timeElapsed;
int history = init_history;


int A_star_expand(state_t *state){

    // VARIABLES FOR ITERATING THROUGH state's SUCCESSORS
    state_t child;
    ruleid_iterator_t iter; // ruleid_terator_t is the type defined by the PSVN API successor/predecessor iterators.
    int ruleid; // an iterator returns a number identifying a rule

    init_fwd_iter(&iter, state);  // initialize the child iterator
    while( (ruleid = next_ruleid(&iter)) >= 0 ) {
        // 300 seconds limit (5 min)
        timeEnd = time(0);
        timeElapsed = difftime(timeEnd, timeStart);
        if (timeElapsed > 300){
            return -1;
        }

        if (fwd_rule_valid_for_history(history, ruleid) != 0){
            apply_fwd_rule(ruleid, state, &child);
            int child_history = next_fwd_history(history, ruleid);

            // child's cost using the heuristic
            const int child_g = g + get_fwd_rule_cost(ruleid);
            const int child_f = child_g + heuristic(&child);

            // print state
            // printf("State: ");
            // print_state(stdout, &child);
            // printf("cost: %d\n", child_f);

            // check if either this child has not been seen yet or if
            // there is a new cheaper way to get to this child.
            const int *old_child_g = state_map_get(map, &child);
            if( (old_child_g == NULL) || (*old_child_g > child_g) ) {
                // add to open with the new cost
                state_map_add(map, &child, child_g);
                state_map_add(historyMap, &child, child_history);
                open.Add(child_f, child_f, child);
            }
            generated++;
        }
    }
    return 0;
}

int A_star(state_t *state_init){

    // initial state's cost
    h0 = heuristic(state_init);
    open.Add(h0, h0, *state_init);
    state_map_add(map, state_init, g);
    state_map_add(historyMap, state_init, history);

    state_t state; // state_t is defined by the PSVN API. It is the type used for individual states.

    while (!open.Empty()){

        // remove top state from priority state
        state = open.Top();
        open.Pop();
        const int *state_g = state_map_get(map, &state);
        g = *state_g;
        const int *state_hist = state_map_get(historyMap, &state);
        history = *state_hist;

        if (is_goal(&state)) {
            // print the distance then the state
            printf("the cost of the path is: %d and h0 is: %d\n", g, h0);
            return g;
        }

        // print state
        // printf("State: ");
        // print_state(stdout, &state);
        // printf("path's cost: %d\n", g);

        // break;
        int timeout = A_star_expand(&state);
        if (timeout == -1){
            printf("Time limit exceeded. Aborted...\n");
            return -1;
        }
    }
    return -1;
}

int main(int argc, char **argv) {

    // Input file.
    char const* const fileNameIn = argv[1]; /* should check that argc > 1 */
    FILE* fileIn = fopen(fileNameIn, "r");

    // Output file
    char const* const fileNameOut = argv[2]; /* should check that argc > 1 */
    FILE* fileOut = fopen(fileNameOut, "w");
    if( fileOut == NULL ) {
        fprintf(stderr, "could not open %s for writing\n", fileNameOut);
        exit(-1);
    }

    // VARIABLES FOR INPUT
    ssize_t nchars;
    state_t state; // state_t is defined by the PSVN API. It is the type used for individual states.

    // READ A LINE OF INPUT FROM stdin
    // printf("Please enter a state followed by ENTER: ");
    if( argc < 4) {
        printf("USAGE:...\n");
        exit(-1);
    }

    /*******************************   file handling    ********************************/
    char problemName[30];
    char state_line[500];
    int k = 2;

    //getting the name form the entry
    while (argv[0][k] != '.') {
        // printf("%c\n", argv[0][k]);
        problemName[k - 2] = argv[0][k];
        k++;
    }
    problemName[k - 2] = '\0';

    char buffer[MAX_LINE_LENGTH] = "group, algorithm, heuristic, domain, instance, cost, h0, generated, time, gen_per_sec";
    fwrite (buffer , sizeof(char), sizeof(buffer), fileOut);

    /**********************************   A* search   **********************************/
    while (fgets(state_line, sizeof(state_line), fileIn))  {

        /* Convert the string to an actual state. */
        read_state(state_line, &state);

        printf("Solving :");
        print_state(stdout, &state);
        printf("...\n");

        clockStart = clock();
        timeStart = time(0);

        try {
            g = A_star(&state);
        }
        catch (std::exception& e) {
            // write to file
            memset(buffer, 0, MAX_LINE_LENGTH);
            sprintf(buffer, "X, A*, %s, %s, \" ", argv[3], problemName);
            fwrite (buffer , sizeof(char), sizeof(buffer), fileOut);
            print_state(fileOut, &state);
            memset(buffer, 0, MAX_LINE_LENGTH);

            if (g == -1){ //timeout
                strcpy(buffer, "na, na, na, na\n");
                fwrite (buffer , sizeof(char), sizeof(buffer), fileOut);
            }
            continue;
        }


        clockEnd = clock();

        // write to file
        memset(buffer, 0, MAX_LINE_LENGTH);
        sprintf(buffer, "X, A*, %s, %s, \" ", argv[3], problemName);
        fwrite (buffer , sizeof(char), sizeof(buffer), fileOut);
        print_state(fileOut, &state);
        memset(buffer, 0, MAX_LINE_LENGTH);

        if (g == -1){ //timeout
            strcpy(buffer, "na, na, na, na\n");
            fwrite (buffer , sizeof(char), sizeof(buffer), fileOut);
        }
        else {
            fwrite (buffer , sizeof(char), sizeof(buffer), fileOut);
            timeElapsed = double(clockEnd - clockStart) / CLOCKS_PER_SEC;
            memset(buffer, 0, MAX_LINE_LENGTH);
            sprintf(buffer, "\", %d, %d, %d, %.6f, %.5e\n",g, h0, generated, timeElapsed, generated/timeElapsed);
            fwrite (buffer , sizeof(char), sizeof(buffer), fileOut);
        }
    }
    fclose(fileIn);
    fclose(fileOut);
}
