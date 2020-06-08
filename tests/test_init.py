import nlaco


def test_get_phrases():
    text = "Lorem ipsum. Foo bar."

    retval = nlaco.get_phrases(text)

    assert retval
    assert len(retval) == 2


def test_get_phrases__seprates_on_comma_with_exclamation_mark():
    text = "Hello, world!"

    retval = nlaco.get_phrases(text)

    assert retval
    assert len(retval) == 2


def test_get_phrases__test_separates_on_semicolon():
    text = "Lorem ipsum. Foo; bar."

    retval = nlaco.get_phrases(text)

    assert retval
    assert len(retval) == 3


def test_get_phrases__combines_consequtive_newlines():
    text = "Lorem ipsum\n\n\n Foo; bar."

    retval = nlaco.get_phrases(text)

    assert retval
    assert len(retval) == 3
    assert "Lorem ipsum" in retval
    assert "Foo" in retval
    assert "bar" in retval


def test_get_card_contents():
    text = "Lorem ipsum\n\n\n Foo; bar."

    retval = nlaco.get_card_contents(text)

    assert retval
    assert len(retval) == 3
    assert "{{c1::Lorem ipsum}}\n\n\n Foo; bar." in retval


def test_get_card_contents__overlap_2():
    text = "Lorem ipsum\n\n\n Foo; bar."

    retval = nlaco.get_card_contents(text, phrases_per_cloze=2)

    assert retval
    assert len(retval) == 2
    assert "{{c1::Lorem ipsum\n\n\n Foo}}; bar." in retval

def test_get_card_contents__overlap_3():
    text = "Lorem ipsum\n\n\n Foo; bar."

    retval = nlaco.get_card_contents(text, phrases_per_cloze=3)

    assert retval
    assert len(retval) == 1
    assert "{{c1::Lorem ipsum\n\n\n Foo; bar}}." in retval