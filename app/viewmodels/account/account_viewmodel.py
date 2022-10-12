from starlette.requests import Request

from app.data.user import User
from app.viewmodels.shared.viewmodel import ViewModelBase


class AccountViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        self.user = User('jesba', 'barbara.jesacher@gmail.com', 'abcdefgh')
