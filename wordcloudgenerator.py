from bs4 import BeautifulSoup
import requests
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from datetime import datetime
import nltk

# Download the punkt tokenizer data if not already available
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

# Now import and use word_tokenize
from nltk.tokenize import word_tokenize

# URL de Infobae y EL PAIS
url_infobae = "https://www.infobae.com/ultimas-noticias/"
url_elpais = "https://elpais.com/argentina/"

# Se realiza la petición GET
html_infobae = requests.get(url_infobae).text
html_elpais = requests.get(url_elpais).text

# Se crea un objeto BeautifulSoup para cada una de las páginas, pasándole como argumento el HTML
soup_infobae = BeautifulSoup(html_infobae, "html.parser")
soup_elpais = BeautifulSoup(html_elpais, "html.parser")

# Se utilizan los métodos find_all de BeautifulSoup para buscar los elementos HTML que contienen las noticias en cada una de las páginas
articles_infobae = soup_infobae.find_all('a', class_='d23-feed-list-card')
articles_elpais = soup_elpais.find_all('article')

# Lista para almacenar los copetes de ambas fuentes de noticias
copetes_list = []

# Se recorren las listas de noticias del portal INFOBAE para extraer información de cada una de ellas y guardar los copetes en la lista
for article in articles_infobae:
    copete = article.find('div', class_='d23-deck').text.strip()
    copetes_list.append(copete)

# Se recorren las listas de noticias EL PAIS para extraer información de cada una de ellas y guardar los copetes en la lista
for article in articles_elpais:
    copete = article.find('p')
    if copete:
        copete = copete.text.strip()
        copetes_list.append(copete)

# Generar el texto completo con todos los copetes juntos
todo_el_texto = " ".join(copetes_list)

# Luego, aquí viene el código 2 sin necesidad de usar un archivo CSV
with open('stopwords.txt', 'r', encoding='utf-8') as file:
    stop_words = set(file.read().splitlines())
# Tokenizar y filtrar stopwords
tokenizado = word_tokenize(todo_el_texto)
tokenizado_filtrado = [palabra for palabra in tokenizado if palabra.lower() not in stop_words]

# Crear el WordCloud
wordcloud = WordCloud(width=800, height=600).generate(" ".join(tokenizado_filtrado))
plt.figure(figsize=(18, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
fecha_actual = datetime.now().strftime("%Y-%m-%d")
plt.title(f"WordCloud - {fecha_actual}")
plt.tight_layout()
ruta_guardado = f"wordcloud/Wordcloud - {fecha_actual}.png"
plt.savefig(ruta_guardado, transparent=True)
plt.show()
