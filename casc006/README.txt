

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

    3) assumes poetic meter is iambic (01)*
       - only includes words with alternating stress (no 11 words like "typhoon")
       - only gives rhyme info for words with stressed final syllables (...1)

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
word2rhythm_and_rhyme.fst  +  16syllabus-rhyhm.fsa
=======================================================================

Here, we test whether "afghanistan afghanistan afghanistan and pakistan" is a legal
iambic tetrameter couplet.  Note that we must reverse the second line, and insert "-trans-"
between the two lines:

% echo '"afghanistan" "afghanistan" "-trans-" "pakistan" "and" "afghanistan"' | carmel -sliOEQWk 5 word2rhythm_and_rhyme.fst 16syllabus-rhyhm.fsa

0 1 0 1 0 1 0 _ae1_n* -trans- _ae1_n*Rev 0Rev 1Rev 0Rev 1Rev 0Rev 1Rev 0Rev


