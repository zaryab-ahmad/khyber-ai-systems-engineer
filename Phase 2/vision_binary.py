import sys
import time
import argparse

# Simulating an external, compiled program that we cannot modify
parser = argparse.ArgumentParser()
parser.add_argument("--image", required=True, help="Image to process")
parser.add_argument("--fail", action="store_true", help="Simulate a crash")
args = parser.parse_args()

print(f"[VISION TOOL] Loading {args.image} into memory...")
time.sleep(1) # Simulating processing time

if args.fail:
    # Print the error to standard error (stderr)
    print(f"[VISION TOOL] FATAL ERROR: Corrupted image data in {args.image}", file=sys.stderr)
    # Exit with a non-zero code to tell the OS we failed!
    sys.exit(1)
else:
    # Print success to standard output (stdout)
    print(f"[VISION TOOL] SUCCESS: 3 Objects detected in {args.image}")
    # Exit with a 0 to tell the OS everything is fine
    sys.exit(0)
