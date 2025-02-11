import re
import math
from collections import Counter
from docx2txt import process

def read_word_document(file_path):
    """Reads text from a Word document."""
    text = process(file_path)
    return text

def preprocess_text(text):
    """Cleans the text by removing special characters and extra spaces."""
    text = re.sub(r'[^a-zA-Z0-9. ]', '', text)  # Remove special characters
    sentences = text.split('.')  # Split into sentences
    sentences = [s.strip() for s in sentences if s.strip()]  # Remove empty strings
    return sentences

def word_frequencies(sentences):
    """Computes word frequencies in the given sentences."""
    word_freq = Counter()
    for sentence in sentences:
        words = sentence.lower().split()
        word_freq.update(words)
    
    max_freq = max(word_freq.values(), default=1)
    for word in word_freq:
        word_freq[word] /= max_freq  # Normalize frequencies
    
    return word_freq

def score_sentences(sentences, word_freq):
    """Scores each sentence based on word importance."""
    sentence_scores = {}
    for sentence in sentences:
        words = sentence.lower().split()
        score = sum(word_freq.get(word, 0) for word in words)
        sentence_scores[sentence] = score
    
    return sentence_scores

def generate_summary(text, compression_ratio=0.3):
    """Generates a summary by selecting the highest-scoring sentences."""
    sentences = preprocess_text(text)
    word_freq = word_frequencies(sentences)
    sentence_scores = score_sentences(sentences, word_freq)
    
    num_sentences = max(1, math.ceil(len(sentences) * compression_ratio))
    sorted_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    summary = ' '.join(sorted_sentences[:num_sentences])
    
    return summary

if __name__ == "__main__":
    file_path = "Vishwamitra.docx"  # Replace with the actual file path
    transcript = read_word_document(file_path)
    summary = generate_summary(transcript, compression_ratio=0.4)
    print("Meeting Summary:")
    print(summary)
    print(len(transcript))
    print(len(summary))
