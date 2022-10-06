from typing import Optional, List

from data.settings import Settings


def get_option_by_id(option: str) -> Optional[Settings]:
    settings = Settings(
        option, "This is the summary", "Full details here!",
    )
    return settings


def options(limit: int = 5) -> List:
    return [
               {'id': 'deidentify', 'summary': "A great web framework"},
               {'id': 'threading', 'summary': "Your favorite ASGI server"},
               {'id': 'logging', 'summary': "Requests for an async world"},
           ][:limit]
