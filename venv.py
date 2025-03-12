import os
import sys
import platform

def get_venv_base():
    """Zwraca ścieżkę do katalogu z środowiskami wirtualnymi."""
    return os.path.join(os.path.expanduser("/home/tomasz/Documents/"), "venvs")

def list_venvs():
    """Wyświetla listę dostępnych środowisk wirtualnych."""
    venv_base = get_venv_base()
    
    if not os.path.exists(venv_base):
        print(f"Błąd: Katalog ze środowiskami wirtualnymi nie istnieje: {venv_base}")
        return None
    
    venvs = [d for d in os.listdir(venv_base) 
             if os.path.isdir(os.path.join(venv_base, d))]
    
    if not venvs:
        print("Nie znaleziono żadnych środowisk wirtualnych.")
        return None
    
    print("\nDostępne środowiska wirtualne:")
    for i, venv in enumerate(venvs, 1):
        print(f"{i}. {venv}")
    
    return venvs

def activate_venv(venv_name):
    """Aktywuje wybrane środowisko wirtualne."""
    
    # Sprawdź system operacyjny
    is_windows = platform.system().lower() == "windows"
    
    # Ścieżka do katalogu ze środowiskami wirtualnymi
    venv_base = get_venv_base()
    
    # Pełna ścieżka do wybranego środowiska
    venv_path = os.path.join(venv_base, venv_name)
    
    if not os.path.exists(venv_path):
        print(f"Błąd: Środowisko '{venv_name}' nie istnieje w {venv_base}")
        sys.exit(1)
    
    # Ścieżka do skryptu aktywacyjnego
    if is_windows:
        activate_script = os.path.join(venv_path, "Scripts", "activate.bat")
    else:
        activate_script = os.path.join(venv_path, "bin", "activate")
    
    if not os.path.exists(activate_script):
        print(f"Błąd: Nie znaleziono skryptu aktywacyjnego w {activate_script}")
        sys.exit(1)
    
    # Generuj komendę do wykonania
    if is_windows:
        command = f"call {activate_script}"
    else:
        command = f"source {activate_script}"
    
    # Wyświetl instrukcję dla użytkownika
    print(f"\nAby aktywować środowisko '{venv_name}', wykonaj następującą komendę:")
    print(f"\n{command}\n")

def main():
    if len(sys.argv) < 2:
        print("Użycie: python nazwa.py [list|switch]")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "list":
        list_venvs()
    elif command == "switch":
        venvs = list_venvs()
        if not venvs:
            sys.exit(1)
        
        try:
            choice = input("\nWybierz numer środowiska do aktywacji: ")
            venv_index = int(choice) - 1
            if 0 <= venv_index < len(venvs):
                activate_venv(venvs[venv_index])
            else:
                print("Nieprawidłowy numer środowiska.")
                sys.exit(1)
        except ValueError:
            print("Proszę podać prawidłowy numer.")
            sys.exit(1)
    else:
        print("Nieznana komenda. Użyj 'list' lub 'switch'")
        sys.exit(1)

if __name__ == "__main__":
    main()
