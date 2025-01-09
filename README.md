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

1. Create a `.env` file at `src/`path  wich may contain:
```sh
NEWS_URL=https://www.domain.com/ultima-hora/
NEWS_IMG_URL=https://www.domain.com/wp-content/uploads
GEMINI_API_KEY="api-key"
UNIVERSIDAD="Escuela"
MATERIA="Análisis "
NOMBRE="Nombre Apellido"
CURSO="E4"
PROFESOR="Eco. ...."
```
2. Run the main script:
    ```sh
    python src/main.py
    ```