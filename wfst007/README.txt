
Converts English grapheme sequences into all possible sequences of pronounceable grapheme segments (allowable letter groups that can map to a phoneme downstream).

Usage:

% echo '"W" "H" "A" "L" "E" "B" "O" "N" "E" "S"' | carmel -sliOEk 10 wfst007 

"WH" "AL" "EB" "ON" "ES" 1
"WH" "AL" "EB" "ON" "E" "S" 1
"WH" "AL" "EB" "O" "N" "ES" 1
"WH" "AL" "E" "B" "ON" "ES" 1
"WH" "AL" "EB" "O" "N" "E" "S" 1
"WH" "AL" "E" "B" "ON" "E" "S" 1
"WH" "AL" "EB" "O" "NE" "S" 1
"WH" "AL" "E" "B" "O" "N" "ES" 1
"WH" "AL" "EB" "O" "NES" 1
"WH" "AL" "E" "B" "O" "N" "E" "S" 1

Notes:

The machine is built from the grapheme segments seen in aligned CMU pronunciation data (e.g., KN/N IGH/AY T/T gives the grapheme segments KN, IGH, and T.) As the example shows, all paths are given a probability of 1.

Combining this machine with a grapheme segment language model (wfsa005) gives ranked paths.

