"""
Read from a File

We used open in read mode and file.read to read and print to display.

Using file functions like open in read mode and file.read
"""

def read_from_file():
    """
    Function to read content from a text file and display it
    """
    filename = input("Enter the filename to read (with .txt extension): ")
    
    try:
        # Open file in read mode
        with open(filename, 'r') as file:
            content = file.read()
        
        print(f"\nContent from {filename}:")
        print("-" * 30)
        print(content)
        print("-" * 30)
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def main():
    """
    Main function to run the read from file program
    """
    print("--- Read from File Program ---")
    read_from_file()

if __name__ == "__main__":
    main()