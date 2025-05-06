def read_and_modify_file():
    try:
        # Ask user for the filename to read
        input_file = input("Enter the name of the file to read: ")

        with open(input_file, "r") as file:
            content = file.read()

        # Modify the content (for example, make it uppercase)
        modified_content = content.upper()

        # Write to a new file
        output_file = "modified_" + input_file
        with open(output_file, "w") as new_file:
            new_file.write(modified_content)

        print(f"✅ File has been modified and saved as '{output_file}'")

    except FileNotFoundError:
        print("❌ Error: The file was not found.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


