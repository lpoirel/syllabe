from pathlib import Path

from syllabise import Token, syllabise


class Runner:
    def clear(self):
        raise NotImplementedError

    def print(self, texte):
        raise NotImplementedError

    def pause(self, duration):
        raise NotImplementedError

    def __init__(self, config):
        self.actions = self.configure(config)

    def configure(self, config):
        actions = {}
        for cle in ("FinDeSyllabe", "FinDeMot", "FinDeLigne", "FinDeParagraphe"):
            actions[cle] = list()
            for command in config[cle]:
                match command.split():
                    case ["clear"]:
                        actions[cle].append(self.clear)
                    case "print", txt:
                        actions[cle].append(lambda txt_=txt: self.print(txt_))
                    case "pause", duration:
                        actions[cle].append(
                            lambda duration_=float(duration): self.pause(duration_)
                        )
                    case other:
                        print("Attention, autre action inconnue :", *other)
        return actions

    def traite_token(self, token):
        if type(token) is Token:
            for action in self.actions[token.name]:
                action()
        else:
            self.print(token)

    def traite_texte(self, path):
        self.clear()
        self.print(f"On va lire le texte {path}")
        self.pause(3)
        self.clear()

        for token in syllabise(Path(path).read_text(encoding="utf8")):
            self.traite_token(token)
