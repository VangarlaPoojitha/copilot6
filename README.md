# copilot6
# Improved Shell Command Execution in Python

This project demonstrates best practices for executing shell commands in Python by:
- Replacing the deprecated `os.popen()` with the more secure and robust `subprocess.run()`
- Encapsulating logic into reusable functions
- Implementing exception handling for robust error management

## Features

- Uses `subprocess.run()` for executing shell commands
- Handles errors gracefully with try-except blocks
- Organizes code into functions for clarity and reusability

## Example Usage

```python
import subprocess

def list_directory(path='.'):
    try:
        result = subprocess.run(['ls', '-l', path], capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

list_directory()
```

## Why Use `subprocess.run()`?

- **Security**: Avoids shell injection vulnerabilities present in older methods
- **Control**: Allows capturing output, error handling, and more process control
- **Future-Proof**: `os.popen()` is deprecated and should be avoided

## Requirements

- Python 3.5 or later

## Running the Program

1. Clone the repository or copy the script.
2. Run the script using:

   ```bash
   python script_name.py
   ```

3. The output will list the contents of the specified directory.

## License

This project is licensed under the MIT License.
# copilot6
