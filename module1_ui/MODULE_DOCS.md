# Module 1: User Interface (UI Module)

## Purpose
Handle all UI pages, navigation, and user authentication.

## Structure
```
module1_ui/
├── frontend/
│   ├── base.html       # Base template with navigation
│   ├── home.html       # Landing page
│   ├── login.html      # Login form
│   ├── register.html   # Registration form
│   └── dashboard.html  # User dashboard
└── backend/
    └── routes.py       # Flask routes for UI
```

## Routes

### GET /
- **Purpose**: Display home page
- **Template**: home.html
- **Auth**: Not required

### GET/POST /login
- **Purpose**: User login
- **Template**: login.html
- **Auth**: Not required
- **POST Data**: username, password

### GET/POST /register
- **Purpose**: User registration
- **Template**: register.html
- **Auth**: Not required
- **POST Data**: username, email, password, academic_level

### GET /dashboard
- **Purpose**: User dashboard
- **Template**: dashboard.html
- **Auth**: Required

### GET /logout
- **Purpose**: Logout user
- **Auth**: Required
- **Redirect**: Home page

## Features

1. **Session Management**: Flask-Login integration
2. **Navigation**: Dynamic nav based on auth status
3. **Flash Messages**: User feedback system
4. **Responsive Design**: Mobile-friendly CSS

## Dependencies
- Flask
- Flask-Login
- Jinja2 templates

## Integration Points
- Uses User model from shared/database/models.py
- Links to Module 2 (profile, history)
- Links to Module 3 (AI explanations)
- Links to Module 5 (reminders)
