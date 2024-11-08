import numpy as np
import cv2
import csv

# Define the amount of rubble scanned
image_nbr = 201

for i in range((image_nbr+1)):

    # Path to save file
    csv_path = f"/Users/mvk/github2/reimagine/00_Scanning/scanned_rubble/csv_files/rubble_{i}.csv"
    # Path to contour
    path = f"/Users/mvk/github2/reimagine/00_Scanning/scanned_rubble/contour_line/contour_{i}.png"
    image = cv2.imread(path)

    # Prepare the image to get the most accurate contour
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    ret, binary_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    contours, hierarchy = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Get the contour and reshape it to simplify the data
    largest_contour = max(contours, key=cv2.contourArea)
    contour_points = largest_contour.reshape(-1, 2)  # Shape: (N, 2)

    # Save as csv file
    with open(csv_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for point in contour_points:
            x, y = point
            csv_writer.writerow([x, y])
        print("successfully saved rubble number ", i, " as a csv file")