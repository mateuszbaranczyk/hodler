from decimal import Decimal
from unittest.mock import patch

from freezegun import freeze_time

from src.api import Price, PriceSelection, UserSavedPrice, save_price


@patch("src.scraper.httpx.get")
def test_create_selection_entry(m_get):
    price_decimal = Decimal("20.00")
    prepare_site_mock(m_get, price_decimal)
    selected_html = f"<span class='price'>{price_decimal} PLN</span>"
    site_url = "example.com/item"
    date = "2000-01-01T00:00:00"
    price = Price(amount=price_decimal, date=date)
    email = "test@test.com"

    expected_result = UserSavedPrice(
        email=email,
        site_url=site_url,
        selected_html=selected_html,
        price=[price],
    )
    request = PriceSelection(
        email=email,
        site_url=site_url,
        selected_html=selected_html,
    )
    with freeze_time(date):
        result = save_price(request)

    assert result == expected_result


def prepare_site_mock(m_get, price_amount):
    source = f"""
    <html>
        <body>
            <div class="product">
                <h1>Widget</h1>
                <span class='price'>{price_amount} PLN</span>
            </div>
        </body>
    </html>
    """
    m_get.return_value.content = source
    m_get.return_value.is_success = True
