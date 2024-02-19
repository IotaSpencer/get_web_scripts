from os import PathLike

from gwss.download import download_file
import resolver
from furl import furl
class Unpkg:

    base_url = furl('https://unpkg.com')

    def __init__(self, package: str, version: str, file: PathLike, s_or_s: str):
        """

        Args:
            package (str): The package name
            version (str):
            file (str | PathLike): The full filename including preceding path and excluding extension
            s_or_s:
        """
        self.package = package
        self.version = version
        self.file = file
        self.s_or_s = s_or_s

        self.url = self.base_url


    def unpkg_dl(self, url: str, dest_dir: PathLike, dest_file: PathLike):
        """

        Parameters
        ----------
        url : str
        dest_dir : PathLike
        dest_file : PathLike

        Returns
        -------

        """
        download_file(self.url, self.package, self.file, self.version, self.s_or_s, dest_dir)

    def unpkg_url(self, *args, **kwargs) -> str:
        """

        :param args:
        :param kwargs: see keywords
        :keyword dir (PathLike):
        :return:
        """
        # create url
        package = self.package
        version = self.version
        _dir = args[2] or kwargs['dir']
        file = args[3] or kwargs['file']



        return