import os
import spacy
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from pdfminer.high_level import extract_text
from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Load English stopwords
stop_words = set(stopwords.words('english'))

# Define SQLAlchemy model for job listings
class JobListing(db.Model):
    __tablename__ = 'job_listings'

    # Define columns based on the provided schema
    job_id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer)
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    max_salary = db.Column(db.Float)
    med_salary = db.Column(db.Float)
    min_salary = db.Column(db.Float)
    pay_period = db.Column(db.String(50))
    formatted_work_type = db.Column(db.String(50))
    location = db.Column(db.String(255))
    applies = db.Column(db.Integer)
    original_listed_time = db.Column(db.DateTime)
    remote_allowed = db.Column(db.Boolean)
    views = db.Column(db.Integer)
    job_posting_url = db.Column(db.String(255))
    application_url = db.Column(db.String(255))
    application_type = db.Column(db.String(50))
    expiry = db.Column(db.DateTime)
    closed_time = db.Column(db.DateTime)
    formatted_experience_level = db.Column(db.String(50))
    skills_desc = db.Column(db.String(255))
    listed_time = db.Column(db.DateTime)
    posting_domain = db.Column(db.String(255))
    sponsored = db.Column(db.Boolean)
    work_type = db.Column(db.String(50))
    currency = db.Column(db.String(10))
    compensation_type = db.Column(db.String(50))

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'

        file = request.files['file']

        if file.filename == '':
            return 'No selected file'

        # You can save the file to a specific directory or process it as needed.
        # For example, saving the file in the 'uploads' directory:
        file.save(os.path.join('uploads', file.filename))

        # Extract text from the uploaded PDF file
        extracted_text = extract_text(os.path.join('uploads', file.filename))

        return render_template('index.html', extracted_text=extracted_text)

    return render_template('index.html')

@app.route('/calculate_match_score', methods=['POST'])
def calculate_match_score():
    if request.method == 'POST':
        # Extract description data from the request
        given_description = request.form.get('given_description')
        custom_description = request.form.get('custom_description')

        # Tokenize the given and custom descriptions
        given_tokens = word_tokenize(given_description)
        custom_tokens = word_tokenize(custom_description)

        # Remove stopwords from the tokens
        given_filtered = [word for word in given_tokens if word.lower() not in stop_words]
        custom_filtered = [word for word in custom_tokens if word.lower() not in stop_words]

        # Calculate the similarity score (here, I'm using the length ratio as a simple metric)
        match_score = len(set(given_filtered) & set(custom_filtered)) / len(set(given_filtered + custom_filtered))

        return jsonify({"match_score": match_score})

@app.route('/job_listings', methods=['GET'])
def get_job_listings():
    # Fetch all job listings from the database
    job_listings = JobListing.query.all()
    job_data = []
    for job in job_listings:
        job_data.append({
            'job_id': job.job_id,
            'company_id': job.company_id,
            'title': job.title,
            'description': job.description,
            'max_salary': job.max_salary,
            'med_salary': job.med_salary,
            'min_salary': job.min_salary,
            'pay_period': job.pay_period,
            'formatted_work_type': job.formatted_work_type,
            'location': job.location,
            'applies': job.applies,
            'original_listed_time': job.original_listed_time,
            'remote_allowed': job.remote_allowed,
            'views': job.views,
            'job_posting_url': job.job_posting_url,
            'application_url': job.application_url,
            'application_type': job.application_type,
            'expiry': job.expiry,
            'closed_time': job.closed_time,
            'formatted_experience_level': job.formatted_experience_level,
            'skills_desc': job.skills_desc,
            'listed_time': job.listed_time,
            'posting_domain': job.posting_domain,
            'sponsored': job.sponsored,
            'work_type': job.work_type,
            'currency': job.currency,
            'compensation_type': job.compensation_type
        })
    return jsonify({'job_listings': job_data})

if __name__ == '__main__':
    app.run(debug=True)
