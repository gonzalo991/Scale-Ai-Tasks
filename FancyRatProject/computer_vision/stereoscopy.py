import cv2
import numpy as np

# Load left and right images (taken from slightly different angles)
left_image = cv2.imread('left_image.jpg', cv2.IMREAD_GRAYSCALE)
right_image = cv2.imread('right_image.jpg', cv2.IMREAD_GRAYSCALE)

# Create a stereo disparity map
stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
disparity_map = stereo.compute(left_image, right_image)

# Normalize the disparity map for visualization
normalized_disparity = cv2.normalize(disparity_map, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# Display the normalized disparity map
cv2.imshow('Disparity Map', normalized_disparity)
cv2.waitKey(0)
cv2.destroyAllWindows()
