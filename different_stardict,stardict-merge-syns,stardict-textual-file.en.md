Q: What is the difference betwen StarDict (.ifo), Stardict (Merge Syns), StarDict Textual File (.xml)?

A: The differences between the StarDict file types are as follows:

- StarDict .ifo file: This is a plain-text file containing metadata about the dictionary such as the version, word count, dictionary name, index file size, and creation date. It helps StarDict allocate memory and scan the index file properly but does not contain the actual dictionary content. It serves mainly for dictionary information and configuration.

- Stardict (Merge Syns): This is not a standard StarDict file but rather a special plugin/format option used by PyGlossary or KOReader for merging synonyms in StarDict dictionaries. It is used when converting or creating dictionaries to fix limitations related to synonym lookups in certain apps. It combines multiple synonym entries to enhance dictionary lookup functionality.

- StarDict Textual File (.xml): This is a textual representation of the dictionary data in XML format. It can be used for editing or converting StarDict dictionaries to other readable formats. The XML file includes dictionary entries with definitions and related data in a structured markup format.

In summary:
- .ifo is metadata file for dictionary configuration.
- Merge Syns is a special merging format/plugin for synonym handling.
- .xml is a textual XML format of the dictionary content itself.

These files serve different purposes in the StarDict dictionary ecosystem. 

If needed, tools like PyGlossary or stardict-tools can convert between these formats for editing or use in different dictionary apps.

[perplexingly.ai]