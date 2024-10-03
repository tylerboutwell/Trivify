import tomllib
from pprint import pprint

from quiz import run_quiz



def load_toml() -> dict:
    with open("questions.toml", "rb") as f:
        toml_data: dict = tomllib.load(f)
        return toml_data

if __name__ == "__main__":
    data = load_toml()
    run_quiz(data)