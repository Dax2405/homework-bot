# Homework Bot


## Description

Homework Bot is an automated tool that generates opinion documents about national and international news. It uses web scraping techniques to fetch news, natural language processing to generate opinions, and creates documents in Word and PDF formats.

## Instalation

1. Clone the repository

```sh
git clone https://github.com/Dax2405/homework-bot.git
```

2. Create and activate a virtual enviroment:

```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```


## Usage

1. Configure the Google Generative AI API in `ai_processing.py`:
    ```python
    genai.configure(api_key="YOUR_API_KEY")
    ```

2.  Configure some variables in the `docs_generator.py` file. Open the file and edit the following variables with the appropriate information:

```python
# Edit these variables with the appropriate information
universidad = "Your University Name"
materia = "Your Subject"
nombre = "Your Name"
curso = "Your Course"
profesor = "Your Professor's Name"
```


3. Run the main script:
    ```sh
    python src/main.py
    ```