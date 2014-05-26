A fst which converts English words to IPA (English pronunciation sequence )


```
$ echo '"hello" "word"' | carmel -sliEOk 1 eword-epron3.fst.wb

Input line 1: "hello" "word"
	(746848 states / 746847 arcs reduce-> 13/12)
hh ah l ow w er d 1
Derivations found for all 1 inputs
Viterbi (best path) product of probs=1, probability=2^0 per-input-symbol-perplexity(N=2)=2^-0 per-line-perplexity(N=1)=2^-0
```

Note: Word Boundary `#` is preserved.

```
echo '"hello" #  "word"' | carmel -sliEOk 1 eword-epron3.fst.wb 

Input line 1: "hello" #  "word"
	(995796 states / 995795 arcs reduce-> 14/13)
hh ah l ow # w er d 1
Derivations found for all 1 inputs
Viterbi (best path) product of probs=1, probability=2^0 per-input-symbol-perplexity(N=3)=2^-0 per-line-perplexity(N=1)=2^-0
```


