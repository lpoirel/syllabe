import sys
from pathlib import Path

from cli import CLI
from gui import GUI

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib


def run(config, runner):
    for path in config["textes"]:
        runner.traite_texte(path)


if __name__ == "__main__":
    config = tomllib.loads((Path(__file__).parent / "config.toml").read_text("utf8"))
    if "--gui" in sys.argv:
        runner = GUI(config)
    else:
        runner = CLI(config)
    run(config, runner)
