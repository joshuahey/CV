# src: The image to use thresh: The threshold maxval: The maxval to use type: Type of filtering .The threshold function works by looking at each pixel's
# grayscale value and assigning a value if it is below the threshold and another value if it is above the threshold. In our example the threshold is
# 0 (black) and the type is binary inverse so if a value is above the threshold the assigned value is 0 (black) and if it is below or equals the threshold 
# the maxval 255 (white) is used. So if the pixel is 0 black it is assigned 255 (white) and if the pixel is not black then it is assigned black which 
# is what THRESH_BINARY_INV tells OpenCV to do. This is how it would work without THRESH_OTSU.


# Returns ret which is the threshold used and outs which is the image
ret, outs = cv2.threshold(src = image, thresh = 0, maxval = 255, type = cv2.THRESH_OTSU+cv2.THRESH_BINARY_INV)

# Make the image larger when it renders
plt.figure(figsize=(10,10))

# Render the image
plt.imshow(outs, cmap='gray')
