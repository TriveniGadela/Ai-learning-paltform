# Quick Start Guide

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment
Create a `.env` file from the template:
```bash
copy .env.example .env
```

Edit `.env` with your AWS credentials:
```
SECRET_KEY=your-random-secret-key
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
BEDROCK_MODEL_ID=anthropic.claude-v2
```

### 3. Run the Application
```bash
python app.py
```

The application will:
- Create the SQLite database automatically
- Start on http://localhost:5000
- Initialize all 5 modules

### 4. First Steps

1. **Register**: Go to http://localhost:5000 and click "Register"
2. **Select Academic Level**: Choose your education level
3. **Ask a Question**: Enter a topic on the dashboard
4. **Get AI Explanation**: Receive personalized explanation
5. **Listen**: Use text-to-speech feature
6. **Set Reminders**: Create learning reminders

## Module Overview

### Module 1: UI (Port: All pages)
- Home: `/`
- Login: `/login`
- Register: `/register`
- Dashboard: `/dashboard`

### Module 2: User Data
- Profile: `/profile`
- History: `/topic-history`
- View Topic: `/topic/<id>`

### Module 3: AI Processing
- Generate: `/generate-explanation` (POST)
- View: `/explanation/<id>`

### Module 4: Voice & Visual
- Audio Player: `/text-to-speech/<id>`
- API: `/api/synthesize/<id>`

### Module 5: Reminders
- List: `/reminders`
- Add: `/add-reminder` (POST)
- Delete: `/delete-reminder/<id>`

## Testing Without AWS

The platform works without AWS Bedrock configured:
- Sample explanations will be shown
- All other features work normally
- Configure AWS later for AI-powered explanations

## Troubleshooting

### Database Issues
Delete `learning_platform.db` and restart the app to recreate.

### Import Errors
Ensure you're in the project root directory when running `python app.py`.

### AWS Bedrock Access
Request model access in AWS Console > Bedrock > Model Access.

## Default Academic Levels

- elementary
- middle_school
- high_school (default)
- undergraduate
- graduate
