Convert English to Chinglish using phoneme-phrase-based model.

```
echo '"i" "s" "i" # "is" # "awesome" ' | carmel -sliOEk 1 fst002/eword-epron3.fst.wb wfst004/phrase_derivation.fst.wb fst003/pinyin-if-pinyin-q.fst.wb wst003/pinyin-q-to-chinese.fst.wb ;
Input line 1: "i" "s" "i" # "is" # "awesome" 
	(1991594 states / 1991593 arcs reduce-> 27/26)
	(102191 states / 126370 arcs reduce-> 198/500)
	(259 states / 3669 arcs reduce-> 203/3031)
	(199 states / 25350 arcs)
爱 爱 赛 # 一 斯 # 奥 丧 0.00111492394569933
Derivations found for all 1 inputs
Viterbi (best path) product of probs=0.00111492394569933, probability=2^-9.80884 per-input-symbol-perplexity(N=7)=2^1.40126 per-line-perplexity(N=1)=2^9.80884
```

Note:

1. Input should be all lowercase
2. Input should not contain punctuation. ( `#`is treat as word boundary. )
3. Should split abbreviation into letters, e.g. "ISI" to "i" "s" "i" .
4. Numbers should be pronounced out, e.g "22" to "twenty" "two".

#### Reference
Xing Shi, Kevin Knight and Heng Ji, *How to Speak a Foreign Language Without Knowing It*, ACL 2014.

