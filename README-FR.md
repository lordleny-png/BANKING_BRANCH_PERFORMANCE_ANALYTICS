# 🏦 Banking Branch Performance Analytics
### Analyse de la performance bancaire, de la distribution des dépôts et de la concentration du marché

## 🚀 Tableau de bord interactif

**[Accéder au tableau de bord en ligne](https://bankingbranchperformanceanalytics-iznjueoncuiuwqdqjl6wey.streamlit.app/)**

Ce projet consiste à développer un tableau de bord interactif d'analyse des données bancaires à partir des données *Summary of Deposits* de la Federal Deposit Insurance Corporation (FDIC), l'organisme américain d'assurance des dépôts bancaires.

L'objectif est d'analyser la répartition géographique des dépôts, de comparer les établissements financiers, d'évaluer la concentration du marché bancaire et de transformer les résultats statistiques en recommandations utiles à la prise de décision.

## 🎯 Objectifs du projet

- Analyser la distribution des dépôts bancaires entre les États américains.
- Identifier les établissements financiers qui détiennent les volumes de dépôts les plus importants.
- Mesurer la concentration des dépôts à l'aide de l'indice Herfindahl-Hirschman (HHI).
- Examiner les parts de marché des trois principaux établissements dans chaque État.
- Étudier la distribution des dépôts, notamment les observations nulles et les valeurs extrêmes.
- Comparer les marchés selon plusieurs indicateurs.
- Formuler des recommandations fondées sur les données disponibles.

## 📊 Principales fonctionnalités

### 1. Analyse descriptive
- Indicateurs clés : dépôts totaux, nombre d'établissements, nombre d'enregistrements d'agences et nombre d'États.
- Classement des États selon les dépôts bancaires.
- Classement des établissements selon les dépôts agrégés.

### 2. Analyse de la concentration du marché
- Calcul du HHI par État.
- Analyse de la part cumulée des trois principaux établissements.
- Comparaison des niveaux de concentration entre les marchés.
- Identification des marchés nécessitant une analyse plus approfondie.

### 3. Analyse de la distribution et de la qualité des données
- Identification des enregistrements avec des dépôts nuls.
- Comparaison des distributions selon le numéro d'agence.
- Visualisation des valeurs extrêmes à l'aide de diagrammes en boîte.
- Examen des principaux enregistrements individuels.

### 4. Comparaison des États et recommandations
- Comparaison des dépôts totaux, du nombre d'établissements, du nombre d'enregistrements et des dépôts médians.
- Visualisation des relations entre les indicateurs.
- Génération de recommandations analytiques à partir des résultats observés.

## 🧰 Technologies utilisées

- **Python** : traitement et analyse des données.
- **Pandas** : nettoyage, agrégation et manipulation des données.
- **Plotly Express** : visualisations interactives.
- **Streamlit** : développement et déploiement du tableau de bord.
- **Pathlib** : gestion des chemins de fichiers.

## 📁 Source des données

Les données proviennent du programme *Summary of Deposits* de la FDIC.

Source officielle : [FDIC — Summary of Deposits](https://www.fdic.gov/bank-data-guidebank/summary-deposits-sod)

Les données comprennent notamment les établissements, les localisations des agences, les États, les numéros d'identification et les montants des dépôts.

Les montants de dépôts (`DEPSUMBR`) sont exprimés en milliers de dollars dans le fichier source et convertis en milliards de dollars pour certaines visualisations.

## 📈 Indicateurs et méthode d'analyse

### Indice Herfindahl-Hirschman (HHI)

Le HHI est calculé en additionnant les carrés des parts de marché, exprimées en pourcentage :

\[
HHI = \sum_{i=1}^{N} s_i^2
\]

où \(s_i\) représente la part des dépôts détenue par l'établissement \(i\) dans un État.

Les catégories de concentration utilisées dans ce projet sont descriptives :

- **HHI inférieur à 1 500** : concentration relativement faible.
- **HHI entre 1 500 et 2 500** : concentration modérée.
- **HHI supérieur à 2 500** : concentration élevée.

Ces seuils servent au dépistage analytique et ne constituent pas, à eux seuls, une conclusion réglementaire sur la concurrence.

### Autres indicateurs

- Dépôts totaux par État et par établissement.
- Part des trois principaux établissements.
- Nombre d'établissements et d'enregistrements.
- Dépôts médians et moyens.
- Nombre d'enregistrements avec des dépôts nuls.

## 💡 Principaux enseignements

L'analyse met en évidence plusieurs dimensions importantes du marché bancaire américain :

- Les volumes de dépôts varient fortement entre les États.
- Certains marchés présentent une concentration importante des dépôts entre quelques établissements.
- Les moyennes peuvent être influencées par des observations exceptionnellement élevées ; les médianes apportent donc un complément utile.
- Les enregistrements avec des dépôts nuls doivent être examinés avant toute conclusion opérationnelle.
- Un volume élevé de dépôts ne signifie pas nécessairement une rentabilité ou une efficacité opérationnelle supérieure.

## 🧭 Recommandations métier

1. **Surveiller la concentration des dépôts** dans les États où quelques établissements dominent le marché.
2. **Comparer les marchés à l'aide de plusieurs indicateurs**, plutôt que de se limiter aux dépôts totaux.
3. **Examiner les valeurs nulles et extrêmes** pour distinguer les anomalies potentielles des situations légitimes.
4. **Suivre l'évolution des parts de marché dans le temps** pour identifier les changements de concentration.
5. **Enrichir les données** avec les coûts d'exploitation, le nombre de clients, les encours de crédit, les volumes de transactions et les revenus afin de mesurer plus précisément la performance.

## ⚠️ Limites de l'analyse

- L'analyse repose sur une extraction
