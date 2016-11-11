// Game of Othello -- Example of main
// Universidad Simon Bolivar, 2012.
// Author: Blai Bonet
// Last Revision: 1/11/16
// Modified by:

#include <iostream>
#include <limits>
#include "othello_cut.h" // won't work correctly until .h is fixed!
#include "utils.h"

#include <unordered_map>

using namespace std;

unsigned expanded = 0;
unsigned generated = 0;
int tt_threshold = 32; // threshold to save entries in TT
int INFINITY = std::numeric_limits<int>::max();

// Transposition table
struct stored_info_t {
    int value_;
    int type_;
    enum { EXACT, LOWER, UPPER };
    stored_info_t(int value = -100, int type = LOWER) : value_(value), type_(type) { }
};

struct hash_function_t {
    size_t operator()(const state_t &state) const {
        return state.hash();
    }
};

class hash_table_t : public unordered_map<state_t, stored_info_t, hash_function_t> {
};

hash_table_t TTable[2];

int maxmin(state_t state, int depth, bool use_tt);
int minmax(state_t state, int depth, bool use_tt = false);
int maxmin(state_t state, int depth, bool use_tt = false);
int negamax(state_t state, int depth, int color, bool use_tt = false);
int negamax(state_t state, int depth, int alpha, int beta, int color, bool use_tt = false);
int scout(state_t state, int depth, int color, bool use_tt = false);
int negascout(state_t state, int depth, int alpha, int beta, int color, bool use_tt = false);

int main(int argc, const char **argv) {
    state_t pv[128];
    int npv = 0;
    for( int i = 0; PV[i] != -1; ++i ) ++npv;

    int algorithm = 0;
    if( argc > 1 ) algorithm = atoi(argv[1]);
    bool use_tt = argc > 2;

    // Extract principal variation of the game
    state_t state;
    cout << "Extracting principal variation (PV) with " << npv << " plays ... " << flush;
    for( int i = 0; PV[i] != -1; ++i ) {
        bool player = i % 2 == 0; // black moves first!
        int pos = PV[i];
        pv[npv - i] = state;
        state = state.move(player, pos);
    }
    pv[0] = state;
    cout << "done!" << endl;

#if 0
    // print principal variation
    for( int i = 0; i <= npv; ++i )
        cout << pv[npv - i];
#endif

    // Print name of algorithm
    cout << "Algorithm: ";
    if( algorithm == 0 ) {
        cout << "Minmax-Maxmin";
    } else if( algorithm == 1 ) {
        cout << "Negamax (minmax version)";
    } else if( algorithm == 2 ) {
        cout << "Negamax (alpha-beta version)";
    } else if( algorithm == 3 ) {
        cout << "Scout";
    } else if( algorithm == 4 ) {
        cout << "Negascout";
    }
    cout << (use_tt ? " w/ transposition table" : "") << endl;

    // Run algorithm along PV (bacwards)
    cout << "Moving along PV:" << endl;
    for( int i = 0; i <= npv; ++i ) {
        //cout << pv[i];
        int value = 0;
        TTable[0].clear();
        TTable[1].clear();
        float start_time = Utils::read_time_in_seconds();
        expanded = 0;
        generated = 0;
        int color = i % 2 == 1 ? 1 : -1;

        try {
            if( algorithm == 0 ) {
                value = color * (color == 1 ? maxmin(pv[i], 0, use_tt) : minmax(pv[i], 0, use_tt));
            } else if( algorithm == 1 ) {
                value = negamax(pv[i], 0, color, use_tt);
            } else if( algorithm == 2 ) {
                value = negamax(pv[i], 0, -200, 200, color, use_tt);
            } else if( algorithm == 3 ) {
                value = color * scout(pv[i], 0, color, use_tt);
            } else if( algorithm == 4 ) {
                value = negascout(pv[i], 0, -200, 200, color, use_tt);
            }
        } catch( const bad_alloc &e ) {
            cout << "size TT[0]: size=" << TTable[0].size() << ", #buckets=" << TTable[0].bucket_count() << endl;
            cout << "size TT[1]: size=" << TTable[1].size() << ", #buckets=" << TTable[1].bucket_count() << endl;
            use_tt = false;
        }

        float elapsed_time = Utils::read_time_in_seconds() - start_time;

        cout << npv + 1 - i << ". " << (color == 1 ? "Black" : "White") << " moves: "
             << "value=" << color * value
             << ", #expanded=" << expanded
             << ", #generated=" << generated
             << ", seconds=" << elapsed_time
             << ", #generated/second=" << generated/elapsed_time
             << endl;
    }

    return 0;
}

