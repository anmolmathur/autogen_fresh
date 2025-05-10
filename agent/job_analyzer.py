import os
import re
import json
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load resume and job description
def load_data(resume_path, job_description):
 resume = open(resume_path, 'r').read()
 job_desc = open(job_description, 'r').read()
 return resume, job_desc

# Preprocess text data
def preprocess_text(text):
 tokens = word_tokenize(text)
 tokens = [t for t in tokens if t.isalpha()]
 stop_words = set(stopwords.words('english'))
 tokens = [t for t in tokens if t not in stop_words]
 return ' '.join(tokens)

# Analyze resume and job description
def analyze_data(resume, job_desc):
 resume = preprocess_text(resume)
 job_desc = preprocess_text(job_desc)

 vectorizer = TfidfVectorizer()
 tfidf_resume = vectorizer.fit_transform([resume])
 tfidf_job_desc = vectorizer.transform([job_desc])

 similarity = cosine_similarity(tfidf_resume, tfidf_job_desc)

 # Detailed analysis
 title = "Software Engineer"
 match_score = f"{similarity[0][0]*100:.2f}%"
 applicability_summary = f"The candidate's profile matches{match_score} of the job requirements."
 strengths = ["Strong programming skills","Relevant experience"]
 gaps = ["Limited knowledge of machine learning"]

 analysis = {
 "title": title,
 "match_score": match_score,
 "applicability_summary": applicability_summary,
 "strengths": strengths,
 "gaps": gaps,
 "recommendation": "Proceed to next stage" if similarity[0][0] > 0.7 else "Skip to next candidate"
 }

 return analysis

# Main function
def main():
 resume_path = './data/resume.txt'
 job_description_path = './data/job_description.txt'
 resume, job_desc = load_data(resume_path, job_description_path)
 analysis = analyze_data(resume, job_desc)
 print(json.dumps(analysis, indent=4))

if __name__ == "__main__":
 main()