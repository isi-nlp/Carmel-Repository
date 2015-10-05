A FST that can convert pinyin-if sequence into pinyin sequence back and forth. e.g. "w o sh i sh ui" <=> "wo shi shui".

[Pinyin][1] : An official phonetic system for transcribing Mandarin Chinese pronunciations of Chinese Characters. One pinyin symbol per Chinese Character. e.g. "我":"wo"

[Pinyin-if sequence][2] One pinyin symbol usually consists two parts: initials and finals. Pinyin-reg sequence is a sequence of such initials and finals. e.g. "wo shi shui":"w o sh i sh ui" 

pinyin-if => pinyin
```
echo 'w o # sh i # sh ui'|carmel -sliEOk 1 pinyin-if-pinyin-q.fst.wb 

Input line 1: w o # sh i # sh ui
	(9 states / 52 arcs)
"wo" # "shi" # "shui" 1
Derivations found for all 1 inputs
Viterbi (best path) product of probs=1, probability=2^0 per-input-symbol-perplexity(N=8)=2^-0 per-line-perplexity(N=1)=2^-0
```
pinyin => pinyin-if
```
echo '"wo" # "shi" # "shui"'|carmel -sriEIk 1 pinyin-if-pinyin-q.fst.wb 

Input line 1: "wo" # "shi" # "shui"
	(144 states / 2411 arcs reduce-> 9/52)
w o # sh i # sh ui 1
Derivations found for all 1 inputs
Viterbi (best path) product of probs=1, probability=2^0 per-input-symbol-perplexity(N=5)=2^-0 per-line-perplexity(N=1)=2^-0
```

Note: The FST is built by `build.py`




  [1]: http://en.wikipedia.org/wiki/Pinyin
  [2]: http://en.wikipedia.org/wiki/Pinyin#Initials_and_finals