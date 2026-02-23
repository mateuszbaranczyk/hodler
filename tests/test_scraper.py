from unittest.mock import patch

import pytest

from src.scraper import ScraperError, get_html


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
def test_raise_error_on_failure(m_get):
    m_get.return_value.is_success = False
    url = "example.com"

    with pytest.raises(ScraperError):
        get_html(url)

    m_get.assert_called_with(url)
