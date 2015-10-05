
This is a WFSA that accepts all words made up of the alphabet [A-Z], but rejects the word "FILTER".

Usage:

%echo ' "F" "I" "L" "T" "E" "R" ' | carmel -sli wfsa006 

Empty or invalid result of composition with transducer "wfsa006".
No derivations found for 1 of 1 inputs

%echo ' "N" "O" "T" "F" "I" "L" "T" "E" "R" ' | carmel -sli wfsa006 
Input line 1: "N" "O" "T" "F" "I" "L" "T" "E" "R" 
	(10 states / 9 arcs)

9
(0 (1 "N"))
(1 (2 "O"))
(2 (3 "T"))
(3 (4 "F"))
(4 (5 "I"))
(5 (6 "L"))
(6 (7 "T"))
(7 (8 "E"))
(8 (9 "R"))
(9)


Bonus:

make_a_filter.py will make a filter for any word, given some alphabet. The alphabet is a global variable set within the script (default is [A-Z]) The word is set at the command line. It is automatically capitalized, and no tests are run to make sure that it uses only the given alphabet.

Usage:
python make_a_filter.py filter

