from itsdangerous.url_safe import URLSafeTimedSerializer
import os

SECRET_KEY = os.getenv("MY_SECRET")


def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(os.getenv('SECRET_KEY'))
    return serializer.dumps(email, salt=os.getenv('SECURITY_PASSWORD_SALT'))


def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(os.getenv('SECRET_KEY'))
    try:
        email = serializer.loads(
            token,
            salt=os.getenv('SECURITY_PASSWORD_SALT'),
            max_age=expiration
        )
    except:
        return False
    return email
