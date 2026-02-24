from src.api import UserSavedPrice
from src.sender import send_notification


def get_prices():
    prices = get_saved_prices()
    for price in prices:
        updated_price = check_price(price)
        is_price_lower = compare_price(updated_price)
        if is_price_lower:
            send_notification(to=price.email, msg="")
    return None


def get_saved_prices() -> list[UserSavedPrice]:
    # TODO query
    return []


def check_price(user_saved_price: UserSavedPrice) -> UserSavedPrice:
    # TODO checking price for saved data, check func api.save_price
    return None


def compare_price(user_saved_price: UserSavedPrice) -> bool:
    # TODO comapre price with history
    return True
