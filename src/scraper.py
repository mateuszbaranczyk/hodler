import httpx


class ScraperError(Exception):
    pass


def get_html(url: str):
    response = httpx.get(url)
    if response.is_success:
        return response.content
    raise ScraperError
