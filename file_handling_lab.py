# File Read & Write Challenge + Error Handling Lab

def read_file(filename):
    """Reads the contents of a file and returns it."""
    with open(filename, "r") as file:
        content = file.read()
    return content


def modify_content(content):
    """Modifies the content of the file (example: converts to uppercase)."""
    return content.upper()


def write_file(new_filename, content):
    """Writes the modified content to a new file."""
    with open(new_filename, "w") as file:
        file.write(content)


def main():
    try:
        # Ask the user for a file name
        filename = input("Enter the name of the file to read: ")

        # Step 1: Read the file
        content = read_file(filename)

        # Step 2: Modify the content
        modified_content = modify_content(content)

        # Step 3: Write to a new file
        new_filename = "modified_" + filename
        write_file(new_filename, modified_content)

        # Step 4: Confirm success
        print(f"✅ File processed successfully! Modified file saved as: {new_filename}")

    except FileNotFoundError:
        print("❌ Error: The file you entered does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read or write this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# Run the program
if __name__ == "__main__":
    main()
