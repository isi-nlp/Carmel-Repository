
Huge French-English word-for-word t-table, implemented as WFST, with
probabilities P(e|f).

% echo '"MAISON"' | carmel -sliOEk 5 huge-french-word.wfst
Input line 1: "MAISON"
        (2 states / 4 arcs)
"HOME" 0.539183
"HOUSE" 0.363243
"HOMES" 0.0806829
"DWELLING" 0.0168912
0
Derivations found for all 1 inputs
Viterbi (best path) product of probs=0.539183, probability=2^-0.891153 per-input-symbol-perplexity(N=1)=2^0.891153 per-line-perplexity(N=1)=2^0.891153
