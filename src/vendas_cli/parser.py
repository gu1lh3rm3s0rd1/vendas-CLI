import csv
import logging
from typing import List, Dict

logger = logging.getLogger(__name__)


class CSVParser:
    """
    Responsável por ler e validar o arquivo CSV de vendas.
    Espera colunas: produto, produto, preco_unitario
    """

    REQUIRED_COLUMNS = ["quantidade", "produto", "preco_unitario"]

    def __init__(self, filepath: str):
        self.filepath = filepath

    def read(self) -> List[Dict[str, str]]:
        """Lê o CSV e retorna uma lista de dicionários."""
        encodings = ["utf-8", "utf-8-sig", "cp1252", "latin-1"]
        last_exc: Exception | None = None

        for enc in encodings:
            try:
                with open(self.filepath, newline='', encoding=enc) as csvfile:
                    reader = csv.DictReader(csvfile)
                    missing = [col for col in self.REQUIRED_COLUMNS if col not in (reader.fieldnames or [])]
                    if missing:
                        raise ValueError(f"Colunas ausentes no CSV: {missing}")
                    data = [row for row in reader]
                    logger.info(f"{len(data)} registros lidos de {self.filepath} (encoding={enc})")
                    return data
            except FileNotFoundError:
                logger.error(f"Arquivo não encontrado: {self.filepath}")
                raise
            except UnicodeDecodeError as e:
                logger.warning(f"Falha ao decodificar {self.filepath} usando {enc}: {e}. Tentando outro encoding.")
                last_exc = e
                continue
            except Exception as e:
                logger.exception(f"Erro ao ler o CSV: {e}")
                raise

        # nenhum encoding funcionou
        if last_exc:
            logger.error(f"Não foi possível decodificar o arquivo {self.filepath} com os encodings testados: {encodings}")
            raise last_exc
        # caso improvável: nenhum erro registrado
        raise RuntimeError(f"Falha desconhecida ao ler o arquivo {self.filepath}")
