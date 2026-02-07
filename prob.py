import os

def list_directory_contents(path='.'):
    try:
        contents = os.listdir(path)
        print(f"Contents of directory '{path}':")
        for item in contents:
            print(item)
    except Exception as e:
        print(f"Error: {e}")

# Example usage
list_directory_contents('/path/to/your/directory')