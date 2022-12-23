#Import the required library
import cv2

#Reading the image
image = cv2.imread("One Direction.jpg")
cv2.imshow("One Direction",image)
cv2.waitKey(0)
#Converting the original image to greyscale
grey_filter = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("New One Direction",grey_filter)
cv2.waitKey(0)
#Inverting the new grayscale image
invert = cv2.bitwise_not(grey_filter)
cv2.imshow("Inverted",invert)
cv2.waitKey()
#Blurring the image using the Gaussian Function in cv2
blur = cv2.GaussianBlur(invert,(21,21),0)
cv2.imshow("Blurred",blur)
cv2.waitKey(0)
#Inverting the blurred image to convert the image into a pencil sketch
invertedblur = cv2.bitwise_not(blur)
cv2.imshow(" Inverted Blurred",invertedblur)
cv2.waitKey(0)

sketch_filter = cv2.divide(grey_filter,invertedblur,scale = 256.0)
cv2.imwrite("Output.jpg",sketch_filter)
cv2.imshow("Sketch",sketch_filter)
cv2.waitKey(0)

