import argparse
import logging
from .parser import CSVParser
from .report import SalesReport
from .output import ReportOutput


def main():
    parser = argparse.ArgumentParser(
        description="Gerador de Relatórios de Vendas (CSV → Texto/JSON/CSV)"
    )

    parser.add_argument("csv_file", help="Caminho do arquivo CSV de vendas")

    parser.add_argument("--start", help="Data inicial no formato YYYY-MM-DD", required=False)
    parser.add_argument("--end", help="Data final no formato YYYY-MM-DD", required=False)
    parser.add_argument(
        "--format",
        choices=["text", "json", "csv"],
        default="text",
        help="Formato da saída do relatório (text, json, csv)"
    )

    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

    parser_csv = CSVParser(args.csv_file)
    data = parser_csv.read()

    report = SalesReport(args.csv_file)
    report.sales_data = data
    summary = report.generate_summary(args.start, args.end)

    if args.format == "json":
        output = ReportOutput.to_json(summary)
        print(output)
        with open("relatorio.json", "w", encoding="utf-8") as f:
            f.write(output)
        logging.info("Relatório JSON salvo em 'relatorio.json'")

    elif args.format == "csv":
        output = ReportOutput.to_csv(summary)
        print(output)
        with open("relatorio.csv", "w", encoding="utf-8", newline="") as f:
            f.write(output)
        logging.info("Relatório CSV salvo em 'relatorio.csv'")

    else:
        output = ReportOutput.to_text(summary)
        print(output)
        
if __name__ == "__main__":
    main()
