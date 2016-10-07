"""
This example doesn't work - it demonstrates features that don't exist yet.

"""
import asyncio
import logging

from juju.model import Model


async def run():
    model = Model()
    await model.connect_current()
    await model.reset(force=True)

    goal_state = Model.from_yaml('bundle-like-thing')
    ubuntu_app = await model.deploy(
        'ubuntu-0',
        service_name='ubuntu',
        series='trusty',
        channel='stable',
    )
    ubuntu_app.on_unit_added(callback=lambda unit: True)

    await model.deploy(
        'nrpe-11',
        service_name='nrpe',
        series='trusty',
        channel='stable',
        num_units=0,
    )
    await model.add_relation(
        'ubuntu',
        'nrpe',
    )

    result, ok = await model.block_until(
        lambda: model.matches(goal_state),
        timeout=600
    )


logging.basicConfig(level=logging.DEBUG)
ws_logger = logging.getLogger('websockets.protocol')
ws_logger.setLevel(logging.INFO)
loop = asyncio.get_event_loop()
loop.create_task(run())
loop.run_forever()
