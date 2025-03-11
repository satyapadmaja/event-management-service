from flask import Blueprint, request, jsonify
from src.models.event_model import Event, db
from src.services.openai_service import categorize_event

event_controller = Blueprint('event_controller', __name__)

@event_controller.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    return jsonify([{'id': event.id, 'title': event.title, 'description': event.description, 'date': event.date, 'category': event.category} for event in events])

@event_controller.route('/events/<int:id>', methods=['GET'])
def get_event(id):
    event = Event.query.get_or_404(id)
    return jsonify({'id': event.id, 'title': event.title, 'description': event.description, 'date': event.date, 'category': event.category})

@event_controller.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    category = categorize_event(data['title'], data['description'])
    new_event = Event(title=data['title'], description=data['description'], date=data['date'], category=category)
    db.session.add(new_event)
    db.session.commit()
    return jsonify({'message': 'Event created', 'event': {'id': new_event.id, 'title': new_event.title, 'description': new_event.description, 'date': new_event.date, 'category': new_event.category}}), 201

@event_controller.route('/events/<int:id>', methods=['PUT'])
def update_event(id):
    data = request.get_json()
    event = Event.query.get_or_404(id)
    event.title = data['title']
    event.description = data['description']
    event.date = data['date']
    event.category = categorize_event(data['title'], data['description'])
    db.session.commit()
    return jsonify({'message': 'Event updated', 'event': {'id': event.id, 'title': event.title, 'description': event.description, 'date': event.date, 'category': event.category}})

@event_controller.route('/events/<int:id>', methods=['DELETE'])
def delete_event(id):
    event = Event.query.get_or_404(id)
    db.session.delete(event)
    db.session.commit()
    return jsonify({'message': 'Event deleted'})