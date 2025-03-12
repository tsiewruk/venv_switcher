# Venv Switcher

A command-line tool for managing Python virtual environments. This tool helps you list, switch between, and remove virtual environments from a centralized location.

## Features

- List all available virtual environments
- Switch between virtual environments
- Remove virtual environments
- Configure virtual environments directory location
- Cross-platform support (Windows and Unix-based systems)
- Cancel operations with 'x' input

## Installation

1. Download the `venv.py` script
2. Place it in a directory of your choice
3. (Optional) Add the directory to your PATH for easier access

## Configuration

By default, virtual environments are stored in `~/venvs`. You can change this location using the configuration command:

```bash
python venv.py --configure
```

Configuration files are stored in:
- Unix-based systems: `~/.venv_switcher.cfg`
- Windows: `%LOCALAPPDATA%\venv_switcher\config.cfg`

## Usage

### List Available Environments

To see all available virtual environments:

```bash
python venv.py list
```

### Switch Environment

To activate a different virtual environment:

```bash
python venv.py switch
```

This will:
1. Show a list of available environments
2. Prompt you to select an environment by number (or 'x' to cancel)
3. Provide the command to activate the selected environment

### Remove Environment

To remove a virtual environment:

```bash
python venv.py remove
```

This will:
1. Show a list of available environments
2. Prompt you to select an environment to remove (or 'x' to cancel)
3. Ask for confirmation before deletion

### Configure Storage Location

To change where virtual environments are stored:

```bash
python venv.py --configure
```

This will:
1. Show the current storage location
2. Allow you to enter a new location
3. Create the directory if it doesn't exist (with your permission)

## Command Reference

| Command | Description |
|---------|-------------|
| `list` | Display all available virtual environments |
| `switch` | Switch to a different virtual environment |
| `remove` | Remove a virtual environment |
| `--configure` | Configure the virtual environments directory |

## Error Handling

The tool includes comprehensive error handling for:
- Missing directories
- Invalid environment selections
- Configuration file issues
- Permission problems
- Invalid commands
- Cancelled operations

## System Requirements

- Python 3.x
- Operating System: Windows, Linux, or macOS

## Notes

- The tool cannot directly activate environments due to shell limitations. Instead, it provides the necessary command to activate the environment.
- All operations are confirmed before execution to prevent accidental deletions.
- The configuration is stored in JSON format for easy editing if needed.
- You can cancel any selection prompt by entering 'x'

## Contributing

Feel free to submit issues and enhancement requests!
