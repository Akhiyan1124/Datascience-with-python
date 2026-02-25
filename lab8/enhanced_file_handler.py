def read_file_with_context_manager(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Read {len(content)} characters")
            return content

    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    read_file_with_context_manager("enhanced_file_handler.py")
    read_file_with_context_manager("missing.txt")
