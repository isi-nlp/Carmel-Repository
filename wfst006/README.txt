
Converts English phoneme sequences into English letter sequences, by spelling out.
For use especially on OOV words.

Usage:

% echo '"W" "EY" "L"' | carmel -sliOEk 10 wfst006

"W" "A" "L" "E" 0.95889
"W" "A" "Y" "L" 0.53116464993
"W" "A" "L" 0.441494040386877
"W" "A" "I" "L" 0.405129496821
"W" "A" "L" "E" 0.252255710217
"W" "E" "L" 0.186530450397272
"W" "A" "I" "L" 0.17375182689
"W" "A" "L" 0.087879871275
"W" "E" "L" "L" 0.0788877062127
"W" "A" "Y" "L" 0.0601691932650251

Notes:

I'm not sure how this was built.  I think maybe [Marcu & Wong 02] was run on
the CMU pronouncing dictionary, and phrase table put into Carmel format.
It's not very usable in the reverse direction.  

Needs improvement!!

