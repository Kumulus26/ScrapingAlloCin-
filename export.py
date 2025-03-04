import openpyxl

def export_to_excel(data, filename="AlloCiné_Classement_Film.xlsx"):
    """ Exporter les données scrapées dans un fichier Excel """
    excel = openpyxl.Workbook()
    sheet = excel.active
    sheet.title = 'Top Rated Movies'
    
    sheet.append(["Classement", "Nom du film", "Auteur", "Catégorie", "Durée (min)", "Note"])

    for film in data:
        sheet.append(film)

    excel.save(f"data/{filename}")
    print(f"✅ Fichier Excel généré : data/{filename}")