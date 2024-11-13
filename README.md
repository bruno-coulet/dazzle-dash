# dazzle-dash

## Nettoyage des données

Remplacer les majuscules des noms de colonnes par des minuscules :


Retirer les espaces en début et fin des noms de colonnes :
```python
df.columns = df.columns.str.strip()
```

Filtrer le DataFrame pour ne garder que les colonnes spécifiées
```python
df_filtered = df[liste de colonnes à garder]
```

## compréhension des données

percentage expenditure : argent dépensé pour la santé en une année par rapport au PIB.

## Analyse multivarié

Etudier la corrélation entre la moyenne de dépense de santé des pays développé et des pays en développement et l'espérance de vie de 2000 à 2015, 

## Définissez la notion de data storytelling

## Exemple.

● Réalisez une veille sur l’outil et apprenez à construire une application
Dash d’une page unique simple


## L’outil Dash


```bash
pip install dash
```
**module dcc** (Dash Core Components).
Ce module inclus dcc.Graph, permet de rendre des graphs interactifs.

**Librairie plotly.express**
permet de dessiner des graphs interactifs et de l'attribuer à la figure du dcc.Graph

Using the plotly.express library, we build the histogram chart and assign it to the figure property of the dcc.Graph. This displays the histogram in our app.

**dcc.RadioItems**
radio buttons component

`callback, Output, Input`
module de rappel et les deux arguments couramment utilisés dans le rappel : Sortie et Entrée.



## Sources de données libres d’accès :
https://drive.google.com/file/d/1RPqWJl1GSsPpeUBg2wFx0SIIh74eGKJE/view