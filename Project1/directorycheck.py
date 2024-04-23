import os

# Get the current working directory
current_dir = os.getcwd()

# Print the current working directory
print("Current working directory:", current_dir)

# List the files in the current working directory to find the HTML file
files_in_dir = os.listdir(current_dir)
print("Files in the current directory:", files_in_dir)
