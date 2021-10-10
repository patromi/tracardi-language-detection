from tracardi.domain.context import Context
from tracardi.domain.entity import Entity
from tracardi.domain.event import Event
from tracardi.domain.profile import Profile
from tracardi.domain.session import Session
from tracardi_plugin_sdk.service.plugin_runner import run_plugin

from tracardi_language_detection.plugin import DetectAction

init = payload={
    'key': '71d83e0a2ee2b68d57bf2f8fe752d73b',
    'string': """Welcome aboard
        Please pay attention as we demonstrate
        The safety features of this aircraft"""
        }
payload = {}
profile = Profile(id="profile-id")
event = Event(id="event-id",
              type="event-type",
              profile=profile,
              session=Session(id="session-id"),
              source=Entity(id="source-id"),
              context=Context())
result = run_plugin(DetectAction, init, payload,
                    profile,event)

print("OUTPUT:", result.output)
print("PROFILE:", result.profile)