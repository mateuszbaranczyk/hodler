from decimal import Decimal

import pytest

from src.parser import extract_price_decimal, get_price_decimal


def test_parser():
    price = 20
    source = f"""
    <html>
        <body>
            <div class="product">
                <h1>Widget</h1>
                <span class='price'>{price} PLN</span>
            </div>
        </body>
    </html>
    """
    expected_content = Decimal(price)
    selected_fragment = "<span class='price'>20 PLN</span>"
    result = get_price_decimal(source, selected_fragment)

    assert result == expected_content


@pytest.mark.parametrize(
    "text,expected",
    [
        ("19.99", Decimal("19.99")),
        ("100.00", Decimal("100.00")),
        ("1.5", Decimal("1.5")),
        ("19,99", Decimal("19.99")),
        ("100,00", Decimal("100.00")),
        ("1,5", Decimal("1.5")),
        ("1 000", Decimal("1000")),
        ("10 000,50", Decimal("10000.50")),
        ("1.000,99", Decimal("1000.99")),
        ("19 999,99", Decimal("19999.99")),
        ("1 000 000.50", Decimal("1000000.50")),
        ("100", Decimal("100")),
        ("0", Decimal("0")),
        ("Price: 25.99 USD", Decimal("25.99")),
        ("€ 49,99", Decimal("49.99")),
        ("999", Decimal("999")),
        ("no number", None),
        ("", None),
        ("abc def", None),
    ],
)
def test_extract_price_decimal(text, expected):
    result = extract_price_decimal(text)
    assert result == expected
