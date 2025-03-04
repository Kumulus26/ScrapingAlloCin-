import openpyxl

def export_to_excel(data, filename="AlloCiné_Classement_Film.xlsx"):
    """ Exporter les données scrapées dans un fichier Excel """
    excel = openpyxl.Workbook()
    sheet = excel.active
    sheet.title = 'Top Rated Movies'
    
    # Ajouter les en-têtes
    sheet.append(["Classement", "Nom du film", "Auteur", "Catégorie", "Année", "Durée", "Note"])

    # Ajouter les films
    for film in data:
        sheet.append(film)

    # Sauvegarder le fichier
    excel.save(f"data/{filename}")
    print(f"✅ Fichier Excel généré : data/{filename}")