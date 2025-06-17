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

1. Download the `venv_switcher` script
2. Place it in a directory of your choice
3. Make it executable: `chmod +x venv_switcher`
4. (Optional) Add the directory to your PATH for easier access

You can then run the script either as:
- `./venv_switcher command` (direct execution)
- `python3 venv_switcher command` (through Python interpreter)

## Configuration

By default, virtual environments are stored in `~/venvs`. You can change this location using the configuration command:

```bash
python venv_switcher --configure
```

Configuration files are stored in:
- Unix-based systems: `~/.venv_switcher.cfg`
- Windows: `%LOCALAPPDATA%\venv_switcher\config.cfg`

## Usage

### List Available Environments

To see all available virtual environments:

```bash
./venv_switcher list
# or
python3 venv_switcher list
```

### Create New Environment

To create a new virtual environment:

```bash
./venv_switcher create
```

This will:
1. Prompt you for the name of the new environment
2. Create the environment with pip support
3. Ask if you want to activate it immediately
4. If you choose "yes", automatically activate the new environment in a new shell

### Switch Environment

To activate a different virtual environment:

```bash
./venv_switcher switch
```

This will:
1. Show a list of available environments
2. Prompt you to select an environment by number (or 'x' to cancel)
3. Automatically activate the selected environment in a new shell
4. To deactivate, simply type `exit` or press Ctrl+D to return to the previous shell

### Remove Environment

To remove a virtual environment:

```bash
./venv_switcher remove
```

This will:
1. Show a list of available environments
2. Prompt you to select an environment to remove (or 'x' to cancel)
3. Ask for confirmation before deletion

### Configure Storage Location

To change where virtual environments are stored:

```bash
./venv_switcher --configure
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

- The tool automatically activates environments by starting a new shell with the virtual environment already active.
- To deactivate an environment, simply type `exit` or press Ctrl+D to return to the previous shell.
- All operations are confirmed before execution to prevent accidental deletions.
- The configuration is stored in JSON format for easy editing if needed.
- You can cancel any selection prompt by entering 'x'
- New environments are created with pip support by default

## Contributing

Feel free to submit issues and enhancement requests!
