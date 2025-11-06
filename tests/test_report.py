import tempfile
import csv
from decimal import Decimal
from src.vendas_cli.report import SalesReport


def create_temp_csv(data):
    """Cria um CSV temporário para os testes."""
    tmp = tempfile.NamedTemporaryFile(mode='w+', newline='', delete=False, encoding='utf-8')
    writer = csv.DictWriter(tmp, fieldnames=["date", "produto", "quantidade"])
    writer.writeheader()
    writer.writerows(data)
    tmp.seek(0)
    return tmp.name


def test_generate_summary_basic():
    data = [
        {"date": "2025-01-01", "produto": "A", "quantidade": "10.00"},
        {"date": "2025-01-02", "produto": "A", "quantidade": "5.00"},
        {"date": "2025-01-03", "produto": "B", "quantidade": "20.00"},
    ]
    csv_path = create_temp_csv(data)

    report = SalesReport(csv_path)
    report.load_data()
    summary = report.generate_summary()

    assert summary["total_sales"] == Decimal("35.00")
    assert summary["best_selling_product"] == "B"
    assert summary["total_per_product"]["A"] == Decimal("15.00")


def test_filter_by_date():
    data = [
        {"date": "2025-01-01", "produto": "A", "quantidade": "10.00"},
        {"date": "2025-02-01", "produto": "B", "quantidade": "20.00"},
    ]
    csv_path = create_temp_csv(data)

    report = SalesReport(csv_path)
    report.load_data()
    filtered = report.filter_by_date(start_date="2025-01-15")

    assert len(filtered) == 1
    assert filtered[0]["produto"] == "B"
