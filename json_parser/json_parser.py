#!/usr/bin/python3
import json
import sys

def print_usage():
    print("Usage: ./json_parser.py <json_file>")
    sys.exit(1)

def json_parser(json_file):
    try:
        with open(json_file) as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Invalid JSON format")
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print_usage()
    else:
        json_file = sys.argv[1]
        data = json_parser(json_file)
        print(data)
