from flask import Blueprint, request, jsonify
from controllers.event_controller import EventController

event_routes = Blueprint('event_routes', __name__)
event_controller = EventController()

@event_routes.route('/events', methods=['POST'])
def create_event():
    data = request.json
    event = event_controller.create_event(data)
    return jsonify(event), 201

@event_routes.route('/events', methods=['GET'])
def get_events():
    events = event_controller.get_events()
    return jsonify(events), 200

@event_routes.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = event_controller.get_event(event_id)
    return jsonify(event), 200

@event_routes.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.json
    updated_event = event_controller.update_event(event_id, data)
    return jsonify(updated_event), 200

@event_routes.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    event_controller.delete_event(event_id)
    return jsonify({'message': 'Event deleted successfully'}), 204

def setup_routes(app):
    app.register_blueprint(event_routes)