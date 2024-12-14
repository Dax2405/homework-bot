import google.generativeai as genai

promt = "Eres un estudiante universitario que acaba de leer una noticia. Quiero que escribas un texto de opinión sobre la noticia, como si fueras yo. Sé consiso, unas 6 - 7 líneas de Word, en un texto formal para un trabajo universitario y en un parrafo general sin frases de inicio o de fin, con dialecto de latinoamericano. Aporta tu punto de vista personal, mostrando cómo te afecta o qué opinas sobre el tema.\n"

genai.configure(api_key="")


def generate_opinion(news_text):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(promt + news_text)
    return response.text
