from itsdangerous import URLSafeTimedSerializer
from app import app

serializer = URLSafeTimedSerializer(app.config["SECRET_KEY"])s
