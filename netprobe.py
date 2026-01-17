#!/usr/bin/env python3
import subprocess
import argparse
import sys

# UPDATE 1: Add 'count' as a parameter
def connectivity(target_ip, count):
    # If count is 10, timeout becomes 17 seconds.
    dynamic_timeout = (count * 1.5) + 2
    
    try:
        # UPDATE 2: Use str(count) in the command list
        result=subprocess.run(
            ["ping", "-c", str(count), target_ip],
            capture_output=True,
            text=True,
            timeout=dynamic_timeout
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
    # 1. Initialize the Parser
    # This creates the object that handles the logic
    parser = argparse.ArgumentParser(description="Network Connectivity Tester")

    # 2. Add the Target Argument (Positional)
    # Because there are no dashes (-), this is required.
    parser.add_argument("target", help="The IP address to ping")

    # 3. Add the Count Argument (Optional)
    # We add '-c' and '--count' so the user can use either.
    # type=int: Ensures the script crashes nicely if the user types "five" instead of "5"
    # default=1: If the user ignores this flag, we just ping once.
    parser.add_argument("-c", "--count", type=int, default=1, help="Number of pings (default: 1)")

    # 4. Parse the Arguments
    # This checks what the user typed in the terminal against the rules above.
    args = parser.parse_args()

    # 5. Pass the data to your function
    # args.target holds the IP ("8.8.8.8")
    # args.count holds the number (5)
    print(f"Pinging {args.target} {args.count} times...")
    connectivity(args.target, args.count)

if __name__=="__main__":
    main()
