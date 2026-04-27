def display_message():
    print("This is a utility function.")

if __name__ == "__main__":
    # This block ONLY runs if you run utility.py directly.
    # It will NOT run if you import utility.py elsewhere.
    print("Running utility script directly for testing...")
    display_message()

# Now try importing it
import utility
utility.display_message()
# Notice that the "Running utility script..." message did NOT appear.
