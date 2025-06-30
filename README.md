# Licht auf Abwegen – Wie Naturgesetze die Richtung bestimmen

Dieses Repository enthält Materialien zu einer mathematischen Schülervorlesung zum Thema **Lichtbrechung und Variationsprinzipien**.

Die zentrale Fragestellung lautet:
> Warum nimmt Licht beim Übergang zwischen zwei Medien (z. B. Luft und Wasser) einen geknickten Weg – und nicht den direkten?

---

## 📄 Materialien

### `handout.pdf`
Ein begleitendes Handout zur Vorlesung, das die physikalischen und mathematischen Grundlagen der Lichtbrechung erklärt. Es führt in das Prinzip der minimalen Laufzeit ein und motiviert das Snell’sche Gesetz mithilfe der Variationsrechnung.

### `lichtbrechung.py`
Ein Python-Skript, das die Gesamtlaufzeit des Lichtstrahls für verschiedene Wege berechnet, den optimalen Weg numerisch bestimmt und diesen grafisch darstellt. Es zeigt:

- den Verlauf der Gesamtlaufzeit \( T(y^*) \)
- den optimalen Strahlenverlauf zwischen Start- und Zielpunkt
- die Lage der Grenzfläche zwischen den Medien

### `lichtbrechung_interaktiv.ipynb`
Ein interaktives Jupyter-Notebook, das die Inhalte aus dem Python-Skript visualisiert – jedoch mit frei einstellbaren Parametern (z. B. Brechungsindizes, Positionen). Damit kann man spielerisch untersuchen, wie sich der Lichtweg verändert.

➡️ Öffne das Notebook direkt in [Google Colab](https://colab.research.google.com/) oder einer lokalen Jupyter-Umgebung.

---

## 🛠 Voraussetzungen

Für die Ausführung des Python-Skripts oder des Notebooks lokal benötigst du:
- Python 3 mit den Paketen: `numpy`, `matplotlib`, `scipy`, `ipywidgets`
- Alternativ: JupyterLab oder Google Colab (keine Installation nötig)

---

## 📬 Kontakt

Erstellt von **Mathis Fricke**  
Technische Universität Darmstadt  
E-Mail: fricke@mma.tu-darmstadt.de