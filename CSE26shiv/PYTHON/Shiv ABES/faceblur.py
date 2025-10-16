import cv2
import numpy as np

def blur_faces_in_image(image_path, output_path=None):
    """
    Detects multiple faces in the given image using OpenCV's Haar Cascade classifier
    and applies a Gaussian blur to each detected face region.
    
    Args:
    - image_path (str): Path to the input image.
    - output_path (str, optional): Path to save the output image. If None, displays the image.
    
    Returns:
    - None: Saves or displays the processed image.
    """
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not load the image. Check the path.")
        return
    
    # Load the pre-trained Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Convert the image to grayscale for face detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale image (handles multiple faces automatically)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # If faces are detected, blur each face region
    if len(faces) > 0:
        print(f"Detected {len(faces)} face(s). Blurring each one...")
        for i, (x, y, w, h) in enumerate(faces, 1):
            # Extract the face region
            face_region = image[y:y+h, x:x+w]
            
            # Apply Gaussian blur to the face region
            blurred_face = cv2.GaussianBlur(face_region, (99, 99), 30.0)
            
            # Replace the original face region with the blurred one
            image[y:y+h, x:x+w] = blurred_face
            print(f"Blurred face {i}: position ({x}, {y}), size ({w}x{h})")
    else:
        print("No faces detected. Returning original image.")
    
    # Save the output if a path is provided, otherwise display it
    if output_path:
        cv2.imwrite(output_path, image)
        print(f"Processed image saved to {output_path}")
    else:
        cv2.imshow('Blurred Faces (Multiple Supported)', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Example usage
if __name__ == "__main__":
    input_image = "Shiv ABES\face.jpg"  # Replace with your image path (works for images with multiple faces)
    output_image = ""     # Optional: Replace with desired output path
    
    blur_faces_in_image(input_image, output_image)

