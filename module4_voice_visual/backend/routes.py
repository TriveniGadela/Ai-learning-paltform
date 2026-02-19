from flask import Blueprint, render_template, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from shared.database.models import Topic

module4_bp = Blueprint('module4', __name__)

@module4_bp.route('/text-to-speech/<int:topic_id>')
@login_required
def text_to_speech(topic_id):
    topic = Topic.query.get_or_404(topic_id)
    if topic.user_id != current_user.id:
        flash('Access denied')
        return redirect(url_for('module1.dashboard'))
    return render_template('module4_voice_visual/frontend/audio_player.html', topic=topic)

@module4_bp.route('/api/synthesize/<int:topic_id>')
@login_required
def synthesize_speech(topic_id):
    topic = Topic.query.get_or_404(topic_id)
    if topic.user_id != current_user.id:
        return jsonify({'error': 'Access denied'}), 403
    
    # In production, integrate with AWS Polly or similar TTS service
    # For now, return text for browser's Web Speech API
    return jsonify({
        'text': topic.explanation,
        'topic': topic.topic_name
    })
