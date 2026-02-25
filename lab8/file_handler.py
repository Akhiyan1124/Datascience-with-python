def read_file_with_exceptions(filename):
    file = None
    try:
        print(f"Opening file: {filename}")
        file = open(filename, 'r')
        content = file.read()
        print("File read successfully.")
        return content

    except FileNotFoundError:
        print("Error: File not found.")
        return None

    except PermissionError:
        print("Error: Permission denied.")
        return None

    except IOError as e:
        print(f"I/O Error: {e}")
        return None

    finally:
        if file and not file.closed:
            file.close()
            print("File closed properly.")


if __name__ == "__main__":
    read_file_with_exceptions("file_handler.py")
    read_file_with_exceptions("missing.txt")
