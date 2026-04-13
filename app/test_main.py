import datetime
from unittest.mock import patch
from app.main import outdated_products


def test_outdated_products_identifies_expired_items() -> None:
    # Definimos una lista de productos con distintas fechas
    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]

    # Mockeamos datetime.date.today para que siempre sea 2 de febrero de 2022
    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = datetime.date(2022, 2, 2)
        # Importante: para que el operador < funcione, el mock debe 
        # devolver objetos que se puedan comparar con datetime.date
        mock_date.side_effect = lambda *args,
                                        **kwargs: datetime.date(*args, **kwargs)

        result = outdated_products(products)
        assert result == ["duck"]


def test_no_outdated_products_returns_empty_list() -> None:
    products = [
        {"name": "chicken", "expiration_date": datetime.date(2022, 2, 5)}
    ]

    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = datetime.date(2022, 2, 2)
        mock_date.side_effect = lambda *args,
                                        **kwargs: datetime.date(*args, **kwargs)

        assert outdated_products(products) == []


def test_product_expiring_today_is_not_outdated() -> None:
    # La regla suele ser expiration_date < today_date
    products = [
        {"name": "milk", "expiration_date": datetime.date(2022, 2, 2)}
    ]

    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = datetime.date(2022, 2, 2)
        mock_date.side_effect = lambda *args, **kwargs: datetime.date(*args, **kwargs)

        assert outdated_products(products) == []
