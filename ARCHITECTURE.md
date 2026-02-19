# System Architecture Diagram

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        USER BROWSER                          │
│                     (HTML/CSS/JavaScript)                    │
└────────────────────────┬────────────────────────────────────┘
                         │
                         │ HTTP Requests
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                      FLASK APPLICATION                       │
│                         (app.py)                             │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Module 1   │  │   Module 2   │  │   Module 3   │      │
│  │  UI & Auth   │  │  User Data   │  │ AI Process   │      │
│  │              │  │              │  │              │      │
│  │ - Home       │  │ - Profile    │  │ - Generate   │      │
│  │ - Login      │  │ - History    │  │ - Explain    │      │
│  │ - Register   │  │ - Topics     │  │ - Bedrock    │      │
│  │ - Dashboard  │  │              │  │              │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│                                                               │
│  ┌──────────────┐  ┌──────────────┐                         │
│  │   Module 4   │  │   Module 5   │                         │
│  │Voice/Visual  │  │  Reminders   │                         │
│  │              │  │              │                         │
│  │ - TTS        │  │ - Schedule   │                         │
│  │ - Audio      │  │ - Notify     │                         │
│  │ - Player     │  │ - Manage     │                         │
│  └──────────────┘  └──────────────┘                         │
│                                                               │
└───────────┬─────────────────────────┬───────────────────────┘
            │                         │
            │                         │
            ▼                         ▼
┌─────────────────────┐   ┌─────────────────────────┐
│   SQLite Database   │   │    Amazon Bedrock       │
│                     │   │    (Claude AI)          │
│ - Users             │   │                         │
│ - Topics            │   │ - Text Generation       │
│ - Reminders         │   │ - Prompt Engineering    │
└─────────────────────┘   └─────────────────────────┘
```

## Data Flow Diagram

### User Registration Flow
```
User → Register Form → Module 1 Backend → Hash Password → 
Database (User Table) → Login Session → Dashboard
```

### AI Explanation Generation Flow
```
User Input (Topic) → Module 3 Backend → 
Prompt Engineering (Academic Level) → 
Amazon Bedrock API → 
AI Response → 
Format & Store (Topic Table) → 
Display to User (Module 3 Frontend)
```

### Audio Learning Flow
```
Topic Explanation → Module 4 Backend → 
Text Extraction → Web Speech API → 
Audio Playback (Browser) → User Listens
```

### Reminder Flow
```
User Creates Reminder → Module 5 Backend → 
Store in Database → Background Scheduler (APScheduler) → 
Check Every 5 Minutes → Send Notification → 
Mark as Sent
```

## Module Interaction Map

```
┌─────────────────────────────────────────────────────────┐
│                    Module 1 (UI Core)                    │
│              Provides: Navigation, Auth, Base            │
└───┬─────────────────────────────────────────────────┬───┘
    │                                                 │
    │ Uses Auth                                       │ Uses Auth
    ▼                                                 ▼
┌─────────────────────┐                   ┌─────────────────────┐
│    Module 2         │                   │    Module 3         │
│  (User & Topics)    │◄──────────────────│  (AI Processing)    │
│                     │  Stores Topics    │                     │
└──────────┬──────────┘                   └──────────┬──────────┘
           │                                         │
           │ Provides Topic Data                    │ Provides Topic Data
           │                                         │
           ▼                                         ▼
┌─────────────────────┐                   ┌─────────────────────┐
│    Module 4         │                   │    Module 5         │
│ (Voice & Visual)    │                   │   (Reminders)       │
└─────────────────────┘                   └─────────────────────┘
```

## Database Relationships

```
┌──────────────────┐
│      User        │
│ ─────────────────│
│ id (PK)          │
│ username         │
│ email            │
│ password_hash    │
│ academic_level   │
└────────┬─────────┘
         │
         │ 1:N
         │
    ┌────┴────┬──────────────┐
    │         │              │
    ▼         ▼              ▼
┌─────────┐ ┌─────────┐ ┌──────────┐
│  Topic  │ │Reminder │ │ (Future) │
│─────────│ │─────────│ │──────────│
│id (PK)  │ │id (PK)  │ │  Quiz    │
│user_id  │ │user_id  │ │  Notes   │
│topic    │ │message  │ │  etc.    │
│explain  │ │schedule │ │          │
└─────────┘ └─────────┘ └──────────┘
```

## Request/Response Cycle

```
1. Browser Request
   ↓
2. Flask Router (app.py)
   ↓
3. Blueprint Route (moduleX/backend/routes.py)
   ↓
4. Business Logic
   ├─→ Database Query (SQLAlchemy)
   ├─→ AI Processing (Bedrock)
   └─→ Data Processing
   ↓
5. Template Rendering (Jinja2)
   ↓
6. HTML Response
   ↓
7. Browser Display
```

## Security Layers

```
┌─────────────────────────────────────┐
│         User Request                │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│    Flask Session Validation         │
│    (Flask-Login)                    │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│    Route Protection                 │
│    (@login_required)                │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│    User Authorization               │
│    (Check user_id matches)          │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│    Database Access                  │
│    (SQLAlchemy ORM)                 │
└─────────────────────────────────────┘
```

## Deployment Architecture (Production)

```
┌─────────────────────────────────────────────────────┐
│                   Load Balancer                      │
└────────────┬────────────────────────────────────────┘
             │
    ┌────────┴────────┐
    │                 │
    ▼                 ▼
┌─────────┐      ┌─────────┐
│ Flask   │      │ Flask   │
│ App 1   │      │ App 2   │
└────┬────┘      └────┬────┘
     │                │
     └────────┬───────┘
              │
              ▼
     ┌────────────────┐
     │   PostgreSQL   │
     │   Database     │
     └────────────────┘
              │
              ▼
     ┌────────────────┐
     │  Redis Cache   │
     │  (Sessions)    │
     └────────────────┘

External Services:
├─→ Amazon Bedrock (AI)
├─→ AWS SES (Email)
└─→ CloudWatch (Monitoring)
```

## File Structure Tree

```
hanu/
├── app.py                          # Main application
├── config.py                       # Configuration
├── requirements.txt                # Dependencies
├── .env.example                    # Environment template
├── .gitignore                      # Git ignore rules
├── README.md                       # Documentation
├── QUICKSTART.md                   # Quick start guide
├── PROJECT_OVERVIEW.md             # Detailed overview
├── test_setup.py                   # Setup verification
│
├── module1_ui/                     # UI & Authentication
│   ├── frontend/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── dashboard.html
│   ├── backend/
│   │   └── routes.py
│   └── MODULE_DOCS.md
│
├── module2_user_data/              # User & Topic Management
│   ├── frontend/
│   │   ├── profile.html
│   │   ├── topic_history.html
│   │   └── view_topic.html
│   └── backend/
│       └── routes.py
│
├── module3_ai_processing/          # AI Text Generation
│   ├── frontend/
│   │   └── explanation.html
│   └── backend/
│       └── routes.py
│
├── module4_voice_visual/           # Audio & Visual Learning
│   ├── frontend/
│   │   └── audio_player.html
│   └── backend/
│       └── routes.py
│
├── module5_reminders/              # Reminders & Notifications
│   ├── frontend/
│   │   └── reminders.html
│   └── backend/
│       └── routes.py
│
└── shared/                         # Shared Resources
    ├── __init__.py
    ├── database/
    │   ├── __init__.py
    │   └── models.py               # SQLAlchemy models
    └── utils/
        ├── __init__.py
        ├── bedrock_client.py       # AWS Bedrock integration
        └── scheduler.py            # Background scheduler
```
