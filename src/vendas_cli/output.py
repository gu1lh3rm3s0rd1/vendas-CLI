import json
import io, csv
from decimal import Decimal
from typing import Dict


class ReportOutput:
    """
    Formata os dados do relatório em texto (tabela simples) ou JSON.
    """

    @staticmethod
    def to_json(summary: Dict) -> str:
        """Retorna o relatório em formato JSON."""
        def default(o):
            if isinstance(o, Decimal):
                return str(o)
            return o

        return json.dumps(summary, indent=4, ensure_ascii=False, default=default)

    @staticmethod
    def to_text(summary: Dict) -> str:
        """Retorna o relatório formatado como texto."""
        lines = []
        lines.append("=== RELATÓRIO DE VENDAS ===\n")

        lines.append("Total de vendas por produto:")
        for product, value in summary["total_per_product"].items():
            lines.append(f"  - {product:<20} R$ {value:>10}")

        lines.append(f"\nValor total de vendas: R$ {summary['total_sales']}")
        lines.append(f"Produto mais vendido:  {summary['best_selling_product']} (R$ {summary['best_selling_value']})")

        return "\n".join(lines)

    @staticmethod
    def to_csv(summary: Dict) -> str:
            """
            Gera um CSV com o total de vendas por produto.
            Também inclui as informações resumidas no final.
            """
            output = io.StringIO()
            writer = csv.writer(output)
            writer.writerow(["Produto", "Total de Vendas (R$)"])

            for product, value in summary["total_per_product"].items():
                writer.writerow([product, value])

            writer.writerow([])
            writer.writerow(["Valor Total de Vendas", summary["total_sales"]])
            writer.writerow(["Produto Mais Vendido", summary["best_selling_product"]])
            writer.writerow(["Valor do Produto Mais Vendido", summary["best_selling_value"]])

            return output.getvalue()

   