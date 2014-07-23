Converts sequences of pronounceable English grapheme segments into phoneme sequences (e.g., "pronouncing" the sequence).
For use especially on OOV words, although in general the machine should reproduce the pronounciation of in vocabulary words.

Usage:

% echo '"<s>" "WH" "A" "LE" "B" "O" "N" "ES" "</s>"' | carmel -sliOEk 10 wfst009 

"W" "EY" "L" "B" "OW" "N" "Z" 1
"W" "EY" "L" "B" "OW" "N" "Z" 0.996560170949
"W" "EY" "L" "B" "OW" "N" "Z" 0.901595744681
"W" "EY" "L" "B" "OW" "N" "Z" 0.898494409446188
"W" "EY" "L" "B" "AH" "N" "Z" 0.657086520047345
"W" "EY" "L" "B" "AH" "N" "Z" 0.592426410361933
"W" "AE" "L" "B" "OW" "N" "Z" 0.40625
"W" "AE" "L" "B" "OW" "N" "Z" 0.40625
"W" "AE" "L" "B" "OW" "N" "Z" 0.404852569448031
"W" "EY" "L" "B" "OW" "N" "Z" 0.372881355932

Notes:

Start and end tags are recommended for best results, although they are not required. wfst008 can be prepended to add the tags to a sequence of pronounceable grapheme segments.

This was built from aligned CMU pronunciation data (KN/N IGH/AY T/T). All possible pronounceable grapheme segments (e.g. KN, IGH, and T) -> phoneme ngrams are counted, including start and end tags. Then the ngrams are pruned: All ngrams that are not full words (with start and end tags) and with counts of 1 are pruned; ngrams that are not full words (with or without start and end tags) and with counts < 10 are also pruned. The counts are then divided to produce edge weights.

This WFST is more liberally pruned in order to fit on GitHub. As part of casc004, this machine achieves 54.3% exact matches on .1% held out data from the CMU Pronunciation Dictionary. A less pruned and larger WFST achieves 66.9% accuracy in the same experiment. For access to the larger machine, contact Aliya Deri at aderi@isi.edu or Kevin Knight at knight@isi.edu.