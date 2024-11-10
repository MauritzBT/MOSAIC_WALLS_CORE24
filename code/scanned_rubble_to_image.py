import cv2
import numpy as np

# Define the amount of rubble scanned
image_nbr = 201

# Define backdrop size in mm
frame_size_v = 200
frame_size_h = 200

for i in range(image_nbr+1):
    
    # Paths
    rubble_path = f"/Users/mvk/github2/reimagine/Final/MOSAIC_WALLS_CORE24/scanned_rubble/scans/rubble_stativ02-{i:03}.jpg"
    contour_on_original_path = f"/Users/mvk/github2/reimagine/Final/MOSAIC_WALLS_CORE24/scanned_rubble/contour_on_original/contour_on_original_{i}.png"
    contour_line_path = f"/Users/mvk/github2/reimagine/Final/MOSAIC_WALLS_CORE24/scanned_rubble/contour_line/contour_{i}.png"
    rubble_shape_path = f"/Users/mvk/github2/reimagine/Final/MOSAIC_WALLS_CORE24/scanned_rubble/rubble_shape/rubble_shape_{i}.png"

    # Load the rubble image
    image = cv2.imread(rubble_path)
    
    # Check if the image was successfully loaded
    if image is None:
        print(f"Error: rubble image {i} not loaded.\n")
    else:
        print(f"Rubble image {i} loaded successfully!\n")

    # Resize the image based on the size of the backdrop and multiply by 10 to generate a better resolution
    image_resize = cv2.resize(image, (frame_size_v*10, frame_size_h*10))

    # Prepare the image to get the most accurate contour
    gray_image = cv2.cvtColor(image_resize, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    ret, binary_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Find the contour
    contours, hierarchy = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest_contour = max(contours, key=cv2.contourArea)
    epsilon = 0.01 * cv2.arcLength(largest_contour, True)
    print(epsilon)
    approx_contour = cv2.approxPolyDP(largest_contour, epsilon, True)


    # Draw the contour on the original rubble image and save it
    cv2.drawContours(image_resize, [approx_contour], -1, (0, 0, 255), 5)

    success = cv2.imwrite(contour_on_original_path, image_resize)

    if success:
        print(f"Contour on rubble image {i} saved successfully\n")
    else:
        print(f"Error saving contour on rubble image {i}\n")


    # Draw red contour on background image and save it
    new_color = (0, 0, 0)
    background_image = np.full_like(image_resize, new_color)
    cv2.drawContours(background_image, [approx_contour], -1, (0, 0, 255), 8)

    success = cv2.imwrite(contour_line_path, background_image)

    if success:
        print(f"Contour {i} saved successfully as {contour_line_path}\n")
    else:
        print("Error saving contour {i}\n")


    # Create an image which shows the shape of the rubble and save it
    white_colour = (255, 255, 255)
    white_image = np.full_like(image_resize, white_colour)
    cv2.drawContours(white_image, [approx_contour], -1, (0, 0, 0), cv2.FILLED)
    success = cv2.imwrite(rubble_shape_path, white_image)

    if success:
        print(f"Rubble shape {i} saved successfully as {rubble_shape_path}\n")
    else:
        print(f"Error saving rubble shape {i}\n")