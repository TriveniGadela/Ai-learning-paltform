# AI-Powered Learning Platform - Project Overview

## 🎯 Project Goal
Build a modular, AI-powered learning platform that provides personalized educational content based on student academic level using Amazon Bedrock.

## 📊 Architecture Overview

### Modular Design
Each module is self-contained with separate frontend and backend folders:

```
Module Structure:
├── moduleX_name/
│   ├── frontend/          # HTML templates
│   │   └── *.html
│   └── backend/           # Python routes
│       └── routes.py
```

### Technology Stack
- **Backend Framework**: Flask (Python)
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask-Login
- **AI Service**: Amazon Bedrock (Claude v2)
- **Frontend**: HTML5, CSS3, JavaScript
- **Template Engine**: Jinja2
- **Scheduler**: APScheduler
- **Text-to-Speech**: Web Speech API

## 📦 Module Breakdown

### Module 1: User Interface (UI Module)
**Purpose**: Core navigation and authentication

**Frontend Components**:
- `base.html` - Master template with navigation
- `home.html` - Landing page
- `login.html` - Authentication form
- `register.html` - User registration
- `dashboard.html` - Main user interface

**Backend Features**:
- User authentication (login/logout)
- Session management
- Registration with academic level
- Route protection

**Key Routes**:
- `/` - Home
- `/login` - Login page
- `/register` - Registration
- `/dashboard` - User dashboard
- `/logout` - Logout

---

### Module 2: User Data & Topic Management
**Purpose**: Manage user profiles and learning history

**Frontend Components**:
- `profile.html` - User profile editor
- `topic_history.html` - List of learned topics
- `view_topic.html` - Individual topic details

**Backend Features**:
- Profile CRUD operations
- Academic level updates
- Topic history retrieval
- User-specific data filtering

**Key Routes**:
- `/profile` - View/edit profile
- `/topic-history` - View all topics
- `/topic/<id>` - View specific topic

**Database Models**:
- User (username, email, academic_level)
- Topic (topic_name, explanation, user_id)

---

### Module 3: AI Text Processing
**Purpose**: Generate personalized explanations using AI

**Frontend Components**:
- `explanation.html` - Display AI-generated content

**Backend Features**:
- Amazon Bedrock integration
- Prompt engineering per academic level
- Response formatting
- Topic storage

**Key Routes**:
- `/generate-explanation` (POST) - Create explanation
- `/explanation/<id>` - View explanation

**AI Integration**:
```python
Prompt Templates by Level:
- Elementary: Simple words, fun examples
- Middle School: Clear language, relatable
- High School: Key concepts, technical
- Undergraduate: Detailed theories
- Graduate: Advanced research perspective
```

**Bedrock Configuration**:
- Model: Claude v2 (anthropic.claude-v2)
- Max Tokens: 1000
- Temperature: 0.7
- Fallback: Sample explanations

---

### Module 4: Voice & Visual Learning
**Purpose**: Multi-modal learning with audio

**Frontend Components**:
- `audio_player.html` - Text-to-speech interface

**Backend Features**:
- Text-to-speech API endpoint
- Audio synthesis
- Playback controls

**Key Routes**:
- `/text-to-speech/<id>` - Audio player page
- `/api/synthesize/<id>` - TTS API

**Features**:
- Play/Pause/Stop controls
- Web Speech API integration
- Adjustable speech rate
- Visual feedback

---

### Module 5: Reminders & Notifications
**Purpose**: Learning consistency through reminders

**Frontend Components**:
- `reminders.html` - Reminder management interface

**Backend Features**:
- Reminder CRUD operations
- Scheduled notifications
- Background job processing
- Status tracking

**Key Routes**:
- `/reminders` - List reminders
- `/add-reminder` (POST) - Create reminder
- `/delete-reminder/<id>` - Remove reminder

**Scheduler**:
- Checks every 5 minutes
- Marks reminders as sent
- Extensible for email/push notifications

---

## 🗄️ Database Schema

### User Table
```sql
id              INTEGER PRIMARY KEY
username        VARCHAR(80) UNIQUE NOT NULL
email           VARCHAR(120) UNIQUE NOT NULL
password_hash   VARCHAR(200) NOT NULL
academic_level  VARCHAR(50) DEFAULT 'high_school'
created_at      DATETIME DEFAULT CURRENT_TIMESTAMP
```

### Topic Table
```sql
id              INTEGER PRIMARY KEY
user_id         INTEGER FOREIGN KEY -> User.id
topic_name      VARCHAR(200) NOT NULL
explanation     TEXT
academic_level  VARCHAR(50)
created_at      DATETIME DEFAULT CURRENT_TIMESTAMP
```

### Reminder Table
```sql
id              INTEGER PRIMARY KEY
user_id         INTEGER FOREIGN KEY -> User.id
message         VARCHAR(500)
scheduled_time  DATETIME
is_sent         BOOLEAN DEFAULT FALSE
created_at      DATETIME DEFAULT CURRENT_TIMESTAMP
```

