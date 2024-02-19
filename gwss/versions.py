from typing import Union

from lastversion import latest
def get_latest(package: str) -> str:
    version: Union[object, str] = latest(package, output_format='tag')
    assert version is not None
    return version