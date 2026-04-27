import sys

print("--- Python Pipe Reader Active ---")

# sys.stdin reads data being 'piped' from the terminal
for line in sys.stdin:
    # We clean the line and process it
    clean_line = line.strip().upper()
    print(f"Processed: {clean_line}")

print("--- End of Stream ---")
