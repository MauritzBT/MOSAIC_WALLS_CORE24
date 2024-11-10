# MOSAIC_WALLS_CORE24
This repository contains the codes for the Mosaic Walls project of the CORE 2024 course at TU Delft.

Please look at the video Mosaic_Walls_Video_Code, which shows you step by step how to run the code. 

The code should be run in the following way: 

in GitHub:
- (import the rubble photos into scanned_rubble/scans) these files are already provided
- install all packages with the requirements.txt file
- update the file paths and inputs in the scanned_rubble_to_image.py code and run it
    - the code will save the following images:
        - a black shape of each stone on a white background
        - a red contour of each stone on top of the original image
        - a red contour of each stone on a white background (for further processing)
- update the file path for the scanned_rubble_to_csv.py code
    - the code will use the red contour images to save each contour in a csv file
        - it saves the pixel positions in x and y from the photo
        - the photo is scaled to the size of the backdrop of the photo *10. this ensures that the pixels correspond to real-life geometry

in Grasshopper (further instructions can be found in the gh file):
- open the grasshopper file 00_FINALCODE.gh in the grasshopper_files folder
- open the stone_input component and update the path to the csv files
- due to the translation of a 3D object into a 2D file, the contour is distorted
- the gh code fixes this distortion with an input for the stone thickness and the camera height
- connect the stone input to ?????
- run the tessellation part of the code
- run the packing part of the code