import httpx


def get_html(url: str):
    response = httpx.get(url)
    if response.is_success:
        return response.content
    return None
