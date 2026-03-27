from deepface import DeepFace
import os

# The filename of the uploaded image is available in the kernel state
img_path = filename

# Path to the problematic weight file
weight_file = "/root/.deepface/weights/age_model_weights.h5"

# Remove the problematic weight file if it exists
if os.path.exists(weight_file):
    print(f"Deleting corrupted weight file: {weight_file}")
    os.remove(weight_file)

# Running the Multi-Agent Analysis
try:
    print(f"Analyzing image: {img_path}")
    results = DeepFace.analyze(img_path = img_path,
                               actions = ['age', 'gender', 'emotion'],
                               enforce_detection=False) # Set to False to prevent errors if a face isn't perfectly detected

    # Output Display
    if results:
        print("\n--- DEEPFACE ANALYSIS COMPLETE ---")
        print(f"Detected Age: {results[0]['age']}")
        print(f"Detected Gender: {results[0]['dominant_gender']}")
        print(f"Detected Emotion: {results[0]['dominant_emotion']}")
    else:
        print("No faces detected or analysis results found.")

except Exception as e:
    print("Error during DeepFace analysis:", e)
