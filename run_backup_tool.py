#!/usr/bin/env python3
import argparse

def run_backup_tool():
    # Initialize
    parser = argparse.ArgumentParser(description="Back up a specific file to a folder.")

    # --- Arguments --- 
     
    # 1. The file we want to backup (Positional/Required)
    parser.add_argument("filename", type=str, help="The path to the file you want to backup.")

    # 2. Where to put it (Optional with a default value)
    # If the user doesn't specify --dest, it uses '/tmp'
    parser.add_argument("--dest", type=str, default="/tmp", help="The destination folder")

    # 3. Verbose mode (Optional flag)
    # '-v' is a short version, '--verbose' is the long version
    parser.add_argument("-v", "--verbose", action="store_true", help="Enabled detailed logging.")

    # --- Processing --- 
    args = parser.parse_args()

    if args.verbose:
        print("--- Starting Automation ---")
        print(f"Target File: {args.filename}")
        print(f"destination: {args.dest}")

    print(f"Backing up '{args.filename} to '{args.dest}'...")

    if args.verbose:
        print("--- Backup Complete ---")

if __name__ == "__main__":
    run_backup_tool()


