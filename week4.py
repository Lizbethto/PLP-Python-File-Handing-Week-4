# File Read & Write with Error Handling

try:
    # Ask the user for the input filename
    input_file = input("Enter the name of the file to read: ")

    # Try to open and read the file
    with open(input_file, "r") as infile:
        content = infile.readlines()

    # Modify the content (example: add line numbers)
    modified_content = ""
    for index, line in enumerate(content, start=1):
        modified_content += f"{index}: {line}"

    # Ask for the output filename
    output_file = input("Enter the name of the new file to write: ")

    # Write the modified content to the new file
    with open(output_file, "w") as outfile:
        outfile.write(modified_content)

    print(f"✅ File has been read and modified content written to '{output_file}'")

except FileNotFoundError:
    print("❌ Error: The file you tried to read does not exist.")
except PermissionError:
    print("❌ Error: You don’t have permission to access this file.")

