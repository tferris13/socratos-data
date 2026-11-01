import csv, sys, unicodedata, collections, json
csv.field_size_limit(10**9)
D=sys.argv[1]; OUT=sys.argv[2]
def strip(s):
    s=unicodedata.normalize('NFD',s.lower())
    return ''.join(c for c in s if not unicodedata.combining(c)).replace('ς','σ').rstrip('0123456789')
forms={}
for r in csv.DictReader(open(f'{D}/forms.tsv'),delimiter='\t',quoting=csv.QUOTE_NONE):
    if r['lemmas']: forms[r['form']]=r['lemmas'].split('|')
gl={}
for r in csv.DictReader(open(f'{D}/lemmas.tsv'),delimiter='\t',quoting=csv.QUOTE_NONE):
    gl[r['lemma']]=r['short_meaning']
works={}
for r in csv.DictReader(open(f'{D}/works.tsv'),delimiter='\t',quoting=csv.QUOTE_NONE):
    works[r['work']]=r['author']+' '+r['title']
flags=[]; stats=collections.Counter(); per=collections.Counter()
PREP_CASE={'εἰς':'a','ἐς':'a','ἐν':'d','ἐνί':'d','ἐκ':'g','ἐξ':'g','ἀπό':'g','ἀπ’':'g','πρό':'g','σύν':'d','ξύν':'d'}
prev=None; total=0
for r in csv.DictReader(open(f'{D}/words.tsv'),delimiter='\t',quoting=csv.QUOTE_NONE):
    total+=1
    w=r['word']; lem=(r['lemmas'] or '').split('|')[0]; p=r['parse'] or ''
    key=(r['work'],r['ref'])
    if prev and prev[0]!=key: prev=None
    c=forms.get(w)
    if lem and c and lem not in c:
        pos=p[:1]
        same=any(strip(x)==strip(lem) for x in c)
        kind='R1-lookalike' if same else ('R1-small-word' if pos in 'rcdgl' and pos else 'R1-other')
        flags.append((kind,r['work'],r['ref'],r['n'],w,lem,gl.get(lem,''),'|'.join(c),p))
    if prev and len(p)==9 and len(prev[2])==9:
        pw,pl,pp=prev[1],prev[3],prev[2]
        if pp[0]=='r' and p[7]=='v' and c and len(c)>1:
            flags.append(('R3-vocative-after-prep',r['work'],r['ref'],r['n'],w,lem,gl.get(lem,''),'|'.join(c),p))
        if pp[0]=='l' and p[0] in 'na' and p[7]!='-' and pp[7]!='-' and (p[7]!=pp[7] or p[2]!=pp[2]) and c and len(c)>1:
            flags.append(('R6-article-mismatch',r['work'],r['ref'],r['n'],w,lem,gl.get(lem,''),'|'.join(c),p+' after '+pw+' '+pp))
    prev=(key,w,p,lem)
for f in flags: stats[f[0]]+=1; per[(f[0],f[1])]+=1
with open(OUT,'w') as o:
    o.write('rule\twork\tref\tn\tword\tlinked_lemma\tlinked_meaning\tanalyzer_lemmas\tparse\n')
    for f in flags: o.write('\t'.join(map(str,f))+'\n')
print('tokens',total); print(stats)
for k,v in per.most_common(25): print(k,works.get(k[1],''),v)
