import argparse
import os

def main():
    # 1. Initialize the Argument Parser
    parser = argparse.ArgumentParser(
        description="A professional CLI tool for scanning and sorting dataset directories.",
        epilog="Example usage: python agile_tool.py --dir ./dataset --sort size"
    )

    # 2. Add the arguments we want to accept from the terminal
    parser.add_argument(
        "--dir", 
        type=str, 
        required=True, 
        help="The target directory containing the dataset you want to process."
    )
    
    parser.add_argument(
        "--sort", 
        type=str, 
        choices=['name', 'size', 'date'], 
        default='name',
        help="How to sort the output (default: name)."
    )
    
    parser.add_argument(
        "--verbose", 
        action="store_true", 
        help="Enable detailed logging output for debugging."
    )

    # 3. Parse the arguments provided by the user
    args = parser.parse_args()

    # 4. Use the parsed arguments in our logic
    if args.verbose:
        print("[DEBUG] Verbose mode activated. Starting deep system scan...\n")
        
    print(f"Target Directory : {args.dir}")
    print(f"Sorting Method   : {args.sort.upper()}")
    
    # Simulate processing the directory
    if not os.path.exists(args.dir):
        print(f"\n[ERROR] The directory '{args.dir}' does not exist. Please check your path.")
    else:
        print("\n[SUCCESS] Directory located. Processing completed.")

if __name__ == "__main__":
    main()
