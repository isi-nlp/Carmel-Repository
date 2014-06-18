
Letter trigram models for dozens of languages.  Data is the UN Declaration
of Human Rights (UNDHR), files also included.  Note that accent marks have 
been removed from letters, as is the custom in cryptography, so most of the
symbols are 'a-z' and '_' (for space).  These LMs require '_' at the beginning 
and end of the string.

Usage:

% carmel -g 1 lm.2.tri.wfsa

"_" "w" "e" "_" "o" "t" "e" "n" "t" "e" "h" "i" "a" "n" "d" "_" "t" "o" "_" "s" "t" "a" "c" "t" "_" "t" "h" "e" "a" "s" "s" "i" "o" "n" "e" "_" "i" "n" "o" "n" "_" "r" "e" "e" "t" "_" "f" "r" "e" "m" "p" "l" "e" "_" "o" "f" "_" "p" "r" "e" "n" "t" "e" "a" "c" "t" "i" "o" "n" "_" "g" "r" "n" "_" "f" "r" "e" "r" "d" "s" "_" "f" "r" "o" "u" "t" "h" "e" "_" "r" "i" "g" "h" "t" "_" "t" "o" "_" "p" "r" "o" "u" "r" "_" "e" "n" "t" "s" "_" "n" "o" "_" "m" "e" "n" "a" "t" "i" "o" "n" "s" "_" "c" "r" "e" "e" "_" "p" "e" "_" "b" "e" "_" "i" "n" "d" "i" "e" "n" "a" "l" "_" "s" "h" "i" "s" "_" "p" "r" "e" "s" "s" "a" "m" "i" "t" "t" "e" "n" "c" "e" "_" "h" "e" "_" "h" "o" "u" "l" "s" "_" "f" "o" "r" "y" "o" "n" "s" "_" "a" "n" "d" "_" "e" "l" "a" "c" "e" "m" "p" "e" "_" "c" "o" "n" "e" "_" "w" "i" "t" "r" "a" "d" "e" "s" "t" "_" "t" "_"

% carmel -g 1 lm.26.tri.wfsa

"a" "r" "b" "e" "r" "_" "i" "r" "_" "a" "n" "g" "_" "u" "n" "m" "e" "n" "_" "e" "b" "e" "i" "n" "d" "_" "s" "t" "a" "a" "t" "_" "v" "o" "n" "_" "g" "e" "i" "t" "_" "d" "e" "r" "_" "g" "e" "n" "_" "d" "e" "r" "_" "b" "e" "h" "u" "t" "e" "_" "b" "e" "n" "_" "s" "e" "r" "e" "h" "u" "l" "t" "_" "d" "e" "r" "u" "n" "d" "_" "i" "_" "o" "d" "e" "n" "i" "e" "_" "d" "i" "g" "e" "n" "_" "h" "a" "_" "o" "d" "e" "r" "h" "n" "d" "_" "i" "n" "e" "r" "_" "m" "i" "l" "l" "e" "_" "e" "r" "_" "g" "r" "i" "e" "l" "b" "a" "r" "u" "n" "d" "_" "i" "h" "e" "n" "_" "l" "a" "r" "t" "g" "l" "e" "i" "t" "e" "t" "e" "r" "e" "u" "n" "g" "e" "m" "_" "f" "a" "n" "g" "_" "a" "l" "s" "c" "h" "_" "a" "n" "e" "d" "e" "r" "n" "_" "p" "o" "t" "i" "i" "n" "a" "b" "e" "n" "t" "e" "n" "o" "c" "h" "t" "_" "a" "u" "f" "_" "b" "e" "n" "_" "f" "r" "e" "i" "n" "e" "r" "_" "u" "n" "t" "z" "e" "i" "t" "_" "d" "i" "g" "e" "n" "_" "n" "a" "c" "h" "s" "_" "a" "u" "e" "n" "t" "s" "s" "t" "a" "a" "t" "i" "g" "e" "n" "_" "s" "i" "c" "h" "l" "i" "g" "e" "n" "_" "w" "e" "r" "_" "h" "a" "t" "i" "o" "n" "a" "t" "_" "n" "a" "l" "e" "n" "_" "a" "l" "l" "e" "c" "h" "t" "_" "a" "n" "_" "z" "u" "_" "h" "a" "b" "e" "n" "_" "d" "u" "r" "_" "v" "e" "r" "d" "e" "n" "_"

Languages, with their integer codes:

  2  english
  3  abkhazian
  4  afrikaans
  5  albanian
  6  arabic
  7  aymara
  8  basque
  9  breton
 10  bulgarian
 11  catalan
 12  chinese
 13  corsican
 14  croatian
 15  czech
 16  danish
 17  dutch
 18  esperanto
 19  estonian
 20  faroese
 21  fijian
 22  finnish
 23  french
 24  frisian
 25  galician
 26  german
 27  greek
 28  greenlandic
 29  guarani
 30  hausa
 31  hungarian
 32  icelandic
 33  indonesian
 34  interlingua
 35  irish
 36  italian
 37  japanese
 38  javanese
 39  kazakh
 40  kinyarwanda
 41  korean
 42  kurdish
 43  latin
 44  latvian
 45  lingala
 46  lithuanian
 47  macedonian
 48  malagasy
 49  malay
 50  maltese
 51  maori
 52  norwegian
 53  occitan
 54  oromiffa
 55  polish
 56  portuguese
 57  quechua
 58  rhaeto-romance
 59  romanian
 60  russian
 61  samoan
 62  scottishgaelic
 63  shona
 64  siswati
 65  slovak
 66  slovenian
 67  somali
 68  spanish
 69  sundanese
 70  swahili
 71  swedish
 72  tonga
 73  turkish
 74  ukrainian
 75  uzbek
 76  welsh
 77  wolof
 78  xhosa
 79  zhuang
