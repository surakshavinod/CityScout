import pandas as pd

# List of file names, change the path if files are in a different directory
file_names = [f"part-{i:05d}-a2b09254-bf3a-49c3-bb42-0b8cb1f81770-c000.csv" for i in range(67)]
output_file = "merged_output.csv"

# Open the output file in write mode
with open(output_file, "w") as outfile:
    # Write header from the first file
    with open(file_names[0], "r") as first_file:
        outfile.write(first_file.readline())  # Write the header line once

    # Append the rest of the files
    for file_name in file_names:
        with open(file_name, "r") as infile:
            next(infile)  # Skip the header line for each file
            # Write the rest of the lines
            outfile.writelines(infile.readlines())
