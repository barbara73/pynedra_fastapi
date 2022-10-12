from starlette.requests import Request

from app.services import option_service
from app.viewmodels.shared.viewmodel import ViewModelBase


class OrderViewModel(ViewModelBase):
    def __init__(self, option_name: str, request: Request):
        super().__init__(request)

        # self.series_count: int = package_service.series_count()
        # self.image_count: int = package_service.image_count()
        # self.study_count: int = package_service.study_count()
        # self.patient_count: int = package_service.patient_count()

        self.option_name = option_name
        # self.option = option_service.options_list()
        self.option = option_service.get_option_by_id(option_name)
        if not self.option:
            return


