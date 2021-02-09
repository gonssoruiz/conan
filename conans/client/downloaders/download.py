from conans.client.downloaders.cached_file_downloader import CachedFileDownloader
from conans.client.downloaders.file_downloader import FileDownloader


def run_downloader(requester, output, verify, config, user_download=False, use_cache=True, **kwargs):
    downloader = FileDownloader(requester=requester, output=output, verify=verify, config=config)
    if use_cache and config.download_cache:
        if config.remote_cache:
            downloader = CachedFileDownloader(remote_cache=config.remote_cache, file_downloader=downloader,
                                              user_download=user_download)
        else:
            downloader = CachedFileDownloader(download_cache=config.download_cache, file_downloader=downloader,
                                              user_download=user_download)
    return downloader.download(**kwargs)
