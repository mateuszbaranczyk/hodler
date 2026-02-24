from unittest.mock import patch

from src.api import Price, UserSavedPrice
from src.tasks import get_prices


@patch("src.tasks.send_notification")
@patch("src.tasks.compare_price")
@patch("src.tasks.check_price")
@patch("src.tasks.get_saved_prices")
def test_task_get_prices(
    m_get_prices_data, m_check_price, m_compare_price, m_notification
):
    saved_user_price = UserSavedPrice(
        email="",
        site_url="",
        selected_html="",
        price=[Price(amount="20.00", date="2000-01-01")],
    )
    saved_prices = [saved_user_price]
    m_get_prices_data.return_value = saved_prices
    m_compare_price.return_value = True
    m_check_price.return_value = saved_user_price

    task = get_prices()

    m_get_prices_data.assert_called_once()
    m_check_price.assert_called_once_with(saved_user_price)
    m_compare_price.assert_called_once_with(saved_user_price)
    m_notification.assert_called_once_with(to=saved_user_price.email, msg="")
    assert task is None
