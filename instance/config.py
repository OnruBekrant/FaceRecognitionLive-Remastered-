import os

# Bu dosya instance klasöründe olmalı (Flask otomatik algılar)
SECRET_KEY = os.getenv("SECRET_KEY", "devkey")
SQLALCHEMY_TRACK_MODIFICATIONS = False
