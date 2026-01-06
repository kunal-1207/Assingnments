"""
Write to a File

Write a program to create a text file and write some content to it.

Using file functions like write and open.
"""

def write_to_file():
    """
    Function to create a text file and write content to it
    """
    filename = input("Enter the filename (with .txt extension): ")
    
    # Get content to write to the file
    print("Enter the content to write to the file (type 'END' on a new line to finish):")
    content_lines = []
    
    while True:
        line = input()
        if line == "END":
            break
        content_lines.append(line)
    
    # Join all lines with newline characters
    content = "\n".join(content_lines)
    
    try:
        # Open file in write mode
        with open(filename, 'w') as file:
            file.write(content)
        
        print(f"Content successfully written to {filename}")
        
        # Verify by reading the file back
        print("\nVerifying the content written:")
        with open(filename, 'r') as file:
            written_content = file.read()
            print(written_content)
            
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def main():
    """
    Main function to run the write to file program
    """
    print("--- Write to File Program ---")
    write_to_file()

if __name__ == "__main__":
    main()