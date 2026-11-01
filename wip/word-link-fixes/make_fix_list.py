import csv, sys, unicodedata, collections, re
csv.field_size_limit(10**9)
D=sys.argv[1]; OUT=sys.argv[2]
def strip(s):
    s=unicodedata.normalize('NFD',s.lower()); return ''.join(c for c in s if not unicodedata.combining(c)).replace('ς','σ')
forms={}
for r in csv.DictReader(open(f'{D}/forms.tsv'),delimiter='\t',quoting=csv.QUOTE_NONE):
    if r['lemmas']: forms[r['form']]=r['lemmas'].split('|')
L=list(csv.DictReader(open(f'{D}/lemmas.tsv'),delimiter='\t',quoting=csv.QUOTE_NONE))
gl={r['lemma']:r['short_meaning'] for r in L}; cnt={r['lemma']:int(r['count'] or 0) for r in L}
# E: malformed duplicate lemmas -> the common spelling with the same dictionary entry
g=collections.defaultdict(list)
for r in L:
    if r['dictionary_id']: g[(r['dictionary_id'],strip(r['lemma']))].append(r['lemma'])
BREATH_MID=re.compile(r'.[̓̔]')
def malformed(x):
    n=unicodedata.normalize('NFD',x)
    return (x.endswith('σ') or BREATH_MID.search(n[1:] if n[:1] else n) and not re.match(r'^.[̓̔]',n)
            or not any(c in n for c in '́̀͂') or '̀' in n or 'garbled' in gl.get(x,''))
MERGE={}
for k,v in g.items():
    v.sort(key=lambda x:-cnt[x]); top=v[0]
    for x in v[1:]:
        if cnt[x]*20<=cnt[top] and x[:1].isupper()==top[:1].isupper() and malformed(x) and not malformed(top):
            MERGE[x]=top
up=lambda s: s[:1].isupper()
def badform(x):
    n=unicodedata.normalize('NFD',x)
    return x.endswith('σ') or bool(re.search(r'.[\u0313\u0314]', n[2:])) or 'garbled' in gl.get(x,'')
REVIEW_CAPS={'Ἐλαιῶν','Ἔρως','Ἔρωτα','Ἔρωτος','Ἔρωτι','Τύχη','Τύχης','Τύχην','Τύχῃ','Νίκη','Νίκην','Δίκη','Δίκην','Δίκης','Φόβος','Φόβον','Ὕπνος','Ὕπνον','Θάνατος','Θάνατον','Πειθώ','Πειθοῦς','Γῆ','Γῆς','Γῆν','Γαῖα','Γαῖαν','Ἥλιος','Ἡλίου','Ἥλιον','Ἡλίῳ','Σελήνη','Σελήνης','Σελήνην','Μοῖρα','Μοῖραν','Ἄτη','Ἄτην','Εἰρήνη','Εἰρήνην'}
def verbish(l): return l.endswith(('ω','ῶ','μαι','μι','μί'))
def stem_ok(w,l): return strip(w)[:3]==strip(l)[:3]
fixes=[]; why=collections.Counter()
HAND={('hdt','1.2.2','6'):'Αἶα',('hdt','1.2.3','32'):'ἁρπαγή'}
for r in csv.DictReader(open(f'{D}/words.tsv'),delimiter='\t',quoting=csv.QUOTE_NONE):
    w=r['word']; lem=(r['lemmas'] or '').split('|')[0]
    if not lem: continue
    c=forms.get(w,[]); new=None; rule=None
    k=(r['work'],r['ref'],r['n'])
    if k in HAND: new, rule = HAND[k], 'hand (print thread)'
    elif lem=='εἰς' and strip(w) in ('εν','ενι','εμ'): new, rule='ἐν','ἐν linked to εἰς'
    elif lem=='ἐάω' and w.startswith('εἴη'): new, rule='εἰμί','εἴη linked to ἐάω'
    elif lem=='χωρή' and r['work']=='hdt': new, rule='χώρη','junk lemma χωρή'
    elif lem=='ὁς' : new, rule='ὅς','junk lemma ὁς'
    elif up(w) and len(w)>1 and not w[1:2].isupper() and not up(lem):
        caps=[x for x in c if up(x) and stem_ok(w,x) and x in gl]
        if caps: new, rule=caps[0], ('REVIEW ' if w in REVIEW_CAPS else '')+'capitalized name linked to common word'+(' (section start)' if r['n']=='1' else '')
    elif not up(w) and up(lem):
        low=[x for x in c if not up(x) and x in gl]
        if low:
            new=low[0]; vl=verbish(new); pv=r['parse'][:1] in ('v','t')
            rule='common word linked to a name' if (not r['parse'] or vl==pv or new=='εἶδον') else 'REVIEW common word linked to a name (parse disagrees)'
    elif lem.endswith('σ') and lem[:-1]+'ς' in gl: new, rule=lem[:-1]+'ς','garbled spelling of a lemma'
    elif lem in MERGE or (lem in gl and badform(lem) and any(x!=lem and x in gl and not malformed(x) and not badform(x) for x in c)):
        good=[x for x in c if x!=lem and x in gl and not malformed(x) and not badform(x)]
        if len(good)==1: new, rule=good[0],'garbled lemma (analyzer has the right one)'
        elif lem in MERGE and stem_ok(w,MERGE[lem]): new, rule=MERGE[lem],'garbled spelling of a lemma'
        else: new, rule=(good[0] if good else MERGE[lem]),'REVIEW garbled lemma'
    if new and new!=lem:
        why[rule]+=1
        fixes.append((rule,r['work'],r['ref'],r['n'],w,lem,gl.get(lem,'')[:60],new,gl.get(new,'(NEW lemma)')[:60]))
with open(OUT,'w') as o:
    o.write('rule\twork\tref\tn\tword\told_lemma\told_meaning\tnew_lemma\tnew_meaning\n')
    for f in fixes: o.write('\t'.join(f)+'\n')
print(why, len(fixes), 'lines', len({(f[1],f[2]) for f in fixes}), 'merge lemmas', len(MERGE))
