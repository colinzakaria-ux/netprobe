#!/usr/bin/env python3
import argparse
import sys

def main(args=None):
    parser=argparse.ArgumentParser(description="Processes a File")
    parser.add_argument('filename', help='Name of file to be processed')

    parsed_args=parser.parse_args(args)
    print(f"--- Attempting to read: {parsed_args.filename} ---")
    try:
        with open(parsed_args.filename, 'r') as f:
            content=f.read()

            print("--- File Contents Start ---")
            print(content)
            print("--- File Contents End ---")

    except FileNotFoundError:
        print(f"Error: Could not find the file named '{parsed_args.filename}")
        sys.exit(1)

if __name__ == "__main__":
    main()







