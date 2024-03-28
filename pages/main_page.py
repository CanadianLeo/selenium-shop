from typing import Any
from typing_extensions import Self

from .base_page import BasePage


class MainPage(BasePage):
    def __init__(self: Self, *args: tuple[Any], **kwargs: dict[str, Any]) -> None:
        super(MainPage, self).__init__(*args, **kwargs)
