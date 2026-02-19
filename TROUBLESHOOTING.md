# Troubleshooting Guide

## Common Issues and Solutions

### 1. Import Errors

#### Problem: `ModuleNotFoundError: No module named 'flask'`
**Solution:**
```bash
pip install -r requirements.txt
```

#### Problem: `ImportError: cannot import name 'db' from 'app'`
**Solution:**
- Ensure you're running from the project root directory
- Check that all `__init__.py` files exist in shared folders

---

### 2. Database Issues

#### Problem: `OperationalError: no such table: user`
**Solution:**
```bash
# Delete the database and restart
del learning_platform.db
python app.py
```

#### Problem: `IntegrityError: UNIQUE constraint failed`
**Solution:**
- Username or email already exists
- Try a different username/email
- Or reset the database (see above)

---

### 3. AWS Bedrock Issues

#### Problem: `ClientError: Could not connect to the endpoint URL`
**Solution:**
1. Check AWS credentials in `.env`:
   ```
   AWS_ACCESS_KEY_ID=your-key
   AWS_SECRET_ACCESS_KEY=your-secret
   AWS_REGION=us-east-1
   ```
2. Verify AWS credentials are valid
3. Check internet connection

#### Problem: `AccessDeniedException: User is not authorized`
**Solution:**
1. Go to AWS Console → Bedrock → Model Access
2. Request access to Claude models
3. Wait for approval (usually instant)
4. Ensure IAM user has Bedrock permissions

#### Problem: AI explanations show fallback message
**Solution:**
- This is expected if AWS is not configured
- Platform works with sample explanations
- Configure AWS credentials to enable AI features

---

### 4. Login/Authentication Issues

#### Problem: Can't login after registration
**Solution:**
- Check username and password are correct
- Ensure cookies are enabled in browser
- Try clearing browser cache

#### Problem: `Unauthorized` error on protected pages
**Solution:**
- Login first before accessing dashboard
- Check if session expired (login again)
- Ensure SECRET_KEY is set in `.env`

---

### 5. Template Not Found Errors

#### Problem: `TemplateNotFound: module1_ui/frontend/base.html`
**Solution:**
```python
# In app.py, ensure template_folder is set correctly:
app = Flask(__name__, template_folder='.')
```

#### Problem: CSS not loading
**Solution:**
- CSS is inline in templates (no external files needed)
- Check browser console for errors
- Hard refresh: Ctrl+F5 (Windows) or Cmd+Shift+R (Mac)

---

### 6. Text-to-Speech Issues

#### Problem: Audio doesn't play
**Solution:**
- Ensure browser supports Web Speech API (Chrome, Edge, Safari)
- Check browser permissions for audio
- Try a different browser

#### Problem: Voice sounds robotic
**Solution:**
- This is expected with Web Speech API
- For better quality, integrate AWS Polly (future enhancement)

---

### 7. Reminder Issues

#### Problem: Reminders not being sent
**Solution:**
- Scheduler runs every 5 minutes
- Check reminder scheduled_time is in the future
- Restart app to restart scheduler
- Check console for scheduler logs

#### Problem: `APScheduler` import error
**Solution:**
```bash
pip install APScheduler==3.10.4
```

---

### 8. Port Already in Use

#### Problem: `OSError: [Errno 48] Address already in use`
**Solution:**

**Windows:**
```bash
# Find process using port 5000
netstat -ano | findstr :5000
# Kill the process (replace PID)
taskkill /PID <PID> /F
```

**Or change port in app.py:**
```python
app.run(debug=True, port=5001)
```

---

### 9. Environment Variable Issues

#### Problem: `.env` file not being read
**Solution:**
1. Ensure file is named `.env` (not `.env.txt`)
2. Place it in project root directory
3. Install python-dotenv:
   ```bash
   pip install python-dotenv
   ```

