"""Awesome template.

A simple module showing how to use docstrings as defined by
[Google Style Guide](https://google.github.io/styleguide/pyguide.html)
Please visit the official website for a complete description.

"""


def template_function(message: str, show: bool = True) -> str:
    """Return a message if `show` is True.

    Args:
        message (str): The message to be returned.
        show (bool): Flag to return the message.

    Return:
        The message. Is show is True, empty string otherwise.

    """
    if show:
        return message
    else:
        return ""


class TemplateClass:
    """Create a class, storing the value of the message as attribute.

    This is the documentation of public attributes for the class.

    A good documentation explains the usage of all parameters and attributes.

    """

    def __init__(self, message: str, show: bool = True):
        """Create the documentation for `__init__` method.

         The `__init__` method can be documented at class level
        or inside the `__init__` method itself. Any is acceptable,
        choose one convention and be consistent on next classes.

        Note:
            The parameter `self` should not be part of `Args` section.

        Args:
            message (str): Message to be returned.
            show (bool): Flag to return the message, default=True.

        """
        self._message = message
        self.show = show

    @property
    def message(self):
        """str: Document properties inside the getter method.

        Returns:
            str: message if show is True, empty string otherwise.
        """
        return self._message if self.show else ""
