#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pinyin import PINYIN_TABLE_MANDARIN_SRC as ptable
import codecs

# hanzi => tone + pinyin
def getFrequency():
    table = {}
    f = open('frequency.txt')
    for line in f:
        ll = line.split('\t')
        word = ll[1]
        word = word.decode('utf8')
        freq = int(ll[2])
        table[word] = freq

    return table


def getTable():
    table = {}
    freqTable = getFrequency()
    for (a,u) in ptable.iteritems():
        for s in u.split(' '):
            n = int(s,16)
            word = unichr(n)
            freq = 1
            if word in freqTable:
                freq = freqTable[word]
            if not word in table:
                table[word] = []
            table[word].append((a.lower(),freq))

    pTable = {}
    pToneTable = {}
    for word in table:
        for value,freq in table[word]:
            p = value[1:]
            pt = value
            if not p in pTable:
                pTable[p] = 0
            if not pt in pToneTable:
                pToneTable[pt] = 0
            pTable[p]+=freq
            pToneTable[pt] += freq

    return table,pTable,pToneTable

def generate_fst_without_tone(path):
    f = open(path,'w')
    t,pt,ptt = getTable()
    f.write('0\n')
    f.write('(0 (0 # #))\n')
    for key in t:
        for value,freq in t[key]:
            if ord('1') <= ord(value[0]) <= ord('5'):
                value = value[1:].lower()
            else:
                print value
                value = value.lower()
            prob = freq*1.0 / pt[value]
            s = '(0 (0 "{}" {} {}))\n'.format(value,key.encode('utf8'),prob)
            f.write(s)

def generate_fst_with_tone(path):
    f = open(path,'w')
    t,pt,ptt = getTable()
    f.write('0\n')
    f.write('(0 (0 # #))\n')
    for key in t:
        for value,freq in t[key]:
            value = value.lower()
            prob = freq*1.0/ptt[value]
            s = '(0 (0 "{}" {} {}))\n'.format(value,key.encode('utf8'),prob)
            f.write(s)

def main():
    fn1 = 'pinyin-q-to-chinese.fst.wb'
    fn2 = 'pinyin-tone-q-to-chinese.fst.wb'
    generate_fst_with_tone(fn2)
    generate_fst_without_tone(fn1)

if __name__ == '__main__':
    main()
