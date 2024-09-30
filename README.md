
# AutoCal - Ai Based HandDrawing Calculator


This is a FastAPI-based application for processing images to analyze and compute expressions. It includes image decoding, analysis of content, and returning the evaluated results in a structured format. The backend is powered by FastAPI and utilizes a serverless architecture to ensure scalability.

Features
Image Processing: Accepts base64-encoded images and decodes them for analysis.
Expression Evaluation: Analyzes the content of the image to extract mathematical expressions and compute the results.
REST API: Provides a RESTful API using FastAPI for seamless integration.
Environment: Supports environment configuration through .env for sensitive data like API keys, secrets, and configuration settings.




## Clone The Repository
```
git clone https://github.com/Rohitlodhii/autocal-backendd.git
cd autocal-backendd

```

## Run in Your Local Environment

```
python3 -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`

pip install -r requirements.txt

```

## Setup the Environment Variables

Create a .env file inside root dir

```
GEMINI_API_KEY=your_api_key_here
```




