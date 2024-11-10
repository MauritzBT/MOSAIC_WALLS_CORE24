# MOSAIC_WALLS_CORE24
This repository contains the codes for the Mosaic Walls project of the CORE 2024 course at TU Delft.

Please look at the video Mosaic_Walls_Video_Code, which shows you step by step how to run the code. 

The code has a pure python part, which can be run in VSCODE for example and a grasshopper part: 

GITHUB
______________
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

GRASSHOPPER
______________
STEP 1: File SetUp

Version and Plugin requirements:
Rhino:
 - Version: Rhino 8
 - Units: mm
Grasshopper:
 - Version: Grasshopper for Rhino 8
 - Plug-ins:
    - LadyBug
    - Parakeet (not available for MAC)
    - OpenNest

Instructions for File SetUp:
1) Open a Rhino 8 file (units in mm)
2) Open the Grasshopper code titled 00_FINAL CODE
3) Follow the steps listed in the instructions group (also listed below)


STEP 2: Rubble Geometry

Instructions for CSV files:
1) Be sure to have CSV files downloaded
2) Ensure that the files are named incrementally
3) Paste path to folder in panel
4) Ensure that the number of scans is correct
5) Check that the output panel contains polyline curves

TROUBLE SHOOTING:
 - enter the python in grasshopper component
 - review how the file_path variable is completed with the i counter
 - test different ways to write the file_path (use the examples for troubleshooting)

Instructions for random rubble generator:
1) Adjust number of duplicates
2) Adjust grid size (for organization of curves)
3) Adjust lower bound and upper bound limits for vector scaling
4) Ensure that the CSV file units match the rhino file units (ie. mm)
5) Adjust lower bound and upper bound limits for geometry scaling
6) Select "Randomized rubble geometries" from list
7) Set "Push rubble geometries" to True


STEP 3: Sort Rubble

Instructions for sorting rubble:
1) Set "Sort rubble?" to True


STEP 4: Create wall, buttress, and cell geometries

Instructions for wall, buttresses, and cells:
1) Adjust wall dimensions
   1.1) Adjust wall dimensions
   1.2) Adjust grid divisions
        NOTE: 
         - minimize division in Y to zero for more square cells
         - X and Y divisions have limits applied to them
2) Select pattern type
   2.1) Choose Pattern Type
   2.2) Choose Cell Widths
3) Adjust pattern factors
   RANDOMIZED ROW HEIGHTS:
     1) Change Factor for max_y
         - keep close to 0.25, don't go beyond 0.4
     2) Change Lower end and Upper end for y (factor multiplier)
     3) Change random seed to get different variations
   ALTERNATING ROW HEIGHTS:
     1) Change Factor for max_y
         - keep close to 0.25, don't go beyond 0.4
   GRADIENT ROW HEIGHTS:
     1) Change Gradient scale factor
         - closer to 1.0 is less dramatic of a gradient
     2) Choose Gradient direction
         - NOTE: Big on bottom has a bug, ran out of time to fix it
   RANDOMIZED CELL WIDTHS:
     1) Change MAX percentage of cell width
         - keep close to 0.25, don't go beyond 0.5
     2) Change random seed to get different variations
4) Adjust buttress dimensions
   4.1) Change Top width
         - will take max between set value and wall thickness
   4.2) Change Bottom width
         - will be 25% wider than top width
5) Select which limits will be implemented (Set to True or False)
   SLENDERNESS LIMIT:
	h/t < 27
   PLAN AREA LIMIT:
	l*t > 0.04 m2
   CELL DIMENSION LIMITS:
	- The cell height should not exceed 1/2 of the cell width
	- Cell width dimension limits based on rubble geometry input
	- Cell height dimension limits based on rubble geometry input
6) Compare available rubble geometry to resulting cell geometries
   - Ensure that the number of cells < 1/3 the number of rubble pieces available
   - Ensure that the cell dimensions are within 10% of rubble dimensions
7) Push Tessellations and Geometry


STEP 5: Packing

SETTINGS:
 - Area tolerance: how much voided cell area is acceptable
 - General tolerance: how much difference in largest segment and base of cell

Instructions for packing:
1) Switch on Pack for main wall
   - Start with Area tolerance at 0.25
   - Find a General tolerance which successfully packs the wall
   - Shift the slider down to minimize the General tolerance
2) Switch on Pack for buttresses
   - Start with Area tolerance at 0.25
   - Find a General tolerance which successfully packs the buttresses
   - Shift the slider down to minimize the General tolerance


STEP 6: Pack Voids

1) Select Type of rubble
   ELLIPSES:
    - small representations of rubble such that the pick and place program can estimate the location of rubble
   REMAINING RUBBLE:
    - uses the remaining rubble pieces to finish packing the wall
    - this should only be used if there is a sufficient amount of small rubble scanned and/or produced
   SCALED DOWN RUBBLE: 
    - ideal representation to be used for visual representation and the structural verification check
2) If scaled down rubble is selected, adjust the scale factor as wanted


STEP 7: Structural Verification

Instructions for structural verification:
1) Push the Data Dam
2) Decide how many divisions between the rows (2-4 is ideal)
3) Choose which path to test
4) Choose maximum movement as percentage of cell width (1.5 is ideal)
5) Check if the number of fitness sliders matches the number required
   - If it does not, double click on the Gene Pool and set the number of sliders accordingly
6) Slide the fitness sliders until there is an ideal path which goes through the wall (this will reduce the algorithm time)
7) Double click on the Evolutionary Solver and set the Fitness to Minimize
8) Run the Evolutionary Solver until the fitness is minimized to your satisfaction
9) Check shortest path length is within the acceptable range