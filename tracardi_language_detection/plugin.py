from tracardi_dot_notation.dot_accessor import DotAccessor
from tracardi_plugin_sdk.action_runner import ActionRunner
from tracardi_plugin_sdk.domain.register import Plugin, Spec, MetaData
from tracardi_language_detection.model.configuration import Message, Config, Key
from tracardi.service.storage.driver import storage
from tracardi.domain.resource import Resource
from tracardi_language_detection.service.sendman import PostMan


class DetectAction(ActionRunner):

    @staticmethod
    async def build(**kwargs) -> 'DetectAction':
        config = Config(**kwargs)
        message = Message(**kwargs["message"])
        key = Key(**kwargs["key"])
        source = await storage.driver.resource.load(config.source.id)
        source.config = key.dict()
        plugin = DetectAction(message, source)
        return plugin

    def __init__(self, message: Message, source: Resource):
        self.message = message
        self.source = source
        self.sendman = PostMan(source.config["key"])

    async def run(self, payload):
        dot = DotAccessor(self.profile, self.session, payload, self.event, self.flow)
        string = dot[self.message]
        return await self.sendman.send(string)


def register() -> Plugin:
    return Plugin(
        start=False,
        spec=Spec(
            module='tracardi_language_detection.plugin',
            className='DetectAction',
            inputs=["payload"],
            outputs=['payload'],
            version='0.1',
            license="MIT",
            author="Patryk Migaj",
            init={'source': {
                'id': None
            },
                "message": {"message": """Welcome aboard
        Please pay attention as we demonstrate
        The safety features of this aircraft"""},
                "key": {"key": None
                        }},
            metadata=MetaData(
                name='tracardi-language-detection',
                desc='This plugin detect language from given string with meaningcloud API',
                type='flowNode',
                width=200,
                height=100,
                icon='icon',
                group=["General"]
            )
        ))
