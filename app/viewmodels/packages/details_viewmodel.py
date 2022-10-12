from starlette.requests import Request

from app.services import package_service
from app.viewmodels.shared.viewmodel import ViewModelBase


class DetailsViewModel(ViewModelBase):
    def __init__(self, package_name: str, request: Request):
        super().__init__(request)

        self.package_name = package_name
        self.package = package_service.get_package_by_id(package_name)
        # self.package: List = package_service.packages_list()

        if not self.package:
            return