/************************ MUTUALLY RECURSIVE MINIMAX ***************************/

/**
* maxmin
*
* @param state: the state to evaluate best strategy
* @param depth: depth of the recursion
* @param use_tt: indicates whether you are using the transposition table or not
*
*/
int minmax(state_t state, int depth, bool use_tt) {

    state_t child;
    bool player = false; // white = min

    if (/*depth == 0 ||*/ state.terminal()) {
        return state.value();
    }

    int score = INFINITY;
    bool pass = true;

    ++expanded;
    for (int pos = 0; pos < DIM; pos++) {
        // Generate child
        if (state.outflank(player, pos)) {
            child = state.move(player, pos);
            pass = false; // some child was generated hence player did not pass
            ++generated;
            score = min(score, maxmin(child, depth + 1, use_tt));
        }
    }

    // Passing the turn
    if (pass) {
        score = min(score, maxmin(state, depth + 1, use_tt));
    }

    return score;
}

/**
* minmax
*
* @param state: the state to evaluate best strategy
* @param depth: depth of the recursion
* @param use_tt: indicates whether you are using the transposition table or not
*
*/
int maxmin(state_t state, int depth, bool use_tt) {

    state_t child;
    bool player = true; // black = max

    if (/*depth == 0 ||*/ state.terminal() ) {
        return state.value();
    }

    int score = -INFINITY;
    bool pass = true;

    ++expanded;
    for (int pos = 0; pos < DIM; pos++) {
        // Generate child
        if (state.outflank(player, pos)) {
            child = state.move(player, pos);
            pass = false; // some child was generated hence player did not pass
            ++generated;
            score = max(score, minmax(child, depth + 1, use_tt));
        }
    }

    // Passing the turn
    if (pass) {
        score = max(score, minmax(state, depth + 1, use_tt));
    }

    return score;
}

/**
* Negamax without alpha-beta prunning
*
* @param state: the state to evaluate best strategy
* @param depth: depth of the recursion
* @param color: which player represents
* @param use_tt: indicates whether you are using the transposition table or not
*
*/
int negamax(state_t state, int depth, int color, bool use_tt) {

    state_t child;
    bool player = color > 0; // black = even numbers

    // std::cout << "holis" << std::endl;
    if (/*depth == 0 ||*/ state.terminal() ) {
        return color * state.value();
    }

    int alpha = -INFINITY;
    bool pass = true;

    ++expanded;
    for (int pos = 0; pos < DIM; pos++) {
        // Generate child
        if (state.outflank(player, pos)) {
            child = state.move(player, pos);
            pass = false; // some child was generated hence player did not pass
            ++generated;
            alpha = max(alpha, -negamax(child, depth + 1, -color, use_tt));
        }
    }

    // Passing the turn
    if (pass) {
        alpha = max(alpha, -negamax(state, depth + 1, -color, use_tt));
    }

    return alpha;
}

/**
* Negamax with alpha-beta prunning
*
* @param state: the state to evaluate best strategy
* @param depth: depth of the recursion
* @param alpha: represents the maximum value for Max nodes
* @param beta: represents the minimum value for Min nodes
* @param color: which player represents
* @param use_tt: indicates whether you are using the transposition table or not
*
*/
int negamax(state_t state, int depth, int alpha, int beta, int color, bool use_tt) {

    state_t child;
    bool player = color > 0; // black = even numbers

    if (/*depth == 0 ||*/ state.terminal() ) {
        return color * state.value();
    }

    int score = -INFINITY;
    int val;
    bool pass = true;
    ++expanded;

    for (int pos = 0; pos < DIM; pos++) {
        // Generate child
        if (state.outflank(player, pos)) {
            child = state.move(player, pos);
            pass = false; // some child was generated hence player did not pass
            ++generated;
            val = -negamax(child, depth + 1, -beta, -alpha, -color, use_tt);
            score = max(score, val);
            alpha = max(alpha, val);
            if (alpha >= beta) break; // alpha-beta cut-off
        }
    }

    // Passing the turn
    if (pass) {
        val = -negamax(state, depth + 1, -beta, -alpha, -color, use_tt);
        score = max(score, val);
    }

    return score;
}

vector<state_t> get_children(state_t state, bool player) {

    vector<state_t> children;
    state_t new_state;

    for( int pos = 0; pos < DIM; ++pos ) {
        if (state.outflank(player, pos)) {
            new_state = state.move(player, pos);
            children.push_back(new_state);
        }
    }

    return children;
}

