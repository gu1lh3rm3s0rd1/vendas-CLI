from decimal import Decimal
from src.vendas_cli.output import ReportOutput


def test_to_json():
    summary = {
        "total_per_product": {"A": Decimal("10.00")},
        "total_sales": Decimal("10.00"),
        "best_selling_product": "A",
        "best_selling_value": Decimal("10.00"),
    }
    result = ReportOutput.to_json(summary)
    assert '"A"' in result
    assert "10.00" in result


def test_to_text():
    summary = {
        "total_per_product": {"A": Decimal("10.00")},
        "total_sales": Decimal("10.00"),
        "best_selling_product": "A",
        "best_selling_value": Decimal("10.00"),
    }
    result = ReportOutput.to_text(summary)
    assert "RELATÓRIO DE VENDAS" in result
    assert "A" in result
