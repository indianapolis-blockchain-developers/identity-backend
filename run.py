from identity_app.app import app, db
from dotenv import load_dotenv


load_dotenv()
db.init_app(app)
app.run(port=5000, debug=True)

