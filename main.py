import cv2

# TODO capture image
image = cv2.imread("image/index.png")
cv2.imshow(winname='Me', mat=image)

gray_image = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY)
cv2.imshow(winname='Me Grey', mat=gray_image)

haar_cascade = cv2.CascadeClassifier('haarcascade_face.xml')

#returns the number or rectangles with faces
faces_rectangle = haar_cascade.detectMultiScale(image=gray_image)

number_of_faces = len(faces_rectangle)
print(number_of_faces)
cv2.waitKey(0)

# TODO capture video
# # Create a VideoCapture object
# cap = cv2.VideoCapture(0)
#
# # Capture an image from the camera
# ret, frame = cap.read()
#
# # Save the image as a file
# cv2.imwrite('captured_image.jpg', frame)
#
# # Release the camera
# cap.release()
