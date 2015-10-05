

Poetry FSTs (by Marjan Ghazvininejad)

=======================================================================
16syllabus-rhyhm.fsa
=======================================================================

  Accepts iambic tetrameter rhyming couplets, e.g.:

	0 1 0 1 0 _ih1_l__iy0__er0* -trans- _ih1_l__iy0__er0*Rev 0Rev 1Rev 0Rev 1Rev 0Rev

=======================================================================
word2rhythm_and_rhyme.fst
=======================================================================

  Assigns stress and rhyme to words, e.g.:

	% echo '"special"' | carmel -sliOQEWk 5 word2rhythm_and_rhyme.fst
	Input line 1: "special"
	(8 states / 8 arcs reduce-> 7/7)
	1 0
	0Rev 1Rev

	% echo '"ultrasound"' | carmel -sliOQEWk 5 word2rhythm_and_rhyme.fst
	Input line 1: "ultrasound"
	(14 states / 16 arcs reduce-> 13/15)
	_aw1_n_d*Rev 0Rev 1Rev
	1 0 1
	1Rev 0Rev 1Rev
	1 0 _aw1_n_d*

	% echo '"correct"' | carmel -sliOQEWk 5 word2rhythm_and_rhyme.fst
	Input line 1: "correct"
	(11 states / 13 arcs reduce-> 10/12)
	_eh1_k_t*Rev 0Rev
	0 1
	1Rev 0Rev
	0 _eh1_k_t*

  Notes:

    1) avoids one-syllable words, whose stress depends on context
       - only includes 6 one-syllable words (the, a, an, ...)

    2) assumes poetic meter is iambic (01)*
       - only includes words with alternating stress (no 11 words like "typhoon")
       - only gives rhyme info for words with stressed final syllables (...1)

    3) concatenates results of words in sequence, e.g.:

    % echo '"correct" "balloon"' | carmel -sliOQEWk 20 word2rhythm_and_rhyme.fst
    Input line 1: "correct" "balloon"
            (21 states / 26 arcs reduce-> 20/25)
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

