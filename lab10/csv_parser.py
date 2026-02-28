#!/usr/bin/env python3
"""
CSV Parser - A command-line tool for parsing and analyzing CSV files
"""

import csv
import argparse
import sys
from typing import List, Dict, Any


def read_csv_file(filename: str) -> List[Dict[str, Any]]:
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)


def is_numeric(value: str) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False


def convert_to_number(value: str) -> float:
    try:
        if '.' not in value:
            return float(int(value))
        return float(value)
    except ValueError:
        return 0.0


def calculate_statistics(data: List[Dict[str, Any]], column: str) -> Dict[str, float]:
    if not data:
        return {"avg": 0, "min": 0, "max": 0, "count": 0}

    if column not in data[0]:
        print(f"Error: Column '{column}' not found.")
        print("Available columns:", ", ".join(data[0].keys()))
        sys.exit(1)

    numerical_values = []

    for row in data:
        value = row[column].strip()
        if is_numeric(value):
            numerical_values.append(convert_to_number(value))

    if not numerical_values:
        print(f"No numerical values found in column '{column}'")
        sys.exit(1)

    avg_value = sum(numerical_values) / len(numerical_values)

    return {
        "avg": round(avg_value, 2),
        "min": min(numerical_values),
        "max": max(numerical_values),
        "count": len(numerical_values)
    }


def filter_rows(data: List[Dict[str, Any]], filter_column: str, filter_value: str):
    if filter_column not in data[0]:
        print(f"Filter column '{filter_column}' not found.")
        sys.exit(1)

    return [
        row for row in data
        if row[filter_column].strip().lower() == filter_value.lower()
    ]


def create_argument_parser():
    parser = argparse.ArgumentParser(
        description="CSV Parser - Analyze CSV files from command line"
    )

    parser.add_argument("filename", help="CSV file path")

    parser.add_argument(
        "--column", "-c",
        required=True,
        help="Column name for statistics"
    )

    parser.add_argument(
        "--filter", "-f",
        nargs=2,
        metavar=("COLUMN", "VALUE"),
        help="Filter rows by column value"
    )

    parser.add_argument(
        "--show-data", "-s",
        action="store_true",
        help="Display filtered rows"
    )

    return parser


def main():
    parser = create_argument_parser()
    args = parser.parse_args()

    print(f"Reading file: {args.filename}")
    data = read_csv_file(args.filename)

    if args.filter:
        filter_column, filter_value = args.filter
        data = filter_rows(data, filter_column, filter_value)

        if args.show_data:
            print("\nFiltered Data:")
            for row in data:
                print(row)

        if not data:
            print("No data after filtering.")
            sys.exit(1)

    stats = calculate_statistics(data, args.column)

    print("\nStatistics:")
    print(f"Average: {stats['avg']}")
    print(f"Minimum: {stats['min']}")
    print(f"Maximum: {stats['max']}")
    print(f"Count: {stats['count']}")


if __name__ == "__main__":
    main()
