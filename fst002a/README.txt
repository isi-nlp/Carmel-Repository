
Converts English word sequences into phoneme sequences, and vice-versa.  
Built from CMU pronouncing dictionary by Ketan Singh at USC.
Fixes problems in fst002 by removing parentheses on words.  Also,
this is a capitalized version.

Usage:

% echo '"DATA"' | carmel -sliOEQk 5 fst002a
Input line 1: "DATA"
(497899 states / 497899 arcs reduce-> 11/11)
D AE T AH 1
D EY T AH 1
0
0
0

% echo 'D EY T AH' | carmel -sriIEQk 5 fst002a
Input line 1: D EY T AH
(25 states / 32 arcs reduce-> 24/31)
DATA 1
DATE A 1
DAYE TO 1
DATE UHH 1
DAE TO 1

