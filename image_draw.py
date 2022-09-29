import face_recognition
import numpy as np
from PIL import Image, ImageDraw
# Load the jpg files into numpy arrays
image = face_recognition.load_image_file('dosie.jpg')
encoding = face_recognition.face_encodings(image)[0]

# Load the jpg files into numpy arrays
image2 = face_recognition.load_image_file('PK.jpg')
encoding2 = face_recognition.face_encodings(image2)[0]

face_locations = face_recognition.face_locations(image2)
face_encodings = face_recognition.face_encodings(image2, face_locations)

# Convert the image to a PIL-format image so that we can draw on top of it with the Pillow library
pillow_image = Image.fromarray(image2)

# Create a Pillow ImageDraw Draw instance to draw with
draw = ImageDraw.Draw(pillow_image)

# Loop through each face found in the unknown image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # See if the face is a match for the known face(s)
    match = face_recognition.compare_faces([encoding], face_encoding)

face_distances = face_recognition.face_distance([encoding], face_encoding)
best_match_index = np.argmin(face_distances)
if match[best_match_index]:
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

# Remove the drawing library from memory as per the Pillow docs
del draw
pillow_image.show()
