# File format

All files are UTF-8. `.tsv` files have one header row and tab-separated columns (tabs and line breaks
inside a cell are replaced by spaces). `.jsonl` files have one JSON object per line.

## Files in `greek/` and `latin/`

| File | One row per | Columns |
|---|---|---|
| `works.tsv` | text | `work` (id), `author`, `title`, `native_title`, `kind` (`line` = verse, numbered by line) |
| `passages.tsv` | line or section | `work`, `ref` (citation, e.g. `1.1` = book 1 line 1), `book`, `chapter`, `text` |
| `words.tsv` | word in the texts | `work`, `ref`, `n` (word number within the passage, from 1), `word`, `lemmas` (dictionary forms, likeliest first, joined by `\|`), `parse` (Greek only: the one reading chosen for this word in context, where there is one), `possible_parses` (every reading the analyser allows for this spelling, joined by `\|`) |
| `forms.tsv` | distinct spelling | `form`, `possible_parses`, `lemmas` |
| `lemmas.tsv` | dictionary word | `lemma`, `short_meaning`, `meaning_source`, `count` (times it occurs in the texts), `dictionary_id` |
| `dictionary.jsonl` | dictionary entry | `id`, `head`, `short`, `text` (plain text), `structured` (senses, citations; see below), `source` |
| `citations.tsv` | citation in an entry | `dictionary_id`, `head`, `work`, `ref`, `sense`, `meaning` — where a dictionary entry cites one of these texts |
| `paradigms.jsonl` | word with a table of forms | `lemma`, `kind`, `status` (`generated, unchecked` = made by software), `table` |
| `scansion.jsonl` (Latin) | line of verse | `work`, `ref`, `scansion` (`m` metre, `p` feet pattern, `y` syllables as [start, end, quantity, ictus]) |

## Files in `latin-readings-nc/`

`readings.tsv`: `work`, `ref`, `n`, `word`, `parse` — the one reading chosen for each Latin word in its
sentence. Join it to `latin/words.tsv` on (`work`, `ref`, `n`). Licence CC BY-NC-SA 4.0.

## Parse codes

Parses use the 9-character Perseus treebank tags. Position by position:

1. part of speech: `n` noun, `v` verb, `a` adjective, `d` adverb, `l` article, `g` particle, `c` conjunction,
   `r` preposition, `p` pronoun, `m` numeral, `i` interjection, `e` exclamation, `t` participle, `w` noun or adjective, `x` irregular, `u` punctuation
2. person: `1` `2` `3`
3. number: `s` singular, `p` plural, `d` dual
4. tense: `p` present, `i` imperfect, `r` perfect, `l` pluperfect, `t` future perfect, `f` future, `a` aorist
5. mood: `i` indicative, `s` subjunctive, `o` optative, `n` infinitive, `m` imperative, `p` participle, `g` gerundive, `d` gerund, `u` supine
6. voice: `a` active, `p` passive, `m` middle, `e` middle-passive, `d` deponent
7. gender: `m` masculine, `f` feminine, `n` neuter
8. case: `n` nominative, `g` genitive, `d` dative, `a` accusative, `v` vocative, `b` ablative, `l` locative
9. degree: `c` comparative, `s` superlative

`-` means the position does not apply. Example: `v3saia---` = verb, 3rd person singular aorist indicative active.

## Structured dictionary entries

`structured` is the form Socratos uses to display an entry: `h` headword, `w` the works cited (`ab`
abbreviation, `a` author, `ti` title, `id` the Socratos work id when the text is in this download), `p`
parts, each with a heading `hd` and senses `s` (`n` sense label, `p` content). Content is a list of plain
strings and tagged pieces such as `["g", text]` (Greek), `["s", text]` (a cross-reference) and
`["r", ...]` (a citation of a cited work, pointing into `w`). Use `text` if you only want the entry as plain text.
