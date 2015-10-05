
English phoneme trigram model.

Trigrams counts taken from 95% of the CMU dictionary (file: pron).  Note: this 
is done over word types, not weighted by frequency!  

Usage:

% carmel -g 3 wfsa002

"EY" "L" "B" "IH" "F" "AY" "OW" "S" "T" "T" "AY" "F" "AO" "T"
"EY" "L" "B" "IH" "F" "AY" "OW" "S" "T" "T" "AY" "F" "AO" "T"
"EY" "EH" "Z" "AE" "K" "AA" "AO" "V" "L" "OW" "DH" "S"
"EY" "EH" "Z" "AE" "K" "AA" "AO" "V" "L" "OW" "DH" "S"
"G" "B" "IH" "JH" "EH" "TH" "AH" "B" "OY" "IH" "L" "CH"
"G" "B" "IH" "JH" "EH" "TH" "AH" "B" "OY" "IH" "L" "CH"

Bonus: 

This directory contains a program (make-ngram-a) to create smoothed bigram and
trigram models for any data set.  Training data should be in a file "xyz"
(as in "pron"), and smoothing data in "xyz.smooth" (as in "pron.smooth").  
Output files of interest are "xyz.bi.wfsa" and "xyz.tri.wfsa" (these have 
*e* input), and "xyz.bi.wfst" and "xyz.tri.wfst" (which are identity machines).

Usage:

% make-ngram-a pron