/**
* TEST FUNCTION for Scout
*
* @param state: the state to evaluate the strategy
* @param depth: depth of the recursion
* @param color: which player represents
* @param condition: indicates the condition to use.
*
*/
bool TEST(state_t state, int depth, int score, int color, int condition){
    if (state.terminal()){

        // If the condition is 0 then we use >.
        if (condition == 0){
            return state.value() > score ? true : false;
        }
        // If the condition is 0 then we use >=.
        else if(condition == 1){
            return state.value() >= score ? true : false;
        }
    }

    // We get the clindren states of the actual state
    bool player = color == 1;
    vector<state_t> children = get_children(state, player);
    int nchildren = children.size(); // We get the number of children.
    state_t child;                   // The actual children.
    ++expanded;

    for (int i = 0; i < nchildren; ++i) {
        // We set who is the actual children.
        child = children[i];
        ++generated;

        // If the node is a Max node (aka the player's turn)...
        if (color == 1 && TEST(child, depth - 1, score, -color, condition)){
            return true;
        }

        // If the node is a Min node (aka the enemy's turn).
        if (color == -1 && !TEST(child, depth - 1, score, -color, condition)){
            return false;
        }
    }

    if (nchildren == 0) {
      // If the node is a Max node (aka the player's turn)...
      if (color == 1 && TEST(state, depth - 1, score, -color, condition)){
          return true;
      }

      // If the node is a Min node (aka the enemy's turn).
      if (color == -1 && !TEST(state, depth - 1, score, -color, condition)){
          return false;
      }

    }

    return color == 1 ? false : true;
}

/**
* Scout
*
* @param state: the state to evaluate best strategy
* @param depth: depth of the recursion
* @param color: which player represents
* @param use_tt: indicates whether you are using the transposition table or not
*
*/
int scout(state_t state, int depth, int color, bool use_tt) {

    if (state.terminal()){
        return state.value();
    }

    int  score = 0;
    ++expanded;

    // We get the clindren states of the actual state.
    bool player = color == 1;
    vector<state_t> children = get_children(state, player);
    int nchildren = children.size(); // We get the number of children.
    state_t child;                   // The actual children.

    for (int i = 0; i < nchildren; ++i) {
        // We set who is the actual children.
        child = children[i];
        ++generated;

        // If it is the first child...
        if (i == 0){
            score = scout(child, depth - 1, -color, false);
        }else{
            // If the node is a Max node (aka the player's turn)...
            if (color == 1 && TEST(child, depth - 1, score, -color, 0)){
                score = scout(child, depth - 1, -color, false);
            }

            // If the node is a Min node (aka the enemy's turn)...
            if (color == -1 && !TEST(child, depth - 1, score,-color, 1)){
                score = scout(child, depth - 1, -color, false);
            }
        }
    }

    // If I pass...
    if (nchildren == 0){
      score = scout(state, depth - 1, -color, false);
    }

    return score;
}

/**
* Negascout with alpha-beta prunning and scout
*
* @param state: the state to evaluate best strategy
* @param depth: depth of the recursion
* @param alpha: represents the maximum value for Max nodes
* @param beta: represents the minimum value for Min nodes
* @param color: which player represents
* @param use_tt: indicates whether you are using the transposition table or not
*
*/
int negascout(state_t state, int depth, int alpha, int beta, int color, bool use_tt) {

    state_t child;
    bool player = color > 0; // black = even numbers

    if (/*depth == 0 ||*/ state.terminal() ) {
        return color * state.value();
    }

    int score = -INFINITY;
    bool pass = true;
    bool firstChild = true;
    ++expanded;

    for (int pos = 0; pos < DIM; pos++) {
        // Generate child
        if (state.outflank(player, pos)) {
            child = state.move(player, pos);
            pass = false; // some child was generated hence player did not pass
            ++generated;
            if (firstChild) {
                firstChild = false;
                score = -negascout(child, depth + 1, -beta, -alpha, -color, use_tt);
            }
            else {
                score = -negascout(child, depth + 1, -alpha - 1, -alpha, -color, use_tt); // search with a null window
                if (alpha < score  &&  score < beta) {
                    score = -negascout(child, depth + 1, -beta, -score, -color, use_tt); // full search
                }
            }
            alpha = max(alpha, score);
            if (alpha >= beta) break; // alpha-beta cut-off
        }
    }

    // Passing the turn
    if (pass) {
        score = -negascout(state, depth + 1, -beta, -score, -color, use_tt);
        alpha = max(alpha, score);
    }

    return alpha;
}
