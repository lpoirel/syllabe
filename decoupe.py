"""Diverses fonctions pour découper du texte"""
import re

import pyphen


def decoupe_en_syllabes(texte, dic=pyphen.Pyphen(lang="fr")):
    """Découpe un mot en syllabes"""
    decoupe = (
        [0] + dic.positions(texte) + [len(texte)]
    )  # les positions des extrémités de syllabes
    for begin, end in zip(
        decoupe[:-1], decoupe[1:]
    ):  # on boucle sur les paires d'extrémités
        yield texte[begin:end]  # on renvoie la syllabe entre les deux extrémités


def decoupe_en_mots(texte):
    """Decoupe une ligne en mots"""
    yield from re.findall(r"\W*\w+\W*", texte)


def decoupe_en_lignes(texte):
    """Découpe un texte en lignes"""
    return texte.splitlines(keepends=True)


def decoupe_en_paragraphes(texte):
    """Découpe un texte en paragraphes"""
    return texte.split("\n\n")
