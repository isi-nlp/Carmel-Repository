# reference: http://www.yellowbridge.com/chinese/pinyin-combo.php or valid-pinyin-table.html

finals = 'a o e ai ei ao ou an ang en eng er u ua uo uai ui uan uang un eng ong i ia ie iao iu ian iang in ing v ve van vn iong'
initials = 'b p m f d t n l g k h j q x zh ch sh r z c s w y'

finals = finals.split()
initials = initials.split()

initials = ['',] + initials
m = {}
m['a'] = '0-11 15-17 19-23'
m['o'] = '0-4 22-22'
m['e'] = '0-0 3-3 5-11 15-21 23-23'
m['ai'] = '0-3 5-11 15-17 19-22'
m['ei'] = '0-11 15-15 17-17 19-19 22-22'
m['ao'] = '0-3 5-11 15-21 23-23'
m['ou'] = '0-0 3-11 15-21 23-23'
m['an'] = '0-11 15-23'
m['ang'] = '0-11 15-23'
m['en'] = '0-5 7-7 9-11 15-22'
m['eng'] = '0-11 15-22'
m['er'] = '0-0'
m['u'] = '1-11 15-23'
m['ue'] = '23-23'
m['ua'] = '9-11 15-18'
m['uo'] = '5-11 15-21'
m['uai'] = '9-11 15-17'
m['ui'] = '5-6 9-11 15-21'
m['uan'] = '5-11 15-21 23-23'
m['uang'] = '9-11 15-17'
m['un'] = '5-11 15-21 23-23'
m['ong'] = '5-11 15-16 18-21 23-23'
m['i'] = '1-3 5-8 12-21 23-23'
m['ia'] = '5-5 8-8 12-14'
m['ie'] = '1-3 5-8 12-14'
m['iao'] = '1-3 5-8 12-14'
m['iu'] = '3-3 5-5 7-8 12-14'
m['ian'] = '1-3 5-8 12-14'
m['iang'] = '7-8 12-14'
m['in'] = '1-3 7-8 12-14 23-23'
m['ing'] = '1-3 5-8 12-14 23-23'
m['v'] = '7-8 12-14 23-23'
m['ve'] = '7-8 12-14 23-23'
m['van'] = '12-14 23-23'
m['vn'] = '12-14 23-23'
m['iong'] = '12-14'

f = open('pinyin-if-pinyin-q.fst.wb','w')

f.write('0\n')

def parse(s):
    ll = s.split()
    r = []
    for lll in ll:
        start = int(lll.split('-')[0])
        end = int(lll.split('-')[1])+1
        r += range(start,end)
    return r

for key in m:
    final = key
    s = m[key]
    r = parse(s)
    for i in r:
        initial = initials[i]
        ss = ''
        if initial == '':
            ss = '(0 (0 {} "{}"))\n'.format(final,final)
        else:
            ss = '(0 ({} {} *e*))\n'.format(initial,initial)
            ss += '({} (0 {} "{}"))\n'.format(initial,final, initial+final)
        f.write(ss)

f.close()
