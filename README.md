# 🎬 Scraping AlloCiné - Meilleurs Films

Ce projet extrait automatiquement les **meilleurs films sur AlloCiné** et les exporte en **Excel et PDF**.

## 🚀 Fonctionnalités
✅ Scraping des **titres, auteurs, genres, durée (en minutes) et notes**  
✅ Exportation des films dans **un fichier Excel** (`data/AlloCiné_Classement_Film.xlsx`)  
✅ Analyse des films avec **Pandas et Matplotlib**  
✅ Affichage d’un **graphique des durées de films**  

---

## 📂 Exemple de sortie
| Classement | Film | Auteur | Genre | Durée (min) | Note |
|------------|---------------------------|------------|--------------|--------|------|
| 1          | Le Parrain                 | Coppola   | Drame, Policier | 175  | 4.9  |
| 2          | Le Seigneur des Anneaux    | Jackson   | Fantastique   | 201  | 4.8  |

---

## 🛠️ Installation
### **1️⃣ Cloner le projet**
```bash
git clone https://github.com/TON-PROFIL/scraping-allocine.git
cd scraping-allocine

### **2️⃣ Installer les dépendances**
```bash
pip install -r requirements.txt

### **3️⃣ Cloner le projet**
```bash
python main.py
