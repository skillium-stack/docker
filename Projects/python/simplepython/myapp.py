import os

# Prompt the user for a name
name = input("Enter a name: ")

# Define the path to the file
file_path = 'simplepython/servers.txt'

# Ensure the directory exists
os.makedirs(os.path.dirname(file_path), exist_ok=True)

try:
    # Open the file in append mode ('a') so it creates the file if it doesn't exist
    with open(file_path, 'a+') as file:
        # Write the name to the file
        file.write(name + '\n')
        # Move the pointer to the beginning of the file
        file.seek(0)
        # Read all the lines in the file
        content = file.readlines()
except Exception as e:
    print(e, type(e))
else:
    # Print each line from the file
    for line in content:
        print(f'{line.rstrip()}')


