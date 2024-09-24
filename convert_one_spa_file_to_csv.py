import spectrochempy as scp
import pandas as pd
import numpy as np

# Define file paths
spa_file_path = r'file.spa' # In
csv_file_path = r'file.csv' # Out

# Read the SPA file
dataset = scp.read(spa_file_path)
data = dataset.data.T

# Create a DataFrame from the dataset
df = pd.DataFrame(data, columns=dataset.x_labels)

# Define the initial wavenumbers array (6950 values)
wavenumbers = np.linspace(4000.1885, 649.9040, 6950)

# Check if wavenumbers length is shorter than DataFrame length and pad if necessary (This was necessary for the SPA files from the IR in my lab)
if len(wavenumbers) < len(df):
    wavenumbers = np.pad(wavenumbers, (0, len(df) - len(wavenumbers)), 'edge')

# Insert the wavenumbers as a new column into the DataFrame
df.insert(0, 'Wavenumber', wavenumbers)

# Save the DataFrame to a CSV file
df.to_csv(csv_file_path, index=False, header=False)

#Final Confirmation
print(f"CSV file saved successfully to {csv_file_path}")
