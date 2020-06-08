import argparse

from . import create_anki_deck, get_card_contents


def parse_args():
    parser = argparse.ArgumentParser("Nlaco command line generator")
    parser.add_argument("text", help="Text to create a card for")
    
    return parser.parse_args()

if __name__ == "__main__":
    parsed = parse_args()

    create_anki_deck(parsed.text)
