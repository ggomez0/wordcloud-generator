# WordCloud Generator
[![Generar WordCloud Diario](https://github.com/ggomez0/WordCloud-Generator/actions/workflows/cron.yml/badge.svg)](https://github.com/ggomez0/WordCloud-Generator/actions/workflows/cron.yml)

## Descripción

WordCloud-Generator es un proyecto de automatización que realiza webscraping de los portales de noticias [INFOBAE](https://www.infobae.com/) y [EL PAIS](https://elpais.com/argentina/) para generar una nube de palabras con las palabras más utilizadas en las noticias de ambos sitios. La nube de palabras se actualiza automáticamente todos los días a las 00:00hs UTC-3 y se muestra en la siguiente página: [WordCloud Page](https://wordcloud.ggomez0.vercel.app/).

La generación de nubes de palabras a partir de noticias proporciona una visualización efectiva de las palabras clave utilizadas en los medios de comunicación. Al automatizar este proceso, podemos obtener una representación gráfica actualizada a diario de las tendencias en los artículos de ambos portales.

## Tecnologías utilizadas

- Python
- Beautiful Soup
- Scrapy
- NLTK
- WordCloud
- GitHub Actions

## Instalación

1. Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/ggomez0/WordCloud-Generator.git
cd WordCloud-Generator
```
## Uso

Ejecuta el script generatewordcloud.py para generar la nube de palabras:

```bash
python wordcloudgenerator.py
```

La imagen de la nube de palabras se generará automáticamente y se guarda en la carpeta wordcloud como "Wordcloud - 2023-08-04".

## Actualización Automática

El repositorio está configurado con GitHub Actions para que el script se ejecute automáticamente todos los días a las 00:00hs UTC-3. La imagen de la nube de palabras se actualizará en la [WordCloud Page](https://wordcloud.ggomez0.vercel.app/) cada vez que se ejecute el script.
