Pronounce English words, including OOV.

% echo '"D" "E" "R" "I"' | carmel -sliOEk 10 --exponents=1,1,.5,1,1 ../wfst007/wfst007 ../wfsa005/wfsa005 ../wfst008/wfst008 ../wfst009/wfst009 


"D" "EH" "R" "IY" 0.0016550460911633

"D" "EH" "R" "IY" 0.00162377027856493

"D" "EH" "R" "IY" 0.00107819593482002

"D" "EH" "R" "IY" 0.00105782100134729

"D" "R" "IY" 0.000876261615086749

"D" "ER" "IY" 0.000860836863087246

"D" "R" "IY" 0.000859702684065477

"D" "ER" "IY" 0.000846287136791743

"D" "ER" "IY" 0.000844569417394079

"D" "ER" "IY" 0.000830294640850974

Notes:

Input should be all uppercase letters.

wfst009 has been liberally pruned in order to fit on GitHub. Using this machine, casc004 achieves 54.3% exact matches on .1% held out data from the CMU Pronunciation Dictionary. A less pruned and larger WFST achieves 66.9% accuracy in the same experiment. For access to the larger machine, contact Aliya Deri at aderi@isi.edu or Kevin Knight at knight@isi.edu.

