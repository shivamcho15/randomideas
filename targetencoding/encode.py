import sys
import pandas as pd

def print_usage():
    print("Usage: python encode.py <input_file> <output_file> <target_col> [columns_to_skip]")
    print("Example: python encode.py input.csv output.csv isFraud id,date")
    print("")
    sys.exit(1)

def main():
    # If not enough arguments are provided, show usage
    if len(sys.argv) < 4:
        print_usage()

    # Parse arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    target_col = sys.argv[3]
    skip_columns = []

    # Parse optional columns to skip
    if len(sys.argv) == 5:
        skip_columns = [x.strip().upper() for x in sys.argv[4].split(",") if x.strip()]
    print(skip_columns)
    # Read CSV
    df = pd.read_csv(input_file)

    # Ensure target column is boolean
    df[target_col] = df[target_col].astype(bool)

    # Perform target encoding
    for col in df.columns:
        if col == target_col or col.strip().upper() in skip_columns:
            continue
        fraud_ratio = df.groupby(col)[target_col].mean()
        df[col] = df[col].map(fraud_ratio)

    # Save the transformed CSV
    df.to_csv(output_file, index=False)
    print(f"Target encoding completed! Saved to {output_file}")

if __name__ == "__main__":
    main()
