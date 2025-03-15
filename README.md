# Venv Switcher

A command-line tool for managing Python virtual environments. This tool helps you list, create, switch between, and remove virtual environments from a centralized location.

## Features

- List all available virtual environments
- Create new virtual environments
- Switch between virtual environments
- Remove virtual environments
- Configure virtual environments directory location
- Cross-platform support (Windows and Unix-based systems)
- Cancel operations with 'x' input

## Installation

1. Download the `venv_switcher.py` script
2. Place it in a directory of your choice
3. (Optional) Add the directory to your PATH for easier access

## Configuration

By default, virtual environments are stored in `~/venvs`. You can change this location using the configuration command:

```bash
python venv_switcher.py --configure
```

Configuration files are stored in:
- Unix-based systems: `~/.venv_switcher.cfg`
- Windows: `%LOCALAPPDATA%\venv_switcher\config.cfg`

## Usage

### List Available Environments

To see all available virtual environments:

```bash
python venv_switcher.py list
```

### Create New Environment

To create a new virtual environment:

```bash
python venv_switcher.py create
```

This will:
1. Prompt you for the name of the new environment
2. Create the environment with pip support
3. Show the command to activate the new environment

### Switch Environment

To activate a different virtual environment:

```bash
python venv_switcher.py switch
```

This will:
1. Show a list of available environments
2. Prompt you to select an environment by number (or 'x' to cancel)
3. Provide the command to activate the selected environment

### Remove Environment

To remove a virtual environment:

```bash
python venv_switcher.py remove
```

This will:
1. Show a list of available environments
2. Prompt you to select an environment to remove (or 'x' to cancel)
3. Ask for confirmation before deletion

### Configure Storage Location

To change where virtual environments are stored:

```bash
python venv_switcher.py --configure
```

This will:
1. Show the current storage location
2. Allow you to enter a new location
3. Create the directory if it doesn't exist (with your permission)

## Command Reference

| Command | Description |
|---------|-------------|
| `list` | Display all available virtual environments |
| `create` | Create a new virtual environment |
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
- Duplicate environment names
- Failed environment creation

## System Requirements

- Python 3.x
- Operating System: Windows, Linux, or macOS

## Notes

- The tool cannot directly activate environments due to shell limitations. Instead, it provides the necessary command to activate the environment.
- All operations are confirmed before execution to prevent accidental deletions.
- The configuration is stored in JSON format for easy editing if needed.
- You can cancel any selection prompt by entering 'x'
- New environments are created with pip support by default

## Contributing

Feel free to submit issues and enhancement requests!
