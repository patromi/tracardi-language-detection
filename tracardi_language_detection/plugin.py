from tracardi_dot_notation.dot_accessor import DotAccessor
from tracardi_dot_notation.dot_template import DotTemplate
from tracardi_plugin_sdk.action_runner import ActionRunner
from tracardi_plugin_sdk.domain.register import Plugin, Spec, MetaData
from tracardi_language_detection.model.configuration import Message, Key, Configuration
from tracardi.service.storage.driver import storage
from tracardi_language_detection.service.sendman import PostMan


class DetectAction(ActionRunner):

    @staticmethod
    async def build(**kwargs) -> 'DetectAction':

        # This reads key
        config = Configuration(**kwargs)
        source = await storage.driver.resource.load(config.source.id)

        return DetectAction(Message(**kwargs), Key(**source.config))

    def __init__(self, message: Message, key: Key):
        self.message = message.message
        self.postman = PostMan(key.token)

    async def run(self, payload):
        dot = DotAccessor(self.profile, self.session, payload, self.event, self.flow)
        template = DotTemplate()
        string = template.render(self.message, dot)
        return await self.postman.send(string)


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
            init={
                'source': {
                    'id': None
                },
                "message": "Hello world"
            },
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
