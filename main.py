from bs4 import BeautifulSoup
import requests
from export import export_to_excel
import re
from analyse import analyse_film_data



base_url = "https://www.allocine.fr/film/meilleurs/?page={}"
films_data = []

def convert_duration_to_minutes(duration_text):
    """Convertit une durée '2h 30min' en minutes (ex : 150)."""
    if not duration_text:
        return None
    
    hours_match = re.search(r'(\d+)h', duration_text)
    minutes_match = re.search(r'(\d+)min', duration_text)

    hours = int(hours_match.group(1)) if hours_match else 0
    minutes = int(minutes_match.group(1)) if minutes_match else 0

    return hours * 60 + minutes

try:    
    for page in range(1, 31):
        url = base_url.format(page)
        print(f"\n🔄 Chargement de la page {page}: {url}")

        source = requests.get(url)
        source.raise_for_status()
        soup = BeautifulSoup(source.text, 'html.parser')

        movies = soup.find('div', class_="gd-col-middle").find('ol').find_all('li')

        if not movies:
            print(f"❌ Fin de la récupération, plus de films trouvés après la page {page - 1}")
            break

        for movie in movies:
            title_tag = movie.find('a', class_="meta-title-link")
            if not title_tag:
                continue

            title_text = title_tag.text.strip()

            rank_div = movie.find('div', class_="label label-text label-sm label-primary-full label-ranking")
            rank = int(rank_div.text.strip()) if rank_div and rank_div.text.strip().isdigit() else None


            category_div = movie.find('div', class_="meta-body-item meta-body-info")
            if category_div:
                category_spans = category_div.find_all('span', class_="dark-grey-link")
                categories = ", ".join([span.text.strip() for span in category_spans]) if category_spans else "Genres inconnus"
            else:
                categories = "Genres inconnus"


            meta_body = movie.find('div', class_="meta-body")
            last_div = meta_body.find('div', class_="meta-body-item meta-body-info") if meta_body else None
            if last_div:
                duration_text = last_div.text.strip().split("|")[0].strip()
                duration = convert_duration_to_minutes(duration_text)
            else:
                duration = None

            rating_div = movie.find('span', class_="stareval-note")
            rating = float(rating_div.text.replace(',', '.').strip()) if rating_div else None


            rating_div = movie.find('span', class_="stareval-note")
            rating = float(rating_div.text.replace(',', '.').strip()) if rating_div else None


            author_div = movie.find('div', class_="meta-body-item meta-body-direction")
            if author_div:
                author_spans = author_div.find_all('span')
                author = author_spans[1].text.strip() if len(author_spans) > 1 else "Auteur inconnu"
            else:
                author = "Auteur inconnu"

            films_data.append([rank, title_text, author, categories, duration, rating])

except Exception as e:
    print(f"❌ Erreur : {e}")

export_to_excel(films_data)
analyse_film_data()