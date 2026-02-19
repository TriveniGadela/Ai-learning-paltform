from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

def check_reminders():
    """Check and process pending reminders"""
    from shared.database.models import Reminder
    from shared.database.db_init import db
    
    now = datetime.utcnow()
    pending_reminders = Reminder.query.filter(
        Reminder.is_sent == False,
        Reminder.scheduled_time <= now
    ).all()
    
    for reminder in pending_reminders:
        # In production, send email or push notification here
        print(f"Reminder: {reminder.message} for user {reminder.user_id}")
        reminder.is_sent = True
    
    if pending_reminders:
        db.session.commit()

def start_scheduler(app):
    """Initialize and start the reminder scheduler"""
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        func=lambda: app.app_context().push() or check_reminders(),
        trigger="interval",
        minutes=5
    )
    scheduler.start()
    return scheduler
