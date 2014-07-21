
Converts English word sequence into syllable-stress pattern.  This device 
produces multiple outputs, since some words are ambiguous (is PRISONER three 
syllables or two?), and since one-syllable words can sometimes be stressed.

=======================================================================

Usage:

% echo '"BUILT" "IN" "PRISONS" "AND" "THE" "REST" "OF" "THE" "EPIC"' | carmel -sliOEQk 5 wfst005

S* S S* S S S S* S S S* S 0.204350973857227
S* S* S* S S S S* S S S* S 0.164490845420452
S* S S* S S S S* S* S S* S 0.0933710114193622
S* S* S* S S S S* S* S S* S 0.0751583235265821
S S S* S S S S* S S S* S 0.0737207105460428

% echo '"GREAT"' | carmel -sliOEQk 5 wfst005

S 0.599
S* 0.400

=======================================================================

Training:

Per [Greene et al 2010], was trained on sonnets, whose lines have known 
rhythm "(S S*)^5".  viterbi alignments after EM training looks like this:

"WHEN" "FROM" "THE" "VAULTED" "WONDER" "OF" "THE" "SKY"
| S | S* | S | S* S | S* S | S* | S | S* | | 0.0438515458168464

"THE" "CURTAIN" "OF" "THE" "LIGHT" "IS" "DRAWN" "ASIDE"
| S | S* S | S* | S | S* | S | S* | S S* | | 0.0807576906686061

"AND" "I" "BEHOLD" "THE" "STARS" "IN" "ALL" "THEIR" "WIDE"
| S | S* | S S* | S | S* | S | S* | S | S* | | 0.0334539153082396

"ASSURED" "THAT" "THOSE" "MORE" "DISTANT" "ORBS" "ARE" "SUNS"
| S S* | S | S* | S | S* S | S* | S | S* | | 0.0256008788185002

"ROUND" "WHICH" "INNUMERABLE" "WORLDS" "REVOLVE"
| S* | S | S S* S S* S | S* | S S* | | 0.024464957516724

=======================================================================

Bigger models

wfst005 only has a 20k vocabulary (word types used in English poetry 
that this model was trained on).  For example, it has:
	NEAR
	NEARED
	NEARER
	NEAREST
	NEARING
	NEARLY
	NEARS
but not NEARLY.  

1) Marjan created wfst005.full by supplementing wfst005 with the rest of 
the CMU pronunciation dictionary.

2) Marjan also created a deterministic wfst005.test{.cap} with a vocab that 
is the intersection between PTB with (CMU + poetry). 

  a) multi-syllable words => 
     stress taken from CMU (if multiple, all get p=1).

  b) one-syllable words => 
     stress taken from poetry (only majority class, with p=1), or
     if not in poetry, then stress taken from CMU.
