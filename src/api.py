from dataclasses import dataclass
from datetime import datetime

from src.parser import BsError, get_price_decimal
from src.scraper import ScraperError, get_html


@dataclass
class PriceSelection:
    email: str
    site_url: str
    selected_html: str


@dataclass
class Price:
    amount: str
    date: str


@dataclass
class UserSavedPrice:
    email: str
    site_url: str
    selected_html: str
    price: list[Price]


def save_price(request: PriceSelection) -> UserSavedPrice:
    now = datetime.now()
    now_iso = datetime.isoformat(now)
    try:
        content = get_html(request.site_url)
        price_decimal = get_price_decimal(content, request.selected_html)
    except (ScraperError, BsError) as e:
        raise Exception(e)
    price = Price(amount=price_decimal, date=now_iso)
    user_saved_price = UserSavedPrice(
        email=request.email,
        site_url=request.site_url,
        selected_html=request.selected_html,
        price=[price],
    )
    return user_saved_price
