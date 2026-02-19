from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from shared.database.models import User, Topic
from shared.database.db_init import db

module2_bp = Blueprint('module2', __name__)

@module2_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        academic_level = request.form.get('academic_level')
        current_user.academic_level = academic_level
        db.session.commit()
        flash('Profile updated successfully')
        return redirect(url_for('module2.profile'))
    return render_template('module2_user_data/frontend/profile.html')

@module2_bp.route('/topic-history')
@login_required
def topic_history():
    topics = Topic.query.filter_by(user_id=current_user.id).order_by(Topic.created_at.desc()).all()
    return render_template('module2_user_data/frontend/topic_history.html', topics=topics)

@module2_bp.route('/topic/<int:topic_id>')
@login_required
def view_topic(topic_id):
    topic = Topic.query.get_or_404(topic_id)
    if topic.user_id != current_user.id:
        flash('Access denied')
        return redirect(url_for('module2.topic_history'))
    return render_template('module2_user_data/frontend/view_topic.html', topic=topic)
