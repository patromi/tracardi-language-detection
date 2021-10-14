import asyncio
import aiohttp
from aiohttp import ClientConnectorError
from tracardi_dot_notation.dot_accessor import DotAccessor
from tracardi_plugin_sdk.action_runner import ActionRunner
from tracardi_plugin_sdk.domain.register import Plugin, Spec, MetaData
from tracardi_plugin_sdk.domain.result import Result
from tracardi_language_detection.model.configuration import Data, Config
from tracardi.service.storage.driver import storage
from tracardi.domain.resource import Resource
from tracardi_language_detection.service.sendman import PostMan


class DetectAction(ActionRunner):

    @staticmethod
    async def build(**kwargs) -> 'DetectAction':
        print(kwargs['data'])
        config = Config(**kwargs)
        data = Data(string=kwargs['data']['string'],key=kwargs['data']['key'])
        source = await storage.driver.resource.load(config.source.id)
        source.config = {
            "string": data.string,
            "key": data.key,
            "timeout": 15}
        plugin = DetectAction(config, source)
        return plugin

    def __init__(self, config: Config, source: Resource):
        self.config = config
        self.source = source
        self.sendman = PostMan(Data(**source.config))

    async def run(self, payload):
        dot = DotAccessor(self.profile, self.session, payload, self.event, self.flow)
        string = dot[self.source.config["string"]]
        postman = await self.sendman.send(string)
        return postman


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
                'id': 'cde09c91-9ae4-4bdc-ab58-ced3ab4e441a'
            },
                "configuation": {
                    "string": None,
                    "key": None,
                    "timeout": 15}
            }
        ),
        metadata=MetaData(
            name='tracardi-language-detection',
            desc='This plugin detect language from given string with meaningcloud API',
            type='flowNode',
            width=200,
            height=100,
            icon='icon',
            group=["General"]
        )
    )
