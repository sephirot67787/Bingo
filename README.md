 🎉 Bingo Web Multiplayer 🃏

Benvenuto nel progetto **Bingo Web Multiplayer**, una web application sviluppata con **Python** e **FastAPI** che permette a più giocatori di partecipare a una partita di Bingo **in tempo reale** tramite browser 🌐⚡  
Welcome to the **Bingo Web Multiplayer** project, a web application developed with **Python** and **FastAPI** that allows multiple players to join a **real-time Bingo game** via browser 🌐⚡

Questo progetto è stato realizzato come **Winter Break Project 2026**, con l’obiettivo di simulare un vero progetto di sviluppo software moderno.  
This project was created as a **Winter Break Project 2026**, aiming to simulate a real modern software development project.

---

## ❄️ Descrizione del progetto / Project Description

Bingo Web Multiplayer è un gioco online multiplayer che consente a più utenti di:  
Bingo Web Multiplayer is an online multiplayer game that allows users to:

- entrare in una stanza virtuale 🏠 / join a virtual room 🏠  
- scegliere un nickname 🧑‍💻 / choose a nickname 🧑‍💻  
- ricevere una cartella Bingo generata casualmente 🎫 / receive a randomly generated Bingo card 🎫  
- visualizzare l’estrazione dei numeri in tempo reale 🔢 / see numbers drawn in real time 🔢  
- dichiarare il vincitore quando viene fatto Bingo 🏆 / declare the winner when Bingo is achieved 🏆  

La comunicazione tra server e client avviene tramite **WebSocket**, garantendo aggiornamenti immediati per tutti i giocatori.  
Server-client communication is handled via **WebSockets**, ensuring instant updates for all players.

---

## 🚀 Tecnologie utilizzate / Technologies Used

- 🐍 Python  
- ⚡ FastAPI  
- 🔌 WebSocket  
- 🌐 HTML  
- 🎨 CSS  
- 📜 JavaScript  
- 🐙 Git & GitHub  

---

## 🏗️ Struttura del progetto / Project Structure

main.py
app/
├─ routers/
│ └─ bingo.py # Logica del gioco e WebSocket / Game logic and WebSocket
├─ static/ # File CSS e risorse statiche / CSS and static resources
└─ templates/
└─ index.html # Interfaccia web del gioco / Game web interface

yaml
Copia codice

- `main.py`: avvia l’app FastAPI e collega i componenti / starts FastAPI and connects components  
- `bingo.py`: gestisce stanze, giocatori, numeri estratti e vincitore / manages rooms, players, drawn numbers, and winner  
- `index.html`: interfaccia utente con cartella, pulsanti e numeri estratti / user interface with card, buttons, and drawn numbers  

---

## 🎮 Funzionalità principali / Main Features

- ✅ Multiplayer in tempo reale / Real-time multiplayer  
- ✅ Generazione casuale delle cartelle Bingo / Randomly generated Bingo cards  
- ✅ Estrazione numeri condivisa / Shared number extraction  
- ✅ Evidenziazione automatica dei numeri estratti / Automatic highlighting of drawn numbers  
- ✅ Gestione nickname univoci / Unique nickname management  
- ✅ Dichiarazione del vincitore in tempo reale / Real-time winner declaration  

---

## 👥 Team di sviluppo – *Tacos* 🌮 / Development Team – *Tacos* 🌮

Il progetto è stato realizzato da un team di 5 studenti / The project was developed by a team of 5 students:

- Michele – Capogruppo / Team Leader  
- Gennaro – Ricerca e documentazione / Research and documentation  
- Pio – Testing e verifica funzionalità / Testing and functionality check  
- Johanna – Frontend e interfaccia grafica / Frontend and graphical interface  
- Petillo – Backend e logica di gioco / Backend and game logic  

📍 Luogo incontri: Casa del capogruppo / Meeting location: Team leader’s house  
⏱️ Tempo complessivo: circa 9 ore / Total time spent: about 9 hours  

Durante gli incontri ogni membro aveva un **portatile personale** 💻 e ascoltava **musica scelta a rotazione** 🎶 mentre condividevamo **tacos** 🌮, simbolo del gruppo e del nome del team.  
During meetings, each member had a **personal laptop** 💻 and listened to **music rotated by each member** 🎶 while sharing **tacos** 🌮, which are also the team’s name.

---

## 🤖 Utilizzo dell’Intelligenza Artificiale / Use of Artificial Intelligence

L’AI è stata utilizzata come **strumento di supporto** / AI was used as a **support tool**, per:  

- comprendere meglio Python e FastAPI / better understand Python and FastAPI  
- migliorare e correggere il codice / improve and correct code  
- chiarire la logica del gioco / clarify game logic  
- supportare la scrittura della documentazione e della presentazione / assist with writing documentation and presentation  

L’AI è stata usata come **aiuto all’apprendimento**, non come sostituzione del lavoro del team / AI was used as a **learning aid**, not as a replacement for team work.

---

## 💡 Idee scartate / Ideas Considered but Not Implemented

- Chat in tempo reale tra i giocatori 💬 / Real-time chat between players 💬  
- Cartelle Bingo personalizzabili 🎫 / Customizable Bingo cards 🎫  
- Matchmaking automatico per stanze pubbliche 🏟️ / Automatic matchmaking for public rooms 🏟️  
- Controllo automatico del Bingo lato server 🤖 / Automatic server-side Bingo checking 🤖  
- Animazioni e suoni avanzati 🔊✨ / Advanced animations and sounds 🔊✨  

Queste funzionalità potranno essere implementate in versioni future / These features may be implemented in future versions.

---

## 🛠️ Come avviare il progetto / How to Run the Project

1. Clona il repository / Clone the repository:
git clone https://github.com/tuo-username/bingo-web-multiplayer.git

markdown
Copia codice

2. Installa le dipendenze / Install dependencies:
pip install fastapi uvicorn

markdown
Copia codice

3. Avvia il server / Run the server:
uvicorn main:app --reload

r
Copia codice

4. Apri il browser / Open the browser:
http://localhost:8000/play

yaml
Copia codice

---

## 📈 Conclusioni / Conclusions

Bingo Web Multiplayer rappresenta una **simulazione reale di sviluppo software moderno** / Bingo Web Multiplayer represents a **realistic simulation of modern software development**, combinando backend, frontend, comunicazione real-time e lavoro di squadra / combining backend, frontend, real-time communication, and teamwork.  
Il progetto ha permesso di sviluppare competenze tecniche, organizzative e collaborative in un contesto pratico e stimolante / The project allowed the team to develop technical, organizational, and collaborative skills in a practical and engaging context.

---

## 📜 Licenza / License

Progetto a scopo didattico 🎓 / Educational project 🎓  
Utilizzabile per studio e apprendimento / Free to use for study and learning purposes

---

🌮 **Team Tacos – Winter Break Project 2026** ❄️🐍
