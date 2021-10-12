# "Künstliche Intelligenz und Maschinelles Lernen in der Praxis"

Begleitmaterial zum Online Kurs "Künstliche Intelligenz und Maschinelles Lernen in der Praxis" von Christian Warmuth und Johannes Hötter.

Link zum Kurs: https://open.hpi.de/courses/kipraxis2021"

Link zum Vorgängerkurs: https://open.hpi.de/courses/kieinstieg2020


<!-- Gliederung -->
<summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#Kurszusammenfassung">Kurszusammenfassung</a>
    </li>
    <li>
      <a href="#installation">Installation</a>
    </li>
    <li><a href="#hinweise">Hinweise zur Ausführung</a></li>
     <li>
      <a href="#quellen">Quellen</a>
    </li>
  </ol>



<!-- Kurszusammenfassung -->
## Kurszusammenfassung

Alle reden über “Maschinelles Lernen”, "Neuronale Netze", "Künstliche Intelligenz" und "Deep Learning - doch wie diese Techniken genau in der Praxis funktionieren und eingesetzt werden, erfahren Sie in diesem weiterführenden openHPI Kurs.

In diesem vierwöchigen Gratis-Kurs können Jugendliche und andere Interessierte ohne Programmier-Erfahrung und technisches Hintergrundwissen lernen, wie Machine Learning Projekte in der Praxis umgesetzt werden können. Wir wollen dabei das Basiswissen aus dem Kurs “Künstliche Intelligenz und Maschinelles Lernen für Einsteiger” weiter vertiefen und Ihnen ein Gefühl für die Chancen und Herausforderungen von Machine Learning Projekten in der Praxis vermitteln. Dafür betrachten wir mehrere konkrete Anwendungsfälle - unter anderem die Erkennung von Gebärdensprache aus Bildern und die Stimmungsanalyse von Zeitungsartikeln. Geleitet wird der Kurs von den Masterstudenten Johannes Hötter und Christian Warmuth.

Dieses Repository beinhaltet die Begleit-Materialien zum Online-Kurs auf openHPI in Form von Jupyter Notebooks und Google Colab Notebooks.

<!-- installation -->
## Installation

Nur notwendig bei lokaler Ausführung der Notebooks - siehe Hinweis weiter unten. Vorraussetzung unter anderem die Installation von Python. Für die Ausführung der Notebooks ohne Setup-Aufwand, können Sie diese als Google Colab ausführen (siehe unten).

1. Klone das Repo
   ```sh
   git clone https://github.com/christianwarmuth/openhpi-kipraxis
   
   cd openhpi-kipraxis
   ```
2. Installiere Packages
   ```sh
   pip install -r requirements.txt
   ```
3. (optional) Installiere seperaten Kernel 
   ```
   python3 -m ipykernel install --name ki-praxis 
   ```
   
<!-- hinweise -->
## Hinweise zur Ausführung mit Google Colab

Für alle Notebooks gilt: Will man diese ausführen, so öffnet man die Notebooks in GitHub direkt (per Click auf den Namen). Im Notebook erscheint oben ein Button "Open in Colab", den man klicken muss. 

## Hinweise zur Ausführung mit Jupyter Notebooks/Jupyter Lab

Man kann die im Github befindlichen Notebooks auch lokal ausführen. Hierfür folgen Sie bitte dem Installationsskript. Hinweise zur Ausführung von Jupyter Notebooks/Jupyter Lab findet sich [hier](https://jupyter.org/install).


**Hinweise zu Woche 2 und 4**:

Für Woche 1 und 3 können wir die Daten direkt hier im Repository zur Verfügung stellen bzw. direkt beziehen. 
Für Woche 2 und Woche 4 haben wir Datensätze von Kaggle verwendet und dürfen diese leider nicht selbst zur Verfügung stellen. Hierzu muss man sich zuerst bei Kaggle einen Account anlegen und anschließend den eigenen Username und Token herausfinden. Siehe https://www.kaggle.com/docs/api oder https://github.com/Kaggle/kaggle-api. 
Gibt man diesen Username und Token dann am Anfang des Google Colab Notebooks an, so kann man auch diesen Code ausführen. 

**Hinweis zu Exkurs Reinforcement Learning in Woche 1:**
Die gezeigten Inhalte im Exkurs Reinforcement Learning kann man leider nicht in Google Colab ausführen, da man hierfür eine OpenAI Gym Environment benötigt, die lokal installiert werden muss. 

Folge den Installationsskripten von https://github.com/Kautenja/gym-super-mario-bros und https://github.com/Kautenja/nes-py um den Exkurs lokal ausführen zu können.


<!-- Quellen -->
## Quellen

**Woche 1:**
  - Hauspreisvorhersage: ursprünglich aus dem [buchbegleitenden Repository](https://github.com/ageron/handson-ml2) von Aurélien Géron, leicht angepasst
  - Exkurs Reinforcement Learning: Basiert auf [MadMario](https://github.com/YuansongFeng/MadMario) und einem [Pytorch Tutorial](https://pytorch.org/tutorials/intermediate/mario_rl_tutorial.html). [Super Mario Bros. Environment](https://github.com/Kautenja/gym-super-mario-bros) für OpenAI Gym

**Woche 2:**
  - Recommender Systems 2: Model von [Morrisb](https://www.kaggle.com/morrisb/how-to-recommend-anything-deep-recommender)



    