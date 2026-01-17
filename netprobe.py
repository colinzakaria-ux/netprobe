#!/usr/bin/env python3
import subprocess
import argparse
import sys

def connectivity(target_ip, count):
    """
    Pings a target IP a specific number of times.
    Returns True if successful, False otherwise.
    """
    # Dynamic timeout: 1.5s per ping + 2s buffer overhead
    timeout_limit = (count * 1.5) + 2

    try:
        result = subprocess.run(
            ["ping", "-c", str(count), target_ip],
            capture_output=True,
            text=True,
            timeout=timeout_limit
        )

    except subprocess.TimeoutExpired:
        print(f"Ping to {target_ip} timed out.")
        return False

    if result.returncode == 0:
        print(f"Ping to {target_ip} successful.")
        return True
    else:
        print(f"Ping to {target_ip} failed.")
        if result.stderr:
            print(f"Error: {result.stderr.strip()}")
        return False

def main():
    parser = argparse.ArgumentParser(description="NetProbe - Network Connectivity Tester")
    parser.add_argument("target", help="The IP address or hostname to ping")
    parser.add_argument("-c", "--count", type=int, default=1, help="Number of pings (default: 1)")
    
    args = parser.parse_args()

    print(f"Pinging {args.target} {args.count} times...")

    try:
        success = connectivity(args.target, args.count)
        if not success:
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()
