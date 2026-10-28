# Socratos data

The Greek and Latin text and dictionary data behind [Socratos](https://socratos.org), a free reader for
ancient Greek and Latin, shared under the same open licences as the sources it was built from.

**Download:** see [Releases](https://github.com/tferris13/socratos-data/releases/latest). Each release has three zip files:

| File | What is in it | Licence |
|---|---|---|
| `greek.zip` | 555 Greek works: passages, every word with its lemma and parse, LSJ entries, short meanings, citations, paradigm tables | CC BY-SA 4.0 |
| `latin.zip` | 170 Latin works: the same with Lewis & Short, plus scansion of the verse | CC BY-SA 4.0 |
| `latin-readings-nc.zip` | the reading chosen for each Latin word in its sentence | CC BY-NC-SA 4.0 (non-commercial) |

Files are plain TSV and JSON Lines. [FORMAT.md](FORMAT.md) explains every column and the parse codes.

## Where it comes from

Texts, treebank parses and dictionaries come from the [Perseus Digital Library](https://www.perseus.tufts.edu/)
and related projects. Short meanings are adapted from LSJ (Greek) and Lewis & Short (Latin) and reviewed by a
classics student; many Latin meanings come from William Whitaker's *Words*. Full credits, and what Socratos
changed, are in [NOTICE.md](NOTICE.md).

Parses and meanings are a reading aid and can be wrong. Corrections are welcome: open an issue here, or use
*Report a mistake* on socratos.org.

## Licence

`greek.zip` and `latin.zip`: [CC BY-SA 4.0](LICENSE). `latin-readings-nc.zip`:
[CC BY-NC-SA 4.0](LICENSE-latin-readings-nc.txt). If you reuse the data, credit
*Socratos (socratos.org), built from the Perseus Digital Library* and the sources in NOTICE.md, and share
your version under the same licence.

This repository holds data only. The Socratos website and app are a separate project.
