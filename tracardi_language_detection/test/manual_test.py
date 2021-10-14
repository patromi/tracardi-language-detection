from tracardi.domain.context import Context
from tracardi.domain.entity import Entity
from tracardi.domain.event import Event
from tracardi.domain.profile import Profile
from tracardi.domain.session import Session
from tracardi_plugin_sdk.service.plugin_runner import run_plugin
from dotenv import load_dotenv

from tracardi_language_detection.plugin import DetectAction
load_dotenv()
print()
init = payload={'source': {
                'id': '55584df6-9ee3-4acd-a0ea-e555122f3dbc'
                },
                "data":{
                "string": """Welcome aboard
        Please pay attention as we demonstrate
        The safety features of this aircraft""",
                "key": "your key",
                "timeout": 15}}

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