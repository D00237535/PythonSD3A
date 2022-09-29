from PIL import Image
import face_recognition

# Load the jpg files into numpy arrays
image = face_recognition.load_image_file('PK.jpg')

face_locations = face_recognition.face_locations(image)

for face_locations in face_locations:
    top, right, bottom, left = face_locations
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()
