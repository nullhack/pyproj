"""Command line interface.

Awesome CLI description.

"""

import typer
from pyproj.template import template_function

app = typer.Typer()


@app.command()
def run(show: bool = typer.Option(None, "--show", "-s")):
    """Awesome function."""
    if show:
        typer.echo(template_function("hello world", show))
    else:
        typer.echo("*****")


if __name__ == "__main__":
    app()
