A wFST that convert Pinyin and Chinese characters back and forth.

`pinyin-q-to-chinese.fst.wb`
`q` means pinyin symbol should be surrounded with quota `"`
`wb` means word boundary `#` is preserved during conversion

`pinyin-tone-q-to-chinese.fst.wb`
`tone` means pinyin is prepended tone marker, e.g. '2kui' and '5de'

#### pinyin => Chinese character
Without tone:
```
$echo '"de"' | carmel -sliOEk 5 pinyin-q-to-chinese.fst.wb 

Input line 1: "de"
	(2 states / 17 arcs)
的 0.908318432939
得 0.0723070030097
德 0.0193659654653
锝 7.10816471314e-06
㤫 1.14647817954e-07
Derivations found for all 1 inputs
Viterbi (best path) product of probs=0.908318432939, probability=2^-0.13873 per-input-symbol-perplexity(N=1)=2^0.13873 per-line-perplexity(N=1)=2^0.13873
```
With tone:
```
$echo '"2de"' | carmel -sliOEk 5 pinyin-tone-q-to-chinese.fst.wb

Input line 1: "2de"
	(2 states / 16 arcs)
得 0.788675470188
德 0.211230742297
锝 7.7531012405e-05
嘚 1.25050020008e-06
㤫 1.25050020008e-06
Derivations found for all 1 inputs
Viterbi (best path) product of probs=0.788675470188, probability=2^-0.342496 per-input-symbol-perplexity(N=1)=2^0.342496 per-line-perplexity(N=1)=2^0.342496

```
#### Chinese character => pinyin
Without tone:
```
$echo '得' | carmel -sriIEk 2 pinyin-q-to-chinese.fst.wb 

Input line 1: 得
	(2 states / 1 arcs)
"de" 0.0723070030097
0
Derivations found for all 1 inputs
Viterbi (best path) product of probs=0.0723070030097, probability=2^-3.78972 per-input-symbol-perplexity(N=1)=2^3.78972 per-line-perplexity(N=1)=2^3.78972
```

With tone:
```
$echo '得' | carmel -sriIEk 2 pinyin-tone-q-to-chinese.fst.wb 
Input line 1: 得
	(2 states / 1 arcs)
"2de" 0.788675470188
0
Derivations found for all 1 inputs
Viterbi (best path) product of probs=0.788675470188, probability=2^-0.342496 per-input-symbol-perplexity(N=1)=2^0.342496 per-line-perplexity(N=1)=2^0.342496
```

#### Word Boundary

```
$ echo '得 # 到' | carmel -sriIEk 2 pinyin-tone-q-to-chinese.fst.wb 
Input line 1: 得 # 到
	(4 states / 3 arcs)
"2de" # "4dao" 0.501719488017995
0
Derivations found for all 1 inputs
Viterbi (best path) product of probs=0.501719488017995, probability=2^-0.995047 per-input-symbol-perplexity(N=3)=2^0.331682 per-line-perplexity(N=1)=2^0.995047
```

```
echo '得 到' | carmel -sriIEk 2 pinyin-tone-q-to-chinese.fst.wb 
Input line 1: 得 到
	(3 states / 2 arcs)
"2de" "4dao" 0.501719488017995
0
Derivations found for all 1 inputs
Viterbi (best path) product of probs=0.501719488017995, probability=2^-0.995047 per-input-symbol-perplexity(N=2)=2^0.497524 per-line-perplexity(N=1)=2^0.995047

```

#### Reference
pinyin.py `Copyright (c) 2004 onward  Yusuke Shinyama <yusuke at cs dot nyu dot edu>`
frequency.txt [Combined character frequency list of Classical and Modern Chinese][1]


  [1]: http://lingua.mtsu.edu/chinese-computing/statistics/char/list.php?Which=TO