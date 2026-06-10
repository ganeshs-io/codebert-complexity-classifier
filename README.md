<div align="center">

# ⏱️ CodeBERT Time Complexity Classifier

[![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)](https://python.org)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Spaces-yellow?style=for-the-badge&logo=huggingface)](https://huggingface.co/spaces/VEGAxV2/codebert-complexity-classifier)
[![Kaggle](https://img.shields.io/badge/Kaggle-Notebook-20BEFF?style=for-the-badge&logo=kaggle)](https://kaggle.com/vegaxv2)

**Fine-tuned CodeBERT to classify Python code into 6 Big-O complexity classes**

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Click_Here-FF4B4B?style=for-the-badge)](https://huggingface.co/spaces/VEGAxV2/codebert-complexity-classifier)

</div>

---

## 📌 Overview

Given any Python function, this model predicts its time complexity class. No rules, no regex — pure learned representations from CodeBERT fine-tuned on labeled code snippets.

**Input:** Any Python function

**Output:** O(1) / O(log n) / O(n) / O(n log n) / O(n²) / O(2ⁿ) with confidence scores

---

## 🏆 Results

| Class | Precision | Recall | F1 |
|:------|:---------:|:------:|:--:|
| O(1) | 1.00 | 0.50 | 0.67 |
| O(log n) | 1.00 | 1.00 | 1.00 |
| O(n) | 1.00 | 1.00 | 1.00 |
| O(n log n) | 1.00 | 1.00 | 1.00 |
| O(n²) | 1.00 | 1.00 | 1.00 |
| O(2ⁿ) | 0.57 | 1.00 | 0.73 |
| **Overall** | **0.93** | **0.89** | **0.88** | 

> **Error analysis:** O(1) and O(2ⁿ) show lower recall — the model occasionally confuses constant-time hash lookups with exponential recursion patterns when variable names are ambiguous. All other classes achieve perfect classification.

---

## 🧠 Model

Base model: `microsoft/codebert-base`

Fine-tuned on a self-constructed dataset of 144 labeled Python snippets across 6 complexity classes. Dataset built from GeeksforGeeks examples and personal LeetCode solutions, augmented via variable renaming.

**Training:** 15 epochs · AdamW lr=2e-5 · T4 GPU · Val accuracy 91.67%

Model hosted at: [VEGAxV2/codebert-complexity-classifier](https://huggingface.co/VEGAxV2/codebert-complexity-classifier)

---

## 🚀 Try It Live

[![Live Demo](https://img.shields.io/badge/HuggingFace_Spaces-Live_Demo-yellow)](https://huggingface.co/spaces/VEGAxV2/codebert-complexity-classifier)

Paste any Python function and get instant complexity prediction with confidence scores.

---

## 🛠️ Tech Stack

`PyTorch` · `HuggingFace Transformers` · `CodeBERT` · `Gradio` · `Kaggle T4 GPU`
