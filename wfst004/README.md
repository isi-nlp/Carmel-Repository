A wFST that convert IPA (English Pronunciation Sequence) to Pinyin-if (Pinyin initial/final sequence) using `phoneme-phrase based model`.

`ae k s eh p t` => `e k e s ai p u t e`
```
echo 'ae k s eh p t' | carmel -sliOEk 1 phrase_derivation.fst.wb

Input line 1: ae k s eh p t
	(26278 states / 48501 arcs reduce-> 219/433)
e k e s ai p u t e 0.666666666667
Derivations found for all 1 inputs
Viterbi (best path) product of probs=0.666666666667, probability=2^-0.584963 per-input-symbol-perplexity(N=6)=2^0.0974938 per-line-perplexity(N=1)=2^0.584963

```

#### Reference
Xing Shi, Kevin Knight and Heng Ji, *How to Speak a Foreign Kanguage Without Knowing It*, ACL 2014.
