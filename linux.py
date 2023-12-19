import subprocess
import sys

VERSION = "v0.1.0"


def display_manual():
    print("internsctl(1) - Custom Linux Command")
    print()
    print("NAME")
    print("    internsctl - Perform various operations using a custom Linux command")
    print()
    print("SYNOPSIS")
    print("    internsctl [COMMAND] [OPTIONS]")
    print()
    print("DESCRIPTION")
    print("    Custom Linux command for performing server operations.")
    
def display_help():
    print("Usage: internsctl [COMMAND] [OPTIONS]")
    print()
    print("Commands:")
    print("    cpu getinfo         Get CPU information")
    print("    memory getinfo      Get memory information")
    print("    user create         Create a new user")
    print("    user list           List all regular users")
    print("    user list --sudo-only  List users with sudo permissions")
    print("    file getinfo        Get information about a file")
    print()
    print("Options:")
    print("    --version           Display version information")
    print("    --help              Display this help message")

def display_version():
    print(f"internsctl {VERSION}")

def get_cpu_info():
    result = subprocess.run(["systeminfo"], capture_output=True, text=True)
    print(result.stdout)

def get_memory_info():
    result = subprocess.run(["systeminfo"], capture_output=True, text=True)
    print(result.stdout)

def create_user(username):
    subprocess.run(["net", "user", username, "/add"])
    print(f"User '{username}' created successfully.")


def list_users_windows():
    result = subprocess.run(["net", "user"], capture_output=True, text=True)
    users = [line.strip() for line in result.stdout.splitlines() if line.strip() and line.strip() != "The command completed successfully."]
    print("Regular Users:")
    print("\n".join(users))

def list_sudo_users_windows():
    result = subprocess.run(["net", "localgroup", "Administrators"], capture_output=True, text=True)
    sudo_users = [line.split(" ")[-1] for line in result.stdout.splitlines() if line.strip()]
    print("Users with sudo permissions:")
    print("\n".join(sudo_users))

if len(sys.argv) > 1:
    if sys.argv[1] == "--help":
        display_help()
    elif sys.argv[1] == "--version":
        display_version()
    elif sys.argv[1] == "cpu" and sys.argv[2] == "getinfo":
        get_cpu_info()
    elif sys.argv[1] == "memory" and sys.argv[2] == "getinfo":
        get_memory_info()
    elif sys.argv[1] == "user" and sys.argv[2] == "create" and len(sys.argv) == 4:
        create_user(sys.argv[3])
    elif sys.argv[1] == "user" and sys.argv[2] == "list":
        list_users_windows()
    elif sys.argv[1] == "user" and len(sys.argv) > 3 and sys.argv[3] == "--sudo-only":
        list_sudo_users_windows()
    else:
        print("Invalid command or options. Use: internsctl --help or internsctl --version")
else:
    display_manual()
