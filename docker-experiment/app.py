from flask import Flask
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('experiment.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS visits 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                     timestamp TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    # Save visit
    conn = sqlite3.connect('experiment.db')
    conn.execute("INSERT INTO visits (timestamp) VALUES (?)", 
                 (datetime.now().strftime('%Y-%m-%d %H:%M:%S'),))
    conn.commit()
    
    # Get all visits
    visits = conn.execute('SELECT * FROM visits ORDER BY id DESC').fetchall()
    conn.close()
    
    html = "<h1>Docker SQLite Experiment</h1>"
    html += f"<p>Totaal bezoeken: {len(visits)}</p>"
    html += "<h2>Laatste 10 bezoeken:</h2><ul>"
    for visit in visits[:10]:
        html += f"<li>Bezoek #{visit[0]} om {visit[1]}</li>"
    html += "</ul>"
    
    return html

@app.route('/reset')
def reset():
    conn = sqlite3.connect('experiment.db')
    conn.execute('DELETE FROM visits')
    conn.commit()
    conn.close()
    return "Database gereset! <a href='/'>Terug</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
