from typing import List, Optional

from app.data.package import Package


def series_count() -> int:
    return 2_234_847


def study_count() -> int:
    return 274_000


def patient_count() -> int:
    return 111


def image_count() -> int:
    return 111_000_000


def packages_list() -> List:
    return [
               {'id': 'Import',
                'summary': "Choose, where the data comes from"},
               {'id': 'Export',
                'summary': "Choose, what to export and where to safe it"},
               {'id': 'DICOM De-identification',
                'summary': "Choose, if DICOM files should be de-identified"},
               {'id': 'Threading',
                'summary': "Make adjustments to the threading"},
               {'id': 'Logging',
                'summary': "Choose compactness of logging"},

           ]


def get_package_by_id(package_name: str) -> Optional[Package]:
    package = Package(
        package_name, "Option name description", "Full details here!"
    )
    return package
