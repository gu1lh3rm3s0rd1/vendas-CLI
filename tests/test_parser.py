import tempfile
import csv
# import pytest
from src.vendas_cli.parser import CSVParser 


def create_temp_csv(data, fieldnames=None):
    fieldnames = fieldnames or ["produto", "quantidade", "preco_unitario"]
    tmp = tempfile.NamedTemporaryFile(mode='w+', newline='', delete=False, encoding='utf-8')
    writer = csv.DictWriter(tmp, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
    tmp.seek(0)
    return tmp.name


def test_read_valid_csv():
    data = [{"produto": "A", "quantidade": "10.00", "preco_unitario": "5.00"}]
    csv_path = create_temp_csv(data)
    parser = CSVParser(csv_path)
    result = parser.read()
    assert len(result) == 1
    assert result[0]["produto"] == "A"



