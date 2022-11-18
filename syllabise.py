"""Decoupe un texte et insère des tokens de fin de syllabe, mot, ligne, paragraphe..."""
from enum import Enum, auto

from decoupe import *


class Token(Enum):
    FinDeSyllabe = auto()
    FinDeMot = auto()
    FinDeLigne = auto()
    FinDeParagraphe = auto()


def syllabise(texte):
    """Affiche le texte avec des pauses"""
    for paragraphe in decoupe_en_paragraphes(texte):
        for ligne in decoupe_en_lignes(paragraphe):
            for mot in decoupe_en_mots(ligne):
                for syllabe in decoupe_en_syllabes(mot):
                    yield syllabe
                    yield Token.FinDeSyllabe
                yield Token.FinDeMot
            yield Token.FinDeLigne
        yield Token.FinDeParagraphe


if __name__ == "__main__":
    from pathlib import Path

    fable = Path(__file__).parent / "exemple" / "fable.txt"
    stream = syllabise(fable.read_text("utf8")[:60])
    print(*stream, sep="\n")
