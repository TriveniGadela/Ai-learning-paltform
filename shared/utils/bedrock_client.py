import boto3
import json
import os
from dotenv import load_dotenv

load_dotenv()

def get_bedrock_client():
    return boto3.client(
        service_name='bedrock-runtime',
        region_name=os.getenv('AWS_REGION', 'us-east-1'),
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
    )

def get_prompt_for_level(topic, academic_level):
    level_prompts = {
        'elementary': f'Explain {topic} in very simple terms for an elementary school student. Use easy words and fun examples.',
        'middle_school': f'Explain {topic} for a middle school student. Use clear language and relatable examples.',
        'high_school': f'Explain {topic} for a high school student. Include key concepts and some technical details.',
        'undergraduate': f'Explain {topic} for an undergraduate student. Include detailed concepts, theories, and applications.',
        'graduate': f'Explain {topic} at a graduate level. Include advanced concepts, research perspectives, and critical analysis.'
    }
    return level_prompts.get(academic_level, level_prompts['high_school'])

def generate_explanation(topic, academic_level):
    try:
        client = get_bedrock_client()
        prompt = get_prompt_for_level(topic, academic_level)
        
        body = json.dumps({
            "prompt": f"\n\nHuman: {prompt}\n\nAssistant:",
            "max_tokens_to_sample": 1000,
            "temperature": 0.7,
            "top_p": 0.9,
        })
        
        response = client.invoke_model(
            modelId=os.getenv('BEDROCK_MODEL_ID', 'anthropic.claude-v2'),
            body=body
        )
        
        response_body = json.loads(response['body'].read())
        explanation = response_body.get('completion', '').strip()
        
        return explanation
    except Exception as e:
        # Fallback explanation if Bedrock is not configured
        return f"""<p><strong>Note:</strong> Amazon Bedrock is not configured. This is a sample explanation.</p>
        <p><strong>{topic}</strong> is an important concept in science and education. 
        To get AI-powered personalized explanations, please configure your AWS credentials and Bedrock access.</p>
        <p>Academic Level: {academic_level.replace('_', ' ').title()}</p>
        <p><em>Error: {str(e)}</em></p>"""
