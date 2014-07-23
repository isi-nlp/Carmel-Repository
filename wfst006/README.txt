
Converts English phoneme sequences into English letter sequences, by spelling out.
For use especially on OOV words, although in general it should reproduce the pronunciation of in-vocabulary words as well.

Usage:

% echo '"<s>" "F" "R" "EH" "N" "AH" "M" "IY" "</s>"' | carmel -sliOEk 10 wfst006 

"F" "R" "E" "N" "E" "M" "Y" 0.97798377752
"F" "R" "E" "N" "E" "M" "Y" 0.867601682766548
"F" "R" "E" "N" "O" "M" "Y" 0.866509449045589
"F" "R" "E" "N" "O" "M" "Y" 0.834645669291
"F" "R" "E" "N" "O" "M" "Y" 0.821726021819307
"F" "R" "E" "N" "O" "M" "Y" 0.768709127293979
"F" "R" "E" "N" "E" "M" "Y" 0.463304266829161
"F" "R" "E" "N" "E" "M" "Y" 0.411012504269972
"F" "R" "E" "N" "O" "M" "Y" 0.394630684744974
"F" "R" "E" "N" "O" "M" "Y" 0.379079969025243

Notes:

Start and end tags are recommended for best results, although they are not required. An FST that automatically adds start and end tags could be built quite easily.

This was built from aligned CMU pronunciation data (KN/N IGH/AY T/T). All possible pronunciation -> spelling ngrams are counted, including start and end tags. Then the ngrams are pruned: All ngrams that are not full words (with start and end tags) and with counts of 1 are pruned; ngrams that are not full words (with or without start and end tags) and with counts < 10 are also pruned. The counts are then divided.

This WFST is more liberally pruned in order to fit on GitHub. It achieves 35.4% exact matches on .1% held out data from the CMU Pronunciation Dictionary. A less pruned and larger WFST achieves 45.7% accuracy in the same experiment. For access to the larger machine, contact Aliya Deri at aderi@isi.edu or Kevin Knight at knight@isi.edu.
