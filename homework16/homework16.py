import csv
import json
import logging
from pathlib import Path
import xml.etree.ElementTree as ET




SURNAME = "Parshyna"

BASE_PATH = Path("ideas_for_test")
CSV_PATH = BASE_PATH / "work_with_csv"
JSON_PATH = BASE_PATH / "work_with_json"
XML_PATH = BASE_PATH / "work_with_xml" / "groups.xml"

CSV_RESULT_FILE = f"result_{SURNAME}.csv"
JSON_LOG_FILE = f"json_{SURNAME}.log"




def process_csv_files():
    csv_files = list(CSV_PATH.glob("*.csv"))

    if len(csv_files) < 2:
        print("Недостатньо CSV файлів.")
        return

    file1, file2 = csv_files[0], csv_files[1]

    all_rows = []
    header = None

    for file in [file1, file2]:
        with open(file, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            file_header = next(reader)

            if header is None:
                header = file_header

            for row in reader:
                all_rows.append(row)


    unique_rows = []
    seen = set()

    for row in all_rows:
        row_tuple = tuple(row)
        if row_tuple not in seen:
            seen.add(row_tuple)
            unique_rows.append(row)

    with open(CSV_RESULT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(unique_rows)

    print(f"CSV опрацьований. Результат збережений в {CSV_RESULT_FILE}")




def validate_json_files():
    logger = logging.getLogger("json_validator")
    logger.setLevel(logging.ERROR)

    file_handler = logging.FileHandler(JSON_LOG_FILE, encoding="utf-8")
    file_handler.setLevel(logging.ERROR)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    for json_file in JSON_PATH.glob("*.json"):
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                json.load(f)
        except json.JSONDecodeError as e:
            logger.error(
                f"Файл {json_file.name} невалидный JSON: {e}"
            )

    print(f"Перевірка JSON завершена. Лог в {JSON_LOG_FILE}")




logger = logging.getLogger(__name__)

def find_incoming_by_group_number(number: str):
    try:
        tree = ET.parse(XML_PATH)
    except ET.ParseError as e:
        logger.error(f"XML is invalid: {e}")
        return None

    root = tree.getroot()

    for group in root.findall(".//{*}group"):
        group_number = group.find(".//{*}number")
        if group_number is not None and group_number.text == number:
            incoming = group.find(".//{*}incoming")
            return incoming.text if incoming is not None else None

    return None


def process_xml():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    logger = logging.getLogger("xml_processor")

    number_to_search = "1"

    incoming = find_incoming_by_group_number(number_to_search)

    if incoming:
        logger.info(
            f"Для group number={number_to_search} incoming={incoming}"
        )
    else:
        logger.info(
            f"Group с number={number_to_search} не знайдено"
        )



if __name__ == "__main__":
    process_csv_files()
    validate_json_files()
    process_xml()