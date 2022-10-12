import fastapi
from fastapi_chameleon import template
from starlette.requests import Request

from app.viewmodels.packages.details_viewmodel import DetailsViewModel

router = fastapi.APIRouter()


@router.get('/project/import_')
@template(template_file='packages/import_.pt')
def import_(package_name: str, request: Request):
    vm = DetailsViewModel(package_name, request)
    return vm.to_dict()


@router.get('/project/export_')
@template(template_file='packages/export_.pt')
def export_(package_name: str, request: Request):
    vm = DetailsViewModel(package_name, request)
    return vm.to_dict()
#
#
# @router.get('/project/{package_name}')
# @template(template_file='packages/import_.pt')
# def import_(package_name: str, request: Request):
#     vm = DetailsViewModel(package_name, request)
#     return vm.to_dict()
#
#
# @router.get('/project/{package_name}')
# @template(template_file='packages/import_.pt')
# def import_(package_name: str, request: Request):
#     vm = DetailsViewModel(package_name, request)
#     return vm.to_dict()