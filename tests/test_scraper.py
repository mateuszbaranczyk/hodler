from unittest.mock import patch

from src.scraper import get_html


@patch("src.scraper.httpx.get")
def test_get_html(m_get):
    expected_site = "<test>"
    m_get.return_value.content = expected_site
    m_get.return_value.is_success = True
    url = "example.com"

    result = get_html(url)

    m_get.assert_called_with(url)
    assert result == expected_site


@patch("src.scraper.httpx.get")
def test_return_none_on_error(m_get):
    m_get.return_value.is_success = False
    url = "example.com"

    result = get_html(url)

    m_get.assert_called_with(url)
    assert result is None
