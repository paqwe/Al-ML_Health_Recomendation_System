from flask import Flask, request, jsonify
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
import re

app = Flask(__name__)

@app.route('/post_string', methods=['POST'])
def post_string():
    try:
        data = request.get_json()
        if not data or 'input_string' not in data:
            return jsonify({'error': 'Missing input_string'}), 400
        
        input_string = data['input_string']
        symptom_words = get_symptom_words(input_string)
        return jsonify({'message': 'String received', 'input': input_string}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


desc_from_patient = "Doctor, I have  been feeling extremely tired all the time, even after resting.My body feels weak, and I sometimes struggle to do simple tasks."
def get_symptom_words(desc_from_patient):

    #split text into sentences
    sentences=sent_tokenize(desc_from_patient)

    #split text into words
    words=word_tokenize(desc_from_patient)

    #remove punctuation character
    desc_from_patient=re.sub(r"[^a-zA-Z0-9]"," ",sentences[1])

    #remove stop words
    words=[w for w in words if w not in stopwords.words("english")]

    #Reduce words to their stems
    stemmed=[PorterStemmer().stem(w)for w in words]

    #Reduce words to their root form
    lemmatized = [WordNetLemmatizer().lemmatize(w) for w in words]

    return desc_from_patient









    
if __name__ == '__main__':
    app.run(debug=True)

