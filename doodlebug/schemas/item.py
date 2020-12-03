from datetime import datetime

from pydantic import BaseModel

from doodlebug.utils import BaseConfig


class Item(BaseModel):
    item_id: str
    item_name: str
    item_date: datetime

    class Config(BaseConfig):
        schema_extra = {
            'example': {
                'item_id': '123',
                'item_name': 'dummy name',
                'item_date': datetime.now().isoformat(),
            }
        }

    @classmethod
    def example_factory(cls):
        example = cls.Config.schema_extra["example"]
        return cls(**example)
