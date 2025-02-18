
### **🐍 script.py**
```python
keywords = {"Python", "Machine Learning", "Data Structures", "SQL", "Django", "Flask", "TensorFlow", "NLP"}

resume = input("Paste your resume text:\n").lower()
score = sum(1 for word in keywords if word.lower() in resume)

print(f"\nResume Score: {score}/{len(keywords)}")

if score < len(keywords) / 2:
    print("🔴 Improve your resume by adding more relevant skills!")
else:
    print("✅ Your resume is well-optimized!")
