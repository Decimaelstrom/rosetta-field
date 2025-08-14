import argparse
import json
import os
import sqlite3
from typing import Any, Dict, List


def read_sqlite_db_readonly(db_path: str, sample_rows: int = 5) -> Dict[str, Any]:
    """Open a SQLite database in read-only mode and return table metadata with sample rows.

    Returns a dictionary with keys:
    - db_path: absolute path to the database
    - tables: list of { name, columns, rows }
    - error: optional error string if the db could not be opened
    """
    result: Dict[str, Any] = {"db_path": db_path, "tables": []}

    # Try read-only URI; some files may be locked by the editor
    try:
        uri = f"file:{db_path}?mode=ro"
        conn = sqlite3.connect(uri, uri=True)
    except Exception as exc:
        result["error"] = f"open_failed: {exc}"
        return result

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        table_names = [row[0] for row in cursor.fetchall()]

        for table_name in table_names:
            table_info: Dict[str, Any] = {"name": table_name, "columns": [], "rows": []}
            try:
                cursor.execute(f"SELECT * FROM {table_name} LIMIT {int(sample_rows)}")
                rows = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description] if cursor.description else []
                table_info["columns"] = columns
                # Convert any non-JSON-serializable objects to string
                serializable_rows: List[List[Any]] = []
                for row in rows:
                    serializable_rows.append([str(v) if not isinstance(v, (int, float, str, type(None))) else v for v in row])
                table_info["rows"] = serializable_rows
            except Exception as table_exc:
                table_info["error"] = f"read_failed: {table_exc}"
            result["tables"].append(table_info)
    finally:
        try:
            conn.close()
        except Exception:
            pass

    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Dump tables and sample rows from SQLite databases under a directory.")
    parser.add_argument("root", help="Root directory to scan for .vscdb/.db files")
    parser.add_argument("--limit", type=int, default=5, help="Sample rows per table (default: 5)")
    args = parser.parse_args()

    roots: List[str] = [args.root]
    db_paths: List[str] = []

    for root in roots:
        for dirpath, _, filenames in os.walk(root):
            for filename in filenames:
                if filename.endswith(".vscdb") or filename.endswith(".db"):
                    db_paths.append(os.path.join(dirpath, filename))

    outputs: List[Dict[str, Any]] = []
    for db_path in sorted(db_paths):
        outputs.append(read_sqlite_db_readonly(db_path, sample_rows=args.limit))

    print(json.dumps(outputs, indent=2))


if __name__ == "__main__":
    main()


