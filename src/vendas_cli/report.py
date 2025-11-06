import csv
import logging
from datetime import datetime
from decimal import Decimal
from typing import List, Dict, Optional

logger = logging.getLogger(__name__)


class SalesReport:
    """
    Classe responsável por processar arquivos CSV de vendas e gerar relatórios.
    """

    def __init__(self, csv_path: str):
        self.csv_path = csv_path
        self.sales_data: List[Dict[str, str]] = []

    def load_data(self) -> None:
        """Lê o arquivo CSV e carrega os registros em memória."""
        try:
            with open(self.csv_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                self.sales_data = [row for row in reader]
                logger.info(f"{len(self.sales_data)} registros carregados.")
        except FileNotFoundError:
            logger.error(f"Arquivo não encontrado: {self.csv_path}")
            raise
        except Exception as e:
            logger.exception(f"Erro ao ler CSV: {e}")
            raise

    def _parse_date(self, date_str: str) -> datetime:
        """Converte string de data em datetime."""
        return datetime.strptime(date_str, "%Y-%m-%d")

    def _parse_decimal(self, value: str) -> Decimal:
        """Converte string numérica em Decimal."""
        try:
            return Decimal(value)
        except Exception:
            logger.warning(f"Valor inválido detectado: {value!r}, retornando 0.")
            return Decimal("0.00")

    def filter_by_date(self, start_date: Optional[str] = None, end_date: Optional[str] = None) -> List[Dict[str, str]]:
        """
        Filtra os registros de vendas por intervalo de datas.
        """
        if not start_date and not end_date:
            return self.sales_data

        start = self._parse_date(start_date) if start_date else None
        end = self._parse_date(end_date) if end_date else None

        filtered = []
        for row in self.sales_data:
            try:
                sale_date = self._parse_date(row["date"])
            except Exception:
                logger.warning(f"Data inválida ignorada: {row.get('date')}")
                continue

            if start and sale_date < start:
                continue
            if end and sale_date > end:
                continue
            filtered.append(row)

        logger.info(f"{len(filtered)} registros após filtro de data.")
        return filtered

    def generate_summary(self, start_date: Optional[str] = None, end_date: Optional[str] = None) -> Dict[str, object]:
        """
        Gera o relatório de vendas:
        - Total de vendas por produto
        - Valor total de vendas
        - Produto mais vendido
        """
        data = self.filter_by_date(start_date, end_date)
        total_per_product: Dict[str, Decimal] = {}

        for row in data:
            product = row.get("produto", "N/A")
            amount = self._parse_decimal(row.get("quantidade", "0"))
            total_per_product[product] = total_per_product.get(product, Decimal("0")) + amount

        total_sales = sum(total_per_product.values(), Decimal("0"))
        best_selling = max(total_per_product.items(), key=lambda x: x[1], default=("N/A", Decimal("0")))

        return {
            "total_per_product": total_per_product,
            "total_sales": total_sales,
            "best_selling_product": best_selling[0],
            "best_selling_value": best_selling[1],
        }
