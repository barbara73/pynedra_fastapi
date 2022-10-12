from starlette.requests import Request

from app.services import option_service
from app.viewmodels.shared.viewmodel import ViewModelBase


class SettingsViewModel(ViewModelBase):
    def __init__(self, option_name: str, request: Request):
        super().__init__(request)

        self.option_name = option_name
        self.option = option_service.get_option_by_id(option_name)
        if not self.option:
            return


