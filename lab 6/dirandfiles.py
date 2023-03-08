##task 1
import os

# Path to the directory you want to list
path = '/path/to/directory'

# List only directories
print("List of directories:")
for dir in os.listdir(path):
    if os.path.isdir(os.path.join(path, dir)):
        print(dir)

# List only files
print("\nList of files:")
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)):
        print(file)

# List all directories and files
print("\nList of directories and files:")
for item in os.listdir(path):
    print(item)

##Task 2

# Path to the directory or file you want to test
path = '/path/to/directory_or_file'

# Test existence
if os.path.exists(path):
    print("Path exists")
else:
    print("Path does not exist")

# Test readability
if os.access(path, os.R_OK):
    print("Path is readable")
else:
    print("Path is not readable")

# Test writability
if os.access(path, os.W_OK):
    print("Path is writable")
else:
    print("Path is not writable")

# Test executability
if os.access(path, os.X_OK):
    print("Path is executable")
else:
    print("Path is not executable")

##Task 3
# Path to the file or directory you want to test
path = '/path/to/file_or_directory'

# Test existence
if os.path.exists(path):
    print("Path exists")

    # Find the filename and directory portion of the given path
    filename = os.path.basename(path)
    directory = os.path.dirname(path)
    print("Filename:", filename)
    print("Directory:", directory)

else:
    print("Path does not exist")
##Task 4
# Path to the text file you want to count the lines of
path = '/path/to/text_file'

# Open the file in read mode
with open(path, 'r') as file:
    # Initialize a variable to keep track of the number of lines
    count = 0
    # Loop through each line in the file
    for line in file:
        # Increment the count variable for each line
        count += 1

# Output the number of lines in the file
print("Number of lines:", count)

##Task 5
# List to write to file
my_list = [1, 2, 3, 4, 5]

# Path to the file to write the list to
path = '/path/to/output/file.txt'

# Open the file in write mode
with open(path, 'w') as file:
    # Write each element of the list to a new line in the file
    for element in my_list:
        file.write(str(element) + '\n')

##Task 6
import string

# Path to the directory to create the files in
directory = '/path/to/directory'

# Loop through each letter of the alphabet
for letter in string.ascii_uppercase:
    # Generate the filename
    filename = directory + '/' + letter + '.txt'
    # Open the file in write mode and close it immediately to create it
    with open(filename, 'w'):
        pass

##Task 7
# Path to the source file
source_file = '/path/to/source/file.txt'

# Path to the destination file
destination_file = '/path/to/destination/file.txt'

# Open the source file in read mode
with open(source_file, 'r') as source:
    # Open the destination file in write mode
    with open(destination_file, 'w') as destination:
        # Read the contents of the source file and write them to the destination file
        contents = source.read()
        destination.write(contents)

##Task 8
import os

# Path to the file to delete
file_path = '/path/to/file.txt'

# Check if the file exists
if not os.path.exists(file_path):
    print('File does not exist')
else:
    # Check if the file is accessible
    if not os.access(file_path, os.W_OK):
        print('File is not writable')
    else:
        # Delete the file
        os.remove(file_path)
        print('File deleted successfully')
