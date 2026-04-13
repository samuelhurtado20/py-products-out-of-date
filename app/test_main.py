import datetime
from unittest.mock import patch
from app.main import outdated_products


def test_outdated_products_identifies_expired_items() -> None:
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
        }
    ]

    # Parcheamos el MÉTODO today dentro de la CLASE date
    with patch("app.main.datetime.date") as mock_date:
        # Configuramos para que today() devuelva una fecha real
        mock_date.today.return_value = datetime.date(2022, 2, 2)
        
        result = outdated_products(products)
        assert result == ["duck"]


def test_no_outdated_products_returns_empty_list() -> None:
    products = [
        {"name": "chicken", "expiration_date": datetime.date(2022, 2, 5)}
    ]

    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = datetime.date(2022, 2, 2)
        
        assert outdated_products(products) == []


def test_product_expiring_today_is_not_outdated() -> None:
    products = [
        {"name": "milk", "expiration_date": datetime.date(2022, 2, 2)}
    ]

    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = datetime.date(2022, 2, 2)
        
        assert outdated_products(products) == []
