from tortoise import Tortoise,fields,run_async
from tortoise.models import Model

class Event(Model):
    id=fields.IntField(pk=True)
    name=fields.TextField(description='Name of the event that corresponds to an action')
    datetime=fields.DatetimeField(null=True,description='Datetime of when the event was generated')
    class Meta:
        table='event'
        table_description='This table contains a list of all the exampl events'
    def __str__(self):
        return self.name
async def run():
    await Tortoise.init(db_url='postgres://postgres:root@localhost:5432/postgres',modules={'models':['__main__']})
    await Tortoise.generate_schemas()

    event=await Event.create(name="1")
if __name__ == '__main__':
    run_async(run())