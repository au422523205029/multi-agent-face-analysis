from deepface import DeepFace

def analyze_face(img_path):
    # Multi-agent analysis logic
    result = DeepFace.analyze(img_path = img_path, 
                              actions = ['age', 'gender', 'emotion'],
                              enforce_detection=False)
    return result[0]

if __name__ == "__main__":
    # Test with an image
    print(analyze_face("test.jpg"))
