#!/usr/bin/env python3

import sys
import subprocess
import argparse


"""
Next Step: Try to write a script from memory (no docs!) that uses subprocess to list
the files in your current directory (ls -l), captures that output, and then uses 
enumerate() to print a numbered list of those files to the console.
"""

def list_dir(path_to_directory)->bool:
    result=subprocess.run(
        ["ls", "-la", path_to_directory],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"Failed to open {path_to_directory}")
        print(f"Error: {result.stderr.strip()}")
        return False
    
    lines = result.stdout.splitlines()
    for index, line in enumerate(lines):
        print(f"{index}: {line}")

    return True

def main():
    parser = argparse.ArgumentParser(description="List files in a directory")
    parser.add_argument(
        "path_to_directory",
        type=str,
        help="Enter: /path/to/dir"
    )
  
    args = parser.parse_args()
    success=list_dir(args.path_to_directory)
    if not success:
        sys.exit(1)

if __name__== "__main__":
    main()
