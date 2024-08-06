import numpy as np
#import cv2
import dlib
from PIL import Image
# Load the dlib models
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
face_rec_model = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')

def get_face_encoding(image):
    try:
        img = Image.open(image).convert('RGB')
        img_array = np.array(img)
        dets = detector(img_array, 1)
        
        if len(dets) == 0:
            print("No faces found in the image.")
            return None

        shape = predictor(img_array, dets[0])
        face_descriptor = face_rec_model.compute_face_descriptor(img_array, shape)
        return np.array(face_descriptor)
    except Exception as e:
        print(f"Error in get_face_encoding: {e}")
        return None
        # shapes = [predictor(rgb_img, face) for face in faces]
        # face_descriptors = [face_rec_model.compute_face_descriptor(rgb_img, shape) for shape in shapes]

        # return face_descriptors
      #  return face_encoding
   # except Exception as e:
        # print(f"Error processing image: {e}")
        # return None
    