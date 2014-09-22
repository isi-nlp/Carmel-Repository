Carmel-Repository
=================

This is a repository for all finite-state machines that are compatible with the Carmel toolkit (http://www.isi.edu/licensed-sw/carmel).

FSA | Description
------------- | -------------
none yet | none yet

WFSA | Description
------------- | -------------
wfsa001 | English letter 2-gram model, P(e)
wfsa002 | English phoneme 3-gram model, P(epron); plus generic n-gram WFSA builder
wfsa003 | Letter 3-gram models for dozens of languages, built from UNDHR data
wfsa004 | Letter 3-gram model for English, built from Penn Treebank plaintext
wfsa005 | Pronounceable grapheme segment 3-gram model for English, built from the aligned CMU Pronunciation Dictionary
wfsa006 | Accepts any word of alphabet [A-Z] except for the word "FILTER." Includes code for building any such filter.

FST | Description
------------- | -------------
fst001 | English-to-Cipher letter substitutor, fully connected
fst002 | English-to-Phonemes, built from CMU Pron Dict
fst002a | English-to-Phonemes, with fixes
fst003 | Pinyin-if-to-pinyin, bi-directional

WFST | Description
------------- | -------------
wfst001 | English-to-French word-to-word translator, P(f&#124;e)
wfst002 | French-to-English word-to-word translator, P(e&#124;f)
wfst003 | Pinyin-to-Chinese bi-directional P(p&#124;c) and P(c&#124;p)
wfst004 | Pinyin-if-to-Epron, Pinyin initial/final to IPA (English Pronounciation)
wfst005 | English-to-Syllable-Stress, includes original CMU pronunciation lexicon
wfst006 | English phonemes to grapheme (spell out), useful for OOV
wfst007 | English graphemes to pronounceable grapheme segment sequences
wfst008 | Adds start and end tags to English pronounceable grapheme segment sequences
wfst009 | English pronounceable grapheme segment sequences to phoneme (pronouncer), useful for OOV

Cascade | Description
------------- | -------------
casc001 | English-to-English word-to-word paraphraser, P(e&#124;e)
casc002 | English letter-substitution cipher solver
casc003 | English-to-Chinglish
casc004 | English word to pronounciation
casc005 | Symbol clustering using EM (any # of clusters, any n-gram order)
