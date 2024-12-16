# dazzle-dash

## Objectif :
Le directeur marketing souhaite avoir un
outil permettant d’automatiser l’analyse des données en interne.

Il faut développer un outil de data visualisation.

Afin répondre à la problématique et de créer une preuve de
concept, nous utilisons une source de données libre d’accès.

## Data storytelling

Le data storytelling est l'art de raconter une histoire à travers les données.

Il s'agit de transformer des informations complexes en récits  accessibles via la visualisation de données, l'analyse et la narration.

L'objectif est de donner du sens aux données brutes en les contextualisant et en les présentant de manière engageante.

Il faut :

- Faciliter la compréhension d'informations complexes pour un public non expert
- Mettre en évidence des insights importants et des opportunités cachées dans les données
- Soutenir la prise de décision basée sur les données en rendant l'information plus percutante

Le data storytelling s'appuie sur trois piliers :
1. les données
2. leur visualisation graphique
3. la narration qui les accompagne

En combinant ces éléments de manière efficace, le data storytelling permet de communiquer des analyses de données de façon claire, convaincante et orientée vers l'action.


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

Supression de la colonne 'under-five deaths', elle fait doublon avec 'infant death'.

Les observations sur la population chinoise et indienne semblent problématiques :
Multiplication de la population chinoise par 1000
Multiplication de la population indienne par 10

## Compréhension des données

| **Colonne**                      | **Description**                                                                                                                                        |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| **country**                      | Le pays pour lequel les données sont fournies.                                                                                                          |
| **year**                         | L'année de collecte des données.                                                                                                                        |
| **status**                       | Le statut de développement du pays.                                                               |
| **life expectancy**              | L'espérance de vie à la naissance (en années).                                                                                                          |
| **adult mortality**              | Le taux de mortalité des adultes exprimé pour 1000 adultes âgés de 15 à 60 ans.                                                           |
| **infant deaths**                | Le nombre absolu de décès infantiles (moins d'un an).                                                                                                   |
| **alcohol**                      | La consommation d'alcool par habitant (litres par an).                                                                                                  |
| **percentage expenditure**       | Le pourcentage des dépenses de santé par rapport au produit intérieur brut (PIB).                                                                        |
| **hepatitis b**                  | La couverture vaccinale contre l'hépatite B (% de la population).                                                                                       |
| **measles**                      | Le nombre de cas de rougeole.                                                                                                                           |
| **bmi**                          | L'indice de masse corporelle moyen de la population.                                                                                                    |
| **under-five deaths**            | Le nombre absolu de décès d'enfants de moins de 5 ans.                                                                                                  |
| **polio**                        | La couverture vaccinale contre la poliomyélite (% de la population).                                                                                    |
| **total expenditure**            | Les dépenses totales de santé par habitant (% du PIB).                                                                                                  |
| **diphtheria**                   | La couverture vaccinale contre la diphtérie (% de la population).                                                                                       |
| **hiv/aids**                     | Le taux de prévalence du VIH/sida (% de la population).                                                                                                 |
| **gdp**                          | Le produit intérieur brut (PIB) par habitant (en dollars américains).                                                                                   |
| **population**                   | La population totale.                                                                                                                                  |
| **thinness 1-19 years**          | Le pourcentage de maigreur chez les personnes âgées de 1 à 19 ans.                                                                                      |
| **thinness 5-9 years**           | Le pourcentage de maigreur chez les enfants âgés de 5 à 9 ans.                                                                                          |
| **income composition of resources** | L'indice de développement humain basé sur les ressources (échelle de 0 à 1).                                                                            |
| **schooling**                    | Le nombre moyen d'années de scolarité.                                                                                                                  |


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