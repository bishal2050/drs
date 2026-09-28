import csv
from pathlib import Path


def read_csv_data(file_path, required_columns):
    path = Path(file_path)
    if not path.is_file():
        raise FileNotFoundError(f"CSV test data file not found: {path}")

    with path.open(mode="r", encoding="utf-8-sig", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        missing_columns = set(required_columns) - set(reader.fieldnames or [])
        if missing_columns:
            raise ValueError(
                f"CSV file is missing required columns: {', '.join(sorted(missing_columns))}"
            )

        rows = [
            {column: (row[column] or "").strip() for column in required_columns}
            for row in reader
        ]

    if not rows:
        raise ValueError(f"CSV test data file contains no test cases: {path}")

    return rows
