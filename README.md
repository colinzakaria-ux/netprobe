# NetProbe

NetProbe is a lightweight, robust command-line interface tool for testing network connectivity. Built with Python, it improves upon standard ping commands by handling timeouts gracefully, providing clear exit codes for automation, and offering a user-friendly argument interface.

## Features
- **Dynamic Timeouts:** Automatically scales the timeout limit based on the number of pings.
- **Error Handling:** Catches system errors and provides clean, readable output instead of traceback crashes.
- **Automation Ready:** Returns proper system exit codes (0 for success, 1 for failure), making it suitable for use in shell scripts or CI/CD pipelines.
- **Graceful Exit:** Handles `CTRL+C` interruptions cleanly without Python errors.

## Installation

No installation is required. Just ensure you have Python 3 installed.

```bash
git clone [https://github.com/your-username/netprobe.git](https://github.com/your-username/netprobe.git)
cd netprobe
chmod +x netprobe.py
``` 

## Usage

Run the script directly from the terminal.

### Basic Ping (Default: 1 count)

`./netorobe.py 8.8.8.8`

### Custom ping count
Ping a target 5 times:

`./netprobe.py -c 5 8.8.8.8 `

### Help argument

`./netprobe.py --help`

## Requirements

- Python 3.6+
- Linux/macOS 

## License

MIT

```

