from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from shared.database.models import Topic
from shared.utils.bedrock_client import generate_explanation as get_ai_explanation
from shared.database.db_init import db

module3_bp = Blueprint('module3', __name__)

@module3_bp.route('/generate-explanation', methods=['POST'])
@login_required
def generate_explanation():
    topic_name = request.form.get('topic')
    if not topic_name:
        flash('Please enter a topic')
        return redirect(url_for('module1.dashboard'))
    
    # Generate AI explanation
    explanation = get_ai_explanation(topic_name, current_user.academic_level)
    
    # Save to database
    topic = Topic(
        user_id=current_user.id,
        topic_name=topic_name,
        explanation=explanation,
        academic_level=current_user.academic_level
    )
    db.session.add(topic)
    db.session.commit()
    
    return render_template('module3_ai_processing/frontend/explanation.html', 
                         topic=topic)

@module3_bp.route('/explanation/<int:topic_id>')
@login_required
def view_explanation(topic_id):
    topic = Topic.query.get_or_404(topic_id)
    if topic.user_id != current_user.id:
        flash('Access denied')
        return redirect(url_for('module1.dashboard'))
    return render_template('module3_ai_processing/frontend/explanation.html', topic=topic)
