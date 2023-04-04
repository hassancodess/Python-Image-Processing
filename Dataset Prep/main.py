import os
import pandas as pd
from PIL import Image
import numpy as np

# Set the directory path
directory = 'data/'

# Create an empty list to hold the data
data = []

# Loop through each directory in the data directory
for subdir in os.listdir(directory):

    # Get the full path of the subdirectory`
    subdir_path = os.path.join(directory, subdir)

    # Only process directories
    if os.path.isdir(subdir_path):

        # Loop through each file in the subdirectory
        for file in os.listdir(subdir_path):

            # Get the full path of the file
            file_path = os.path.join(subdir_path, file)

            # Only process image files
            if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
                np_img = np.array(Image.open(file_path))
                img_flatten = np_img.flatten()
                reshape = img_flatten.reshape(1, img_flatten.shape[0])
                data.append({'Folder': subdir, 'Image': reshape})

# Convert the data list to a pandas DataFrame
df = pd.DataFrame(data)

# Write the DataFrame to a CSV file
df.to_csv('output.csv', index=False)

