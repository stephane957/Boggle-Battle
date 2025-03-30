# Boggle Battle 🎲🔠

[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://reactjs.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)

A real-time 1v1 Boggle word game with simple matchmaking and scoring system.

**Frontend**: React + CSS Modules (Lightweight implementation)  
**Backend**: Flask + SQLAlchemy  
**Database**: SQLite (File-based development)

## Features ✨
- Real-time 1v1 gameplay
- 4x4 letter grid generation
- Word validation using dictionary
- Score tracking and timer
- Simple matchmaking system
- Responsive game board

## Local Setup 🛠️

### Prerequisites
- Node.js v16+
- Python 3.9+
- npm & pip

### Installation
1. Clone repository:
```
git clone https://github.com/yourusername/Boggle-Battle.git
cd Boggle-Battle
```
- Frontend
```
cd boggle-frontend
npm install
```
- Backend
```
cd boggle-backend
python -m venv venv
source venv\Scripts\activate  # Linux: venv/bin/activate
pip install -r requirements.txt
```

### Configuration ⚙️
- Backend (Flask): 
Create *boggle-backend/config.py*:
```
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///boggle.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```
- Frontend (React): 
Create *.env* file in root of the boggle-frontend directory:
```
REACT_APP_API_URL=http://localhost:5000
```
### Database Setup 💾
The SQLite database will be automatically created on first run. Initialize tables:
```
cd boggle-backend
flask shell
>>> from app import db
>>> db.create_all()
```

### Running Locally 🖥️
1. Start Backend
```
cd boggle-backend
flask run --port 5000
```
2. Start Frontend
```
cd boggle-frontend
npm start
Starts the development server.

npm run eject
Removes this tool and copies build dependencies, configuration files
and scripts into the app directory. If you do this, you can’t go back!
```
Access: http://localhost:3000

### Game Rules 📜
1. 3-minute rounds with 4x4 letter grid
2. Players find words with adjacent letters
3. Score based on word length:
      - 3-4 letters: 1 point
      - 5 letters: 2 points
      - 6+ letters: 3 points
4. Duplicate words between players cancel out
5. Highest score wins!

### Testing 🧪
Frontend
```
cd boggle-frontend
npm test
```
Backend
```
cd boggle-backend
pytest
```

### Troubleshooting 🔧
Common issues:
1. CORS errors: Ensure backend is running on port 5000
2. Database issues: Delete boggle.db and re-run db.create_all()
3. Stale data: Hard refresh browser (Ctrl+Shift+R)
4. Missing dependencies: Re-run npm install/pip install

# Ready to Play?
Start both servers and visit http://localhost:3000 to begin your word battle!
