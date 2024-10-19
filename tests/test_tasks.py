from app.tasks import run_healthchecks

def test_run_healthchecks(app):
    run_healthchecks.defer(1)

# def test_model():
    
#     from mixer.backend.django import mixer
#     from customapp.models import User, UserMessage

#     # Generate a random user
#     user = mixer.blend(User)
