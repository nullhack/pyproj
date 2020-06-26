## Documentation Style


### Code blockquotes with line highlight

```Python hl_lines="1  7 8 9 10 11 12"
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
```

??? optional-class "Source"
    <pre>
    ```Python hl_lines="1  7 8 9 10 11 12"
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
    ```
    </pre>

---

### Footnote

This is a footnote [^1] and this is another footnote[^2]

[^1]: Footnote 1.
[^2]: Footnote 2.

??? optional-class "Source"
    <pre>
    ```This is a footnote[^1] and this is another footnote[^2]
    [^1]: Footnote 1.
    [^2]: Footnote 2.```
    </pre>

---

### Mathematical notation

$p(x|y) = \frac{p(y|x)p(x)}{p(y)}$, \(p(x|y) = \frac{p(y|x)p(x)}{p(y)}\).

??? optional-class "Source"
    <pre>
    ```
    $p(x|y) = \frac{p(y|x)p(x)}{p(y)}$, \(p(x|y) = \frac{p(y|x)p(x)}{p(y)}\).
    ```
    </pre>

---

### Message detail


!!! warning
    Warning message.

??? optional-class "Source"
    <pre>
    ```!!! warning
        Warning message.```
    </pre>

---

### Tab

=== "Tab 1"
    Markdown **content**.

    Multiple paragraphs.

=== "Tab 2"
    More Markdown **content**.

    - list item a
    - list item b

??? optional-class "Source"

    <pre>```=== "Tab 1"
        Markdown **content**.
        Multiple paragraphs.
    ```</pre>

    <pre>```=== "Tab 2"
        More Markdown **content**.
        - list item a
        - list item b
    ```</pre>

---

### Table

| First Header | Second Header | Third Header |
| ------------ | ------------- | ------------ |
| Content Cell | Content Cell  | Content Cell |
| Content Cell | Content Cell  | Content Cell |

??? optional-class "Source"
    <pre>
    ```
    | First Header | Second Header | Third Header |
    | ------------ | ------------- | ------------ |
    | Content Cell | Content Cell  | Content Cell |
    | Content Cell | Content Cell  | Content Cell |
    ```
    </pre>

---

### Task list

- [X] item 1
    * [X] item A
    * [ ] item B
        more text
        + [x] item a
        + [ ] item b
        + [x] item c
    * [X] item C
- [ ] item 2
- [ ] item 3


??? optional-class "Source"
    <pre>
    ```
    - [X] item 1
        * [X] item A
        * [ ] item B
            more text
            + [x] item a
            + [ ] item b
            + [x] item c
        * [X] item C
    - [ ] item 2
    - [ ] item 3
    ```
    </pre>

---

## More

* [pymdown-extensions](https://facelessuser.github.io/pymdown-extensions/)
* [mkdocs-material extensions](https://squidfunk.github.io/mkdocs-material/extensions/admonition/)
