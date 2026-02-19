"""
Test script to verify the platform setup
Run: python test_setup.py
"""

def test_imports():
    """Test if all required packages are installed"""
    print("Testing imports...")
    try:
        import flask
        print("✓ Flask installed")
        import flask_sqlalchemy
        print("✓ Flask-SQLAlchemy installed")
        import flask_login
        print("✓ Flask-Login installed")
        import boto3
        print("✓ Boto3 installed")
        import dotenv
        print("✓ Python-dotenv installed")
        import apscheduler
        print("✓ APScheduler installed")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_structure():
    """Test if all module folders exist"""
    print("\nTesting folder structure...")
    import os
    
    folders = [
        'module1_ui/frontend',
        'module1_ui/backend',
        'module2_user_data/frontend',
        'module2_user_data/backend',
        'module3_ai_processing/frontend',
        'module3_ai_processing/backend',
        'module4_voice_visual/frontend',
        'module4_voice_visual/backend',
        'module5_reminders/frontend',
        'module5_reminders/backend',
        'shared/database',
        'shared/utils'
    ]
    
    all_exist = True
    for folder in folders:
        if os.path.exists(folder):
            print(f"✓ {folder}")
        else:
            print(f"✗ {folder} missing")
            all_exist = False
    
    return all_exist

def test_files():
    """Test if critical files exist"""
    print("\nTesting critical files...")
    import os
    
    files = [
        'app.py',
        'requirements.txt',
        'config.py',
        '.env.example',
        'shared/database/models.py',
        'shared/utils/bedrock_client.py',
        'module1_ui/backend/routes.py',
        'module1_ui/frontend/base.html'
    ]
    
    all_exist = True
    for file in files:
        if os.path.exists(file):
            print(f"✓ {file}")
        else:
            print(f"✗ {file} missing")
            all_exist = False
    
    return all_exist

def main():
    print("=" * 50)
    print("AI Learning Platform - Setup Verification")
    print("=" * 50)
    
    imports_ok = test_imports()
    structure_ok = test_structure()
    files_ok = test_files()
    
    print("\n" + "=" * 50)
    if imports_ok and structure_ok and files_ok:
        print("✓ All tests passed! Ready to run the application.")
        print("\nNext steps:")
        print("1. Copy .env.example to .env")
        print("2. Configure your AWS credentials in .env")
        print("3. Run: python app.py")
    else:
        print("✗ Some tests failed. Please check the errors above.")
    print("=" * 50)

if __name__ == '__main__':
    main()
