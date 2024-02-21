from os import PathLike

import click

from gwss.download import download_file
import resolver
from furl import furl
class Unpkg:

    base_url = furl('https://unpkg.com')

    def __init__(self, package: str, version: str, name: PathLike, s_or_s: str, dest_dir: PathLike, filename: PathLike):
        """

        Args:
            package : str
            The package name
            version : str
            The version number of the package
            name : str | PathLike
            The 'nickname' given to the file
            s_or_s : str
            The string 'scripts' or 'styles'
            dest_dir : PathLike



        """
        self.package = package
        self.version = version
        self.name = name
        self.s_or_s = s_or_s
        self.dest_dir = dest_dir
        self.filename = filename
        self.url = self.base_url


    def unpkg_dl(self, url: str):
        """
        Download the package file from unpkg.com
        Parameters
        ----------
        url : str
            url to download from

        Returns
        -------
        True if file is successfully downloaded
        False otherwise
        """
        download_file(self.url, self.package, self.file, self.dest_dir)

    def unpkg_url(self, *args, **kwargs) -> str:
        """

        :param args:
        :param kwargs: see keywords
        :keyword dir (PathLike):
        :return:
        """
        url = furl(self.base_url)
        # create url
        package = self.package
        url = url.add(path=f"{package}")
        version = self.version
        url = url.add(path=f"@{version}")
        _dir = args[2] or kwargs['dir']
        url = url.add(path=f"{_dir}")
        file = args[3] or kwargs['file']
        url = url.add(path=f"{file}")
        extension = None
        match s_or_s:
            case 'script':
                extension = 'js'
            case 'style':
                extension = 'css'
            case _:
                exit(2) # This should not happen

        click.echo(url)

        return