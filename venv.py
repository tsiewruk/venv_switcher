import os
import sys
import platform
import shutil

def get_venv_base():
    """Returns the path to the virtual environments directory."""
    return os.path.join(os.path.expanduser("/home/tomasz/Documents/"), "venvs")

def list_venvs():
    """Displays a list of available virtual environments."""
    venv_base = get_venv_base()
    
    if not os.path.exists(venv_base):
        print(f"Error: Virtual environments directory does not exist: {venv_base}")
        return None
    
    venvs = [d for d in os.listdir(venv_base) 
             if os.path.isdir(os.path.join(venv_base, d))]
    
    if not venvs:
        print("No virtual environments found.")
        return None
    
    print("\nAvailable virtual environments:")
    for i, venv in enumerate(venvs, 1):
        print(f"{i}. {venv}")
    
    return venvs

def remove_venv(venv_name):
    """Removes the selected virtual environment."""
    venv_base = get_venv_base()
    venv_path = os.path.join(venv_base, venv_name)
    
    if not os.path.exists(venv_path):
        print(f"Error: Environment '{venv_name}' does not exist in {venv_base}")
        return False
    
    try:
        # User confirmation
        confirm = input(f"\nAre you sure you want to remove environment '{venv_name}'? (yes/no): ")
        if confirm.lower() != 'yes':
            print("Environment removal cancelled.")
            return False
        
        # Remove environment directory
        shutil.rmtree(venv_path)
        print(f"\nEnvironment '{venv_name}' has been removed.")
        return True
    except Exception as e:
        print(f"Error while removing environment: {str(e)}")
        return False

def activate_venv(venv_name):
    """Activates the selected virtual environment."""
    
    # Check operating system
    is_windows = platform.system().lower() == "windows"
    
    # Path to virtual environments directory
    venv_base = get_venv_base()
    
    # Full path to selected environment
    venv_path = os.path.join(venv_base, venv_name)
    
    if not os.path.exists(venv_path):
        print(f"Error: Environment '{venv_name}' does not exist in {venv_base}")
        sys.exit(1)
    
    # Path to activation script
    if is_windows:
        activate_script = os.path.join(venv_path, "Scripts", "activate.bat")
    else:
        activate_script = os.path.join(venv_path, "bin", "activate")
    
    if not os.path.exists(activate_script):
        print(f"Error: Activation script not found at {activate_script}")
        sys.exit(1)
    
    # Generate command to execute
    if is_windows:
        command = f"call {activate_script}"
    else:
        command = f"source {activate_script}"
    
    # Display instructions for user
    print(f"\nTo activate environment '{venv_name}', execute the following command:")
    print(f"\n{command}\n")

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py [list|switch|remove]")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "list":
        list_venvs()
    elif command == "switch":
        venvs = list_venvs()
        if not venvs:
            sys.exit(1)
        
        try:
            choice = input("\nSelect environment number to activate: ")
            venv_index = int(choice) - 1
            if 0 <= venv_index < len(venvs):
                activate_venv(venvs[venv_index])
            else:
                print("Invalid environment number.")
                sys.exit(1)
        except ValueError:
            print("Please enter a valid number.")
            sys.exit(1)
    elif command == "remove":
        venvs = list_venvs()
        if not venvs:
            sys.exit(1)
        
        try:
            choice = input("\nSelect environment number to remove: ")
            venv_index = int(choice) - 1
            if 0 <= venv_index < len(venvs):
                remove_venv(venvs[venv_index])
            else:
                print("Invalid environment number.")
                sys.exit(1)
        except ValueError:
            print("Please enter a valid number.")
            sys.exit(1)
    else:
        print("Unknown command. Use 'list', 'switch' or 'remove'")
        sys.exit(1)

if __name__ == "__main__":
    main()
