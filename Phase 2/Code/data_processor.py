import argparse

def main():
    parser = argparse.ArgumentParser(description="KASE Industrial Data Processor")
    
    # 1. Add a positional (required) argument
    parser.add_argument("filename", help="The name of the file to process")
    
    # 2. Add an optional flag
    parser.add_argument("--secret", action="store_true", help="Enable secret processing mode")

    args = parser.parse_args()

    print(f"--- Processing: {args.filename} ---")
    if args.secret:
        print("!! SECRET MODE ACTIVATED !!")
    else:
        print("Standard mode active.")

if __name__ == "__main__":
    main()
