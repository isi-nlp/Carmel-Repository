
Adds start (<s>) and end (</s>) symbols to sequences of pronounceable grapheme segments.

Usage:

% echo '"KN" "IGH" "T"' | carmel -sliOEk 5 wfst008 

"<s>" "KN" "IGH" "T" "</s>" 1

Notes:

Pronounceable grapheme segments are derived from aligned CMU pronounciation data (e.g., KN/N IGH/AY T/T gives the grapheme segments KN, IGH, and T.)