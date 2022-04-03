import subprocess

import typer


def main():
    process = subprocess.run(["mongo"])
    print(f"Mongo exited ({process.returncode})")


def cli():
    typer.run(main)


if __name__ == "__main__":
    cli()
