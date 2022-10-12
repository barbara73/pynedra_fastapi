from typing import List

from starlette.requests import Request

from app.services import option_service
from app.viewmodels.shared.viewmodel import ViewModelBase


class IndexViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.option: List = option_service.options_list()