## 🔐 Security Features

1. **Password Security**: Werkzeug password hashing
2. **Session Management**: Flask-Login with secure cookies
3. **Route Protection**: @login_required decorator
4. **CSRF Protection**: Flask built-in
5. **SQL Injection Prevention**: SQLAlchemy ORM
6. **Environment Variables**: Sensitive data in .env

## 🚀 Deployment Considerations

### Development
```bash
python app.py
# Runs on localhost:5000
# Debug mode enabled
# SQLite database
```

### Production Checklist
- [ ] Change SECRET_KEY
- [ ] Use production database (PostgreSQL/MySQL)
- [ ] Enable HTTPS
- [ ] Configure AWS credentials securely
- [ ] Set DEBUG=False
- [ ] Use production WSGI server (Gunicorn)
- [ ] Set up logging
- [ ] Configure email for reminders
- [ ] Enable CORS if needed
- [ ] Set up monitoring

## 📈 Scalability

### Current Architecture
- Single server
- SQLite database
- Synchronous processing

### Future Scaling Options
1. **Database**: Migrate to PostgreSQL/MySQL
2. **Caching**: Add Redis for sessions
3. **Queue**: Celery for async AI processing
4. **Load Balancing**: Multiple Flask instances
5. **CDN**: Static assets delivery
6. **Microservices**: Split modules into services

## 🔧 Customization Guide

### Adding New Academic Level
1. Update `config.py` ACADEMIC_LEVELS
2. Add prompt template in `bedrock_client.py`
3. Update frontend select options

### Adding New Module
1. Create `moduleX_name/` folder
2. Add `frontend/` and `backend/` subfolders
3. Create `routes.py` with Blueprint
4. Register blueprint in `app.py`
5. Add navigation links in `base.html`

### Changing AI Model
1. Update BEDROCK_MODEL_ID in `.env`
2. Adjust prompt format in `bedrock_client.py`
3. Test with different academic levels

## 📚 API Endpoints Summary

| Method | Endpoint | Module | Auth | Purpose |
|--------|----------|--------|------|---------|
| GET | / | 1 | No | Home page |
| GET/POST | /login | 1 | No | User login |
| GET/POST | /register | 1 | No | Registration |
| GET | /dashboard | 1 | Yes | Dashboard |
| GET | /logout | 1 | Yes | Logout |
| GET/POST | /profile | 2 | Yes | Profile management |
| GET | /topic-history | 2 | Yes | Topic list |
| GET | /topic/<id> | 2 | Yes | View topic |
| POST | /generate-explanation | 3 | Yes | AI generation |
| GET | /explanation/<id> | 3 | Yes | View explanation |
| GET | /text-to-speech/<id> | 4 | Yes | Audio player |
| GET | /api/synthesize/<id> | 4 | Yes | TTS API |
| GET | /reminders | 5 | Yes | List reminders |
| POST | /add-reminder | 5 | Yes | Create reminder |
| GET | /delete-reminder/<id> | 5 | Yes | Delete reminder |

## 🎓 User Flow

1. **Registration**: User signs up with academic level
2. **Login**: Authentication and session creation
3. **Dashboard**: Central hub with quick actions
4. **Topic Input**: User enters topic to learn
5. **AI Processing**: Bedrock generates explanation
6. **View Explanation**: Personalized content displayed
7. **Audio Learning**: Optional text-to-speech
8. **History**: Access past topics
9. **Reminders**: Set learning reminders
10. **Profile**: Update academic level anytime

## 🧪 Testing Strategy

### Manual Testing
- User registration and login
- Topic generation with different levels
- Audio playback functionality
- Reminder creation and scheduling
- Profile updates

### Automated Testing (Future)
- Unit tests for models
- Integration tests for routes
- API endpoint testing
- Database operations testing

## 📝 Development Workflow

1. **Setup**: Install dependencies, configure .env
2. **Database**: Auto-created on first run
3. **Development**: Modify modules independently
4. **Testing**: Use test_setup.py to verify
5. **Deployment**: Follow production checklist

## 🤝 Contributing Guidelines

1. Each module is independent
2. Follow existing code structure
3. Update module documentation
4. Test before committing
5. Use meaningful commit messages

## 📞 Support & Resources

- **Flask Docs**: https://flask.palletsprojects.com/
- **AWS Bedrock**: https://aws.amazon.com/bedrock/
- **SQLAlchemy**: https://www.sqlalchemy.org/
- **Bootstrap (optional)**: https://getbootstrap.com/

## 🎉 Success Metrics

- User registration and retention
- Topics generated per user
- Audio feature usage
- Reminder completion rate
- Academic level distribution
- AI explanation quality feedback

---

**Version**: 1.0.0  
**Last Updated**: 2024  
**Status**: Production Ready (with AWS configuration)
