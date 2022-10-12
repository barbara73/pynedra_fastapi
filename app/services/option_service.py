from typing import List, Optional

from app.data.option import Option


def options_list() -> List:
    return [
               {'id': 'order',
                'summary': "Create an order table for ordering DICOM images from Synedra"},
               {'id': 'settings',
                'summary': "Set options for saving DICOM images"},
           ]


def get_option_by_id(option_name: str) -> Optional[Option]:
    print('here I am in get options by id')
    option = Option(
        option_name, "Option name description", "Full details here!"
    )
    return option
