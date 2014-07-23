
This is a smoothed trigram language model for English pronounceable grapheme segments (allowable letter groups that can map to a phoneme downstream). It accepts sequences of these segments.

When combined with a grapheme to segment FST (wfst007) it can rank the grouping of graphemes for pronouncing any word.

The machine is built from the grapheme segments seen in aligned CMU pronunciation data (e.g., KN/N IGH/AY T/T gives the grapheme segments KN, IGH, and T.) It uses the code from make-ngram-a from wfsa002.