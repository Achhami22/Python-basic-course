# write a python program to print the contents of directory using os module
import os

# Specify the directory you want to list
directory = './'  # Current directory. You can change this to any path like 'C:/Users/YourName/Documents'

try:
    # List all files and directories in the specified path
    contents = os.listdir(directory)
    print(f"Contents of '{directory}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory}' does not exist.")
except PermissionError:
    print(f"You do not have permission to access '{directory}'.")
