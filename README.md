# Event Management Service

This project is a simple event management service that provides a backend server using Flask, RESTful APIs for managing events, and a PostgreSQL database for storage. It also integrates with the OpenAI API for intelligent event categorization.

## Features

- Create, retrieve, update, and delete events
- Categorize events using OpenAI's API
- Store event data in a PostgreSQL database
- RESTful API endpoints for easy integration

## Project Structure

```
event-management-service
├── src
│   ├── app.py                  # Entry point of the application
│   ├── controllers
│   │   └── event_controller.py  # Handles event-related requests
│   ├── models
│   │   └── event_model.py       # Defines the Event model
│   ├── routes
│   │   └── event_routes.py       # Defines API endpoints
│   ├── services
│   │   └── openai_service.py     # Interacts with OpenAI API
│   └── config.py                # Configuration settings
|   |__  client
|        |
|          gui.py
├── requirements.txt             # Project dependencies
├── Dockerfile                   # Docker image instructions
└── docker-compose.yml           # Service configurations
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd event-management-service
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt

3. Install, Run PostgreSQL:
  brew install postgresql
  brew services start postgresql
  psql postgres

  createdb event_management
  CREATE ROLE your_user WITH LOGIN PASSWORD 'your_password';
  ALTER ROLE your_user CREATEDB;
  # .env - change your_user and your_password
  DATABASE_URL=postgresql://your_user:your_password@localhost:5432/event_management
  export DYLD_LIBRARY_PATH="/usr/local/opt/postgresql/lib:$DYLD_LIBRARY_PATH"
  source ~/.bash_profile

4. Local LLM - Install and test with Curl command
   brew install ollama
   ollama serve
   ollama pull mistral
   curl -X POST "http://localhost:11434/api/generate" \
     -d '{
          "model": "mistral",
          "prompt": "Categorize the following event: Title: Birthday, Description: Aravind Birthday event"
        }'

5. Running the application:

Window 1 - Run the application

   # Using Tkinker GUI - If this command doesnt work in Visual Studio try in standalone terminal
   python src/client/gui.py

   # Run the Flask app
   cd /Users/mantha/AI-Projects/event-management-service
   python -m src.app

Window 2 - Run LLM

Window 3 - Give Curl commands if running the flask app: Example curl commands are given below

CURL Commands
Create Event
curl -X POST http://127.0.0.1:5000/events -H "Content-Type: application/json" -d '{"title": "Sample Event", "description": "This is a sample event", "date": "2025-03-10T10:00:00"}'

Get All Events:
curl http://127.0.0.1:5000/events

Get Event Ids
curl http://127.0.0.1:5000/events

Update Event
curl -X PUT http://127.0.0.1:5000/events/1 -H "Content-Type: application/json" -d '{"title": "Updated Event", "description": "This is an updated event", "date": "2025-03-11T10:00:00"}'

Delete Event
curl -X DELETE http://127.0.0.1:5000/events/1

## Usage

- Use the provided RESTful API endpoints to manage events.
- Events can be categorized by sending their title and description to the OpenAI API.

## License

This project is not licensed as of now.
