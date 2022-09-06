from flask import Blueprint
from flask_pydantic import validate
from pydantic import BaseModel, StrictFloat, StrictInt

from core.tools import logic

core_api = Blueprint("", __name__)


class Message(BaseModel):
    """The message model.

    This model is used to validate the request body.
    Only a list of only integers or only floats is allowed.
    """

    __root__: list[StrictInt] | list[StrictFloat]


@core_api.post("/filter")
@validate()
def process_filter(body: Message) -> Message:
    """Process the request body."""
    return Message(__root__=logic.filter_and_sort(body))
