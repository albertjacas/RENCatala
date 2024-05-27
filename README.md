<a name="readme-top"></a>
<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Model de REN híbrid en llengua catalana</h3>

  <p align="center">
    Implementació d'un model híbrid de reconeixement d'entitats nomenades mitjançant l'ús de la llibreria spaCy i expressions regulars per al treball de final de grau a la Universitat Pompeu Fabra, facultat de Traducció i Interpretació.
    <br />
    <br />
  </p>
  <span align="center"> 
  
  [![Made with Python](https://img.shields.io/badge/Built%20with%20Python-%234584B6.svg?style=flat&logo=python&logoColor=FFDE57)](https://www.opengl.org)
  [![Made with spaCy](https://img.shields.io/badge/Built%20with%20spaCy-FFFFFF?style=for-the-badge&logo=spacy&style=flat")]([https://](https://developer.apple.com/xcode/))
  
  </span>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Taula de continguts</summary>
  <ol>
    <li>
      <a href="#about-the-project">Sobre el projecte</a>
      <ul>
        <li>
          <a href="#built-with">Desenvolupament</a>
        </li>
      </ul>
    </li>
    <li>
      <a href="#usage">Ús</a>
    </li>
    <li><a href="#acknowledgement">Nota addicional</a></li>
    <li><a href="#contact">Autoria</a></li>
    <li><a href="#licence">Llicència</a></li>
    <li><a href="#references">Referències</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## Sobre el projecte

En l'era digital actual, el processament del llenguatge natural (PLN) s'enfronta al repte de processar un volum i diversitat de textos sense precedents, circumstància que planteja obstacles significatius per a l'extracció i l'organització de la informació. El reconeixement d'entitats nomenades (REN) és crucial en aquest context, ja que identifica i classifica automàticament noms propis, ubicacions, dates, quantitats i altres expressions específiques. En aquest treball de fi de grau es desenvolupa un model de reconeixement d'entitats nomenades per a la llengua catalana mitjançant l'ampliació de les capacitats dels models existents, que sovint són limitats per a aquest idioma. La metodologia combina tècniques d'aprenentatge automàtic i regles per crear un model híbrid capaç de detectar entitats de nom propi (ENAMEX), expressions temporals (TIMEX) i expressions numèriques (NUMEX). L'avaluació del model amb el corpus AnCora, el qual s'ha anotat manualment, revela una mesura F del 82,03\%, fet que destaca la viabilitat i efectivitat del sistema. Finalment, es presenta una aplicació pràctica del model desenvolupat mitjançant la creació de glossaris *ad hoc* per a eines de traducció assistida per ordinador (TAO).

Resum de <a href="#references">[1]</a>


### Desenvolupament

- Python (versió 3.12.3)
- spaCy (version 3.7.4, pipeline ca_core_news_sm)


<!-- Before use -->
## Ús

1. Clona aquest repositori.

```
git clone https://github.com/albertjacas/RENCatala/
```

2. Obre la llibreta de Jupyter regex.ipynb. Per utilitzar un text diferent al de prova, substitueix el valor de la constant TEXT_ARXIU per l'arxiu desitjat.

3. Executa la llibreta regex.ipynb sencera.   

4. Obre la llibreta de Jupyter avaluacio.ipynb. Per utilitzar un cropus d'avaluació diferent al de prova (que ha d'estar en format .conllu), substitueix el valor de la constant CORPUS_ARXIU per l'arxiu desitjat.

5. Executa la llibreta avaluacio.ipynb sencera. 

6. Per crear un arxiu .csv amb totes les entitats nomenades detectades al text de prova, executa la llibreta exportar_eina_TAO.ipynb.

<!-- ACKNOWLEDGEMENTS -->
## Nota addicional

Aquest repositori conté els arxius desenvolupats com a part experimental del treball de fi de grau del grau de Traducció i Interpretació de la Universitat Pompeu Fabra <a href="#references">[1]</a>.


<!-- CONTACT -->
## Autoria

**Albert Jacas Mateu**

- Github: <a href="https://github.com/albertjacas/">@albertjacas</a>


<!-- LICENCE -->
## Llicència

RENCatala té llicència sota la GNU GPLv3, vegeu [LICENSE](https://github.com/albertjacas/RENCatala/blob/main/LICENSE) per a més informació.


<!-- REFERENCES -->
## Referències

* <a href="#">[1] Jacas Mateu, A. (2024). Implementació d'un model híbrid per al reconeixement d'entitats nomenades en llengua catalana. Manuscrit pendent de publicació. </a>

<p align="right">(<a href="#readme-top">Tornar a l'inici</a>)</p>
