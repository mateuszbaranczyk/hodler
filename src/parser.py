import re
from decimal import Decimal, InvalidOperation

from bs4 import BeautifulSoup


class BsError(Exception):
    pass


def get_price_decimal(content: str, selected_fragment: str) -> str:
    try:
        selection = get_selection(content, selected_fragment)
    except Exception as e:
        raise BsError(e)
    return extract_price_decimal(selection)


def get_selection(content: str, selected_fragment: str) -> str:
    soup = BeautifulSoup(content, "html.parser")
    tag, class_name = parse_tag(selected_fragment)
    selection = soup.select_one(f"{tag}.{class_name}")
    return selection.get_text()


def parse_tag(html_fragment: str) -> tuple[str, str]:
    soup = BeautifulSoup(html_fragment, "html.parser")
    element = soup.find()
    class_name = element.get("class")
    class_string = " ".join(class_name) if class_name else None

    return element.name, class_string


def extract_price_decimal(text: str) -> Decimal | None:
    match = re.search(r"\d[\d\s.,]*", text)
    if not match:
        return None

    raw = match.group()
    cleaned = raw.replace(" ", "")

    if "," in cleaned and "." in cleaned:
        last_comma = cleaned.rfind(",")
        last_dot = cleaned.rfind(".")

        if last_comma > last_dot:
            cleaned = cleaned.replace(".", "").replace(",", ".")
        else:
            cleaned = cleaned.replace(",", "")
    elif "," in cleaned:
        cleaned = cleaned.replace(",", ".")

    try:
        return Decimal(cleaned)
    except InvalidOperation:
        return None
