import os
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import cv2
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
                img = cv2.imread(file_path)
                flatten_img = img.flatten()
                np_img = np.array(flatten_img)
                # reshape = img_flatten.reshape(1, img_flatten.shape[0])
                # csv_string = ','.join([str(x) for x in flatten_img])
                data.append({'Folder': subdir, 'Image': flatten_img})

# Convert the data list to a pandas DataFrame
df = pd.DataFrame(data)

# Write the DataFrame to a CSV file
df.to_csv('output.csv', index=False)

