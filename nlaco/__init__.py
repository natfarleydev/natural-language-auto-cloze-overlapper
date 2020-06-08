import re
from typing import List, Set
from uuid import uuid4

phrase_separators = ".;,\n!"
split_by_phrase_separators_pattern = re.compile(
    f"(?<=[{phrase_separators}])?[^{phrase_separators}]+?(?=[${phrase_separators}])"
)


def get_phrases(text) -> List[str]:
    return [x.strip() for x in split_by_phrase_separators_pattern.findall(text)]


def get_card_contents(text: str, phrases_per_cloze=1) -> Set[str]:
    phrases = get_phrases(text)

    retset = set()
    for i in range(phrases_per_cloze, len(phrases) + 1):
        p = phrases[i - phrases_per_cloze : i]
        assert len(p) == phrases_per_cloze, f"Problem!!! {p}"
        retset.add(re.sub(f"({'.+?'.join(p)})", r"{{c1::\1}}", text, flags=re.DOTALL))

    return retset


def create_anki_deck(text, deckname=None, filename=None):
    from genanki import Model, Note, Deck, Package

    # This is mostly hobbled together from the tests for genanki
    CSS = """.card {
    font-family: arial;
    font-size: 20px;
    text-align: center;
    color: black;
    background-color: white;
    }
    .cloze {
    font-weight: bold;
    color: blue;
    }
    .nightMode .cloze {
    color: lightblue;
    }
    """

    MY_CLOZE_MODEL = Model(
        998877661,
        "Nlaco Cloze Model",
        fields=[{"name": "Text"}, {"name": "Extra"},],
        templates=[
            {
                "name": "Nlaco Cloze Card",
                "qfmt": "{{cloze:Text}}",
                "afmt": "{{cloze:Text}}<br>{{Extra}}",
            },
        ],
        css=CSS,
        model_type=Model.CLOZE,
    )

    name_uuid = uuid4()

    for overlap in range(1, 4):

        notes = [
            Note(model=MY_CLOZE_MODEL, fields=(p, ""))
            for p in get_card_contents(text, phrases_per_cloze=overlap)
        ]
        for n in notes:
            assert (
                n.cards
            ), f"No cards in note {n}, this will cause your Anki DB to break!"

        if deckname is None:
            _deckname = f"nlaco-overlap-{overlap}--" + str(name_uuid)
        else:
            raise NotImplementedError("Custom decknames are not supported yet :(")

        # % 500000 to make sure the int can fit into an SQL database. TODO see
        # whether this is random enough to make sure there are no collisions.
        deck = Deck(deck_id=name_uuid.int % 500000, name=_deckname)
        for note in notes:
            deck.add_note(note)

        if filename is None:
            Package(deck).write_to_file(f"{_deckname}.apkg")
        else:
            raise NotImplementedError("Custom filenames are not supported yet :(")
