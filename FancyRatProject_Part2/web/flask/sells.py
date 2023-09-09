from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
api = Api(app)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db = SQLAlchemy(app)

# Define the database schema
class Sell(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.Float)
    date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    sells = db.relationship('Sell', backref='user', lazy=True)

# Create the database tables
db.create_all()

# Define a resource for sells
class SellResource(Resource):
    # Validate and sanitize the request parameters
    def get(self):
        try:
            # Retrieve query parameters for pagination
            page = request.args.get('page', default=1, type=int)
            per_page = request.args.get('per_page', default=10, type=int)

            # Paginate the Sell data from the database
            sells = Sell.query.paginate(page=page, per_page=per_page, error_out=False)

            if not sells.items:
                return {'message': 'No sells found.'}

            # Prepare the JSON response
            sell_data = []
            for sell in sells.items:
                sell_info = {
                    'name': sell.name,
                    'price': sell.price,
                    'date': sell.date.strftime('%Y-%m-%d %H:%M:%S'),
                    'user_name': sell.user.name
                }
                sell_data.append(sell_info)

            return {
                'page': page,
                'per_page': per_page,
                'total_items': sells.total,
                'sells': sell_data
            }

        except SQLAlchemyError as e:
            return {'error': f'SQLAlchemy Error: {str(e)}'}, 500  # Handle SQLAlchemy errors specifically

# Add the SellResource as a route to the Flask application
api.add_resource(SellResource, '/sells')

# Start the Flask application when this script is executed
if __name__ == '__main__':
    app.run(debug=True)