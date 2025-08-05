def modify_content(content):
    return content.upper()  

def read_and_modify_file():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, 'r') as file:
            original_content = file.read()
            print("File read successfully!")

            modified_content = modify_content(original_content)

            output_filename = f"modified_{filename}"
            with open(output_filename, 'w') as output_file:
                output_file.write(modified_content)
                print(f"Modified content written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")

read_and_modify_file()
