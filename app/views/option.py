import fastapi
from fastapi_chameleon import template
from starlette.requests import Request

from app.viewmodels.option.order_viewmodel import OrderViewModel
from app.viewmodels.option.settings_viewmodel import SettingsViewModel

router = fastapi.APIRouter()


@router.get('/option/order')
@template(template_file='option/order.pt')
def order(option_name: str, request: Request):
    vm = OrderViewModel(option_name, request)
    return vm.to_dict()


@router.get('/option/settings')
@template(template_file='option/settings.pt')
def settings(option_name: str, request: Request):
    vm = SettingsViewModel(option_name, request)
    return vm.to_dict()
