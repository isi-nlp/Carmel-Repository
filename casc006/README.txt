
Poetry FSTs (by Marjan Ghazvininejad)

=======================================================================
16syllabus-rhyhm.fsa
=======================================================================

  Accepts iambic tetrameter rhyming couplets, e.g.:

	0 1 0 1 0 _ih1_l__iy0__er0* -trans- _ih1_l__iy0__er0*Rev 0Rev 1Rev 0Rev 1Rev 0Rev

=======================================================================
iamb-penta-couplet.fsa
=======================================================================

  Accepts iambic pentameter rhyming couplets.

=======================================================================
word2rhythm_and_rhyme.fst
=======================================================================

  Assigns stress and rhyme to words, e.g.:

	% echo '"special"' | carmel -sliOQEWk 5 word2rhythm_and_rhyme.fst

	1 0
	0Rev 1Rev

	% echo '"ultrasound"' | carmel -sliOQEWk 5 word2rhythm_and_rhyme.fst

	_aw1_n_d*Rev 0Rev 1Rev
	1 0 1
	1Rev 0Rev 1Rev
	1 0 _aw1_n_d*

	% echo '"correct"' | carmel -sliOQEWk 5 word2rhythm_and_rhyme.fst

	_eh1_k_t*Rev 0Rev
	0 1
	1Rev 0Rev
	0 _eh1_k_t*

  Notes:

    1) only includes most frequent 20k words

    2) avoids one-syllable words, whose stress depends on context
       - only includes 6 one-syllable words (the, a, an, ...)
       - NEW: Kevin added a few extra more

    3) assumes poetic meter is iambic (01)*
       - only includes words with alternating stress 
       - no "11" words (like "typhoon")
       - however, does include "...100" words (like "angela")
         - treated as "101" for meter purposes
         - however, rhyme is taken from the vowel of the "1" syllable

    4) concatenates results of words in sequence, e.g.:

	    % echo '"correct" "balloon"' | carmel -sliOQEWk 20 word2rhythm_and_rhyme.fst

	    _eh1_k_t*Rev 0Rev _uw1_n*Rev 0Rev
	    _eh1_k_t*Rev 0Rev 0 1
	    0 _eh1_k_t* _uw1_n*Rev 0Rev
	    _eh1_k_t*Rev 0Rev 0 _uw1_n*
	    0 _eh1_k_t* 0 1
	    1Rev 0Rev _uw1_n*Rev 0Rev
	    0 _eh1_k_t* 0 _uw1_n*
	    1Rev 0Rev 0 1
	    0 _eh1_k_t* 1Rev 0Rev
	    1Rev 0Rev 0 _uw1_n*
	    1Rev 0Rev 1Rev 0Rev
	    0 1 _uw1_n*Rev 0Rev
	    _eh1_k_t*Rev 0Rev 1Rev 0Rev
	    0 1 0 1
	    0 1 1Rev 0Rev
	    0 1 0 _uw1_n*

=======================================================================
sonnet.wfsa = word2rhythm_and_rhyme.fst  o  iamb-penta-couplet.fsa
=======================================================================

The sonnet.wfsa accepts all word sequences that legally form a sonnet.

There are 2.1 x 10^31 legal sonnets with this vocabulary.

% carmel -g 5 sonnet.wfsa

"monopoly" "preserves" "devine" "steroid" "-trans-" "paranoid" "helmet" "lounging" "shaping" "but"
"militiamen" "critique" "displayed" "sergei" "-trans-" "array" "centurion" "religiously"
"rescheduling" "receptors" "entourage" "-trans-" "mirage" "pilotless" "sahara" "invests"
"projecting" "magma" "axel" "massimo" "-trans-" "munro" "volleyball" "cyber" "turbo" "my"
"hypocrisy" "prospectus" "motivate" "-trans-" "circulate" "convent" "accommodating"

