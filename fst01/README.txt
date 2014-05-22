
Fully-connected FST converts plaintext letters (a-z) to ciphertext 
letters (A-Z).  It also converts space (_) to space (_).

% echo '"a" "_" "a"' | carmel -sliOk 5 fst01
Input line 1: "a" "_" "a"
        (4 states / 53 arcs)
"A" "_" "A" 1
"A" "_" "B" 1
"B" "_" "A" 1
"A" "_" "C" 1
"B" "_" "B" 1
Derivations found for all 1 inputs
Viterbi (best path) product of probs=1, probability=2^0 per-input-symbol-perplexity(N=3)=2^-0 per-line-perplexity(N=1)=2^-0

