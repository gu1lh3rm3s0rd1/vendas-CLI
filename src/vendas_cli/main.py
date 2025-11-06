import logging
from parser import CSVParser
from report import SalesReport
from output import ReportOutput


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    # Path do CSV
    csv_path = "vendas.csv"

    parser = CSVParser(csv_path)
    data = parser.read()

    report = SalesReport(csv_path)
    report.sales_data = data  # reutiliza os dados lidos
    summary = report.generate_summary()

    text_output = ReportOutput.to_text(summary)
    print(text_output)

    json_output = ReportOutput.to_json(summary)
    with open("relatorio.json", "w", encoding="utf-8") as f:
        f.write(json_output)
        print("\nRelatório JSON salvo em 'relatorio.json'")


if __name__ == "__main__":
    main()
