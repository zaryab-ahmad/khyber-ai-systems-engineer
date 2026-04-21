def clean_string(text):
    return text.strip().lower()

if __name__ == "__main__":
    print(f"Test: {clean_string('  Python Pro  ')}")

# Main Script Usage
import data_utils

raw_data = ["  Data ", " SCIENCE  ", "  ai "]
cleaned_data = [data_utils.clean_string(item) for item in raw_data]

print(f"Final Dataset: {cleaned_data}")
