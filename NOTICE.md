# Credits and licences

The Socratos data is built from these open sources. If you reuse it, credit them (and Socratos) and share
your version under the same licence.

| Source | Licence | Used for |
|---|---|---|
| Perseus Digital Library, *canonical-greekLit* and *canonical-latinLit* | CC BY-SA 4.0 | Greek and Latin texts |
| Perseus Ancient Greek and Latin Dependency Treebank 2.1 | CC BY-SA 3.0 US | lemmas and parses for the words it covers |
| Morpheus morphological analyser, Perseus Project (perseids-tools/morpheus) | code MPL-2.0; stem files CC BY-SA 3.0 US | lemmas and parses for the other words; paradigm tables (Greek); vowel lengths |
| Liddell, Scott & Jones, *A Greek-English Lexicon* (Perseus, *lexica*) | CC BY-SA 4.0 | Greek dictionary entries and short meanings |
| Lewis & Short, *A Latin Dictionary* (Perseus, *lexica*) | CC BY-SA 4.0 | Latin dictionary entries and short meanings |
| W. Smith, *Dictionary of Greek and Roman Biography and Mythology* and *Dictionary of Greek and Roman Geography* (Perseus, *canonical-pdlrefwk*) | CC BY-SA 4.0 | descriptions of people and places |
| Pleiades gazetteer (pleiades.stoa.org) | CC BY 3.0 | some place descriptions |
| William Whitaker, *Words* | free for any use | some Latin short meanings; Latin paradigm tables |
| LatinCy, *la_core_web_lg* (Patrick J. Burns) | MIT; trained partly on CC BY-NC-SA treebanks | the Latin readings chosen in context (separate download) |

## What Socratos changed

- Texts: split into lines or sections with their citation references, cleaned of markup, each word numbered.
- Parses: Perseus treebank tags where the treebank covers a word; elsewhere the Morpheus reading judged
  likeliest, with rule-based fixes. Parses can be wrong.
- Dictionary entries: re-parsed from the Perseus XML into numbered senses, abbreviations written out,
  endings expanded, Latin spelling normalised, citations linked to the texts (`citations.tsv`).
- Short meanings: adapted from LSJ (Greek) and Lewis & Short (Latin), and reviewed by a classics student;
  for Latin, many come from Whitaker's *Words*. Names are condensed from Smith or Pleiades. The column
  `meaning_source` in `lemmas.tsv` names the dictionary each meaning comes from.

## Licences of this download

- `greek` and `latin`: **CC BY-SA 4.0** (see LICENSE.txt). The CC BY-SA 3.0 US parts are shared under 4.0,
  as their licence allows.
- `latin-readings-nc`: **CC BY-NC-SA 4.0** (non-commercial). It is kept separate because the model that
  chose these readings was trained partly on non-commercial data.

Please credit: *Socratos (socratos.org), built from the Perseus Digital Library and the sources above.*

Data from Perseus is available from the Perseus Digital Library; corrections are welcome back to Perseus.
