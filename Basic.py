from tortoise import Tortoise,fields,run_async
from tortoise.models import Model

class Event(Model):
    id=fields.IntField(pk=True)
    name=fields.TextField()
    datetime=fields.DatetimeField(null=True)
    class Meta:
        table="event"
    def __str__(self):
        return self.name
async def run():
    await Tortoise.init(db_url='postgres://postgres:root@localhost:5432/postgres',modules={'models':['__main__']})
    await Tortoise.generate_schemas()

    event=await Event.create(name='Test')
    # await Event.first(id=event.id)
    print(await Event.filter(name='Test').first())

    await Event.filter(id=1).update(name='Upadate Test')
if __name__ == '__main__':
    run_async(run())