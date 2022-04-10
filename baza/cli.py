import subprocess
import configparser

import typer


DEFAULT_CONFIG_FILES_NAMES = [
    ".bazarc",
]


def main(selector: str):
    config = configparser.ConfigParser()
    config.read(DEFAULT_CONFIG_FILES_NAMES)

    if selector not in config.sections():
        typer.echo(f"{selector} is not a valid selector")
        return

    connection_string = config.get(selector, "connection_string")
    if connection_string is None:
        typer.echo(f"{selector} has no connection string")
        return

    process = subprocess.run(["mongosh", connection_string])


def cli():
    typer.run(main)


if __name__ == "__main__":
    cli()
