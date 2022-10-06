import datetime
from typing import List, Optional

from starlette.requests import Request

from data.release import Release
from services import package_service, user_service
from viewmodels.shared.viewmodel import ViewModelBase


class OptionsViewModel(ViewModelBase):
    def __init__(self, option: str, request: Request):
        super().__init__(request)

        self.option = option
        self.setting = package_service.get_package_by_id(option)

        if not self.option:
            return
