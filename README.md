# natural-language-auto-cloze-overlapper
An Anki plugin for generating automatic cloze overlapped cards using regex

## Usage

**WARNING** Make sure your collection is backed up, this plugin is largely untested in terms of creating broken decks!

Once downloaded, do

```bash
python -m nlaco 'Text you want, you really want, to memorize with overlaps.'
```

and it will create 

```
$ ls *.apkg
nlaco-overlap-1--a9e59fbb-d8f0-45da-9d6e-ea42dc852bf0.apkg  nlaco-overlap-2--a9e59fbb-d8f0-45da-9d6e-ea42dc852bf0.apkg  nlaco-overlap-3--a9e59fbb-d8f0-45da-9d6e-ea42dc852bf0.apkg
```

which can be imported into Anki