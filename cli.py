"""Command line interface.

Awesome CLI description.

"""

import typer

app = typer.Typer()


@app.command()
def run(show: bool = typer.Option(None, "--show", "-s")):
    """Awesome function."""
    if show:
        typer.echo("hello world")
    else:
        typer.echo("*****")


if __name__ == "__main__":
    app()
