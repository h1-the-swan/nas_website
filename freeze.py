from flask_frozen import Freezer
from app import create_app

freezer = Freezer()
app = create_app(config='production')
freezer.init_app(app)

if __name__ == '__main__':
    freezer.freeze()
