from models.user import User
from app import db
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

@main.route('/recognize', methods=['POST'])
def recognize():
    if 'image' not in request.files:
        return "No image uploaded", 400

    image = request.files['image']
    from app.services.face_service import extract_embedding

    test_embedding = extract_embedding(image)
    if test_embedding is None:
        return "Yüz algılanamadı", 400

    # Veritabanındaki tüm kullanıcıları al
    users = User.query.all()
    if not users:
        return "Sistemde kayıtlı kişi yok", 404

    # Karşılaştırma
    best_match = None
    best_score = -1
    for user in users:
        known_embedding = np.array(user.face_encoding)
        score = cosine_similarity(
            [test_embedding],
            [known_embedding]
        )[0][0]

        if score > best_score:
            best_score = score
            best_match = user

    # Eşik değeri (0.5 düşük, 1.0 tam aynı)
    if best_score > 0.5:
        return render_template("result.html", name=best_match.name, score=round(best_score * 100, 2))
    else:
        return render_template("result.html", name="Tanınmadı", score=round(best_score * 100, 2))