#### Problem: `SECRET_KEY` not set warning
**Solution:**
- Copy `.env.example` to `.env`
- Set a random secret key:
  ```
  SECRET_KEY=your-random-secret-key-here-change-this
  ```

---

### 10. Performance Issues

#### Problem: Slow AI response generation
**Solution:**
- This is normal for AI processing (5-10 seconds)
- Bedrock API call takes time
- Consider adding loading spinner (future enhancement)

#### Problem: Database queries slow
**Solution:**
- SQLite is fine for development
- For production, migrate to PostgreSQL
- Add database indexes if needed

---

## Verification Steps

### 1. Test Installation
```bash
python test_setup.py
```

### 2. Check Python Version
```bash
python --version
# Should be 3.8 or higher
```

### 3. Verify Dependencies
```bash
pip list | findstr flask
pip list | findstr boto3
pip list | findstr sqlalchemy
```

### 4. Test Database Connection
```python
python
>>> from app import db
>>> db.create_all()
>>> exit()
```

### 5. Test AWS Connection
```python
python
>>> import boto3
>>> client = boto3.client('bedrock-runtime', region_name='us-east-1')
>>> print("AWS connection OK")
>>> exit()
```

---

## Debug Mode

### Enable Detailed Logging

Add to `app.py`:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Check Flask Debug Output
- Debug mode is enabled by default in development
- Check terminal for detailed error messages
- Look for stack traces

---

## Getting Help

### 1. Check Documentation
- README.md - Main documentation
- QUICKSTART.md - Setup guide
- PROJECT_OVERVIEW.md - Technical details
- ARCHITECTURE.md - System design

### 2. Check Logs
- Terminal output shows Flask logs
- Database errors appear in console
- AWS errors show in terminal

### 3. Common Error Messages

| Error | Likely Cause | Solution |
|-------|--------------|----------|
| 404 Not Found | Wrong URL | Check route spelling |
| 500 Internal Server Error | Code error | Check terminal logs |
| 401 Unauthorized | Not logged in | Login first |
| 403 Forbidden | Wrong user | Check user_id |
| Connection refused | App not running | Start app.py |

---

## Reset Everything

If all else fails, start fresh:

```bash
# 1. Delete database
del learning_platform.db

# 2. Delete Python cache
rmdir /s /q __pycache__
rmdir /s /q shared\__pycache__

# 3. Reinstall dependencies
pip uninstall -r requirements.txt -y
pip install -r requirements.txt

# 4. Restart application
python app.py
```

---

## Platform-Specific Issues

### Windows
- Use `\` for paths (handled automatically)
- Use `del` instead of `rm`
- Use `copy` instead of `cp`

### Mac/Linux
- Use `/` for paths
- Use `rm` for delete
- Use `cp` for copy
- May need `python3` instead of `python`

---

## Browser Compatibility

### Recommended Browsers
- ✅ Chrome (latest)
- ✅ Edge (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)

### Known Issues
- IE 11: Not supported (use modern browser)
- Old browsers: Web Speech API may not work

---

## Production Deployment Issues

### Issue: Debug mode in production
**Solution:**
```python
# In app.py
if __name__ == '__main__':
    app.run(debug=False)  # Set to False
```

### Issue: Database not persistent
**Solution:**
- Use PostgreSQL or MySQL instead of SQLite
- Update DATABASE_URI in `.env`

### Issue: Secret key exposed
**Solution:**
- Never commit `.env` to git
- Use environment variables on server
- Generate strong random key

---

## Still Having Issues?

1. Run the verification script:
   ```bash
   python test_setup.py
   ```

2. Check all files exist:
   ```bash
   dir /s /b *.py
   dir /s /b *.html
   ```

3. Verify folder structure matches documentation

4. Review error messages carefully

5. Check that you're in the correct directory

---

**Remember**: Most issues are due to:
- Missing dependencies
- Wrong directory
- AWS not configured (expected)
- Database needs reset

The platform works without AWS - you'll just see sample explanations instead of AI-generated ones.
