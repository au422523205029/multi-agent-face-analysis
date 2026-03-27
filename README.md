# Multi-Agent Face Analysis System

A modular ML framework designed to recognize multiple facial attributes using specialized agents.

## 🧠 System Architecture
Instead of a monolithic model, we use a **Multi-Agent** approach where each agent specializes in a single task. This improves precision and allows independent model optimization.

## 📊 Agent Performance
| Agent | Model/Architecture | Expected Accuracy |
| :--- | :--- | :--- |
| **Face Detector** | OpenCV / RetinaFace | 98% |
| **Gender Agent** | VGG-Face | 95% |
| **Age Agent** | Deep Expectation | 81% |
| **Emotion Agent** | CNN / FER | 89% |

## 🚀 Key Technologies
- **Python**
- **DeepFace Framework**
- **TensorFlow / Keras**
-
