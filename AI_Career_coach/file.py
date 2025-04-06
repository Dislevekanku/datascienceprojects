# 🐾 Cat Spotter AI

Welcome to **Cat Spotter AI**, a beginner-friendly web app that demonstrates how machine learning trains AI to recognize cat images! This project is part of the "AI Toolbox Adventure: Tools & Theory for Beginners" plan, designed to help newbies explore AI concepts through hands-on tools.

## 📖 Overview

The Cat Spotter AI app lets you:
- Upload or select an image (e.g., a cat, dog, or other object) to see if the AI identifies it as a cat.
- Use a pre-trained machine learning model (MobileNetV2) to predict if the image contains a cat, with a confidence score.
- Learn how AI is trained with examples (photos) to recognize cats, through an educational section on machine learning.
- Share your results with the community on Discord!

This project aligns with Day 4 of the AI Toolbox Adventure, focusing on the theory: *"Machine learning trains AI with examples (e.g., photos to recognize cats)."* It uses a pre-trained model to show how AI learns patterns from data, making it a perfect introduction to machine learning for beginners.


## 🧠 Machine Learning Concepts

### How Does AI Learn to Spot Cats?
- **Machine Learning Basics:** Machine learning (ML) is a part of AI where computers learn by looking at examples, without being explicitly programmed. In this app, we use **supervised learning**, where the AI is trained with labeled data (e.g., photos labeled as “cat” or “not cat”).
- **Training Process:**
  1. **Collect Data:** We use a dataset like ImageNet, with over 14 million labeled images across 1,000 categories (including cats!).
  2. **Train the Model:** The AI learns patterns (e.g., cats have whiskers, pointy ears) by adjusting its settings (called weights) to get better at guessing.
  3. **Test the Model:** We show the AI new images it hasn’t seen before. If it correctly identifies cats, it’s learned successfully!
- **Pre-Trained Model:** We use **MobileNetV2**, a model already trained on ImageNet. This is called **transfer learning**—we take a pre-trained model and use it for our task (spotting cats) without training from scratch.
- **Why Use Photos?** Images contain visual patterns (like shapes, colors, textures) that AI can learn to recognize. For cat recognition, the AI learns features like ear shape, eye placement, and fur patterns.

## 🛠️ Setup Instructions

### Prerequisites
- **Python 3.9** installed on your system (specified in `runtime.txt` for compatibility).
- A code editor (e.g., VS Code) and terminal.
- (Optional) A free account on [Streamlit Community Cloud](https://streamlit.io/cloud) for deployment.
