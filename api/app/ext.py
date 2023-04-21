from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from marshmallow import SchemaOpts

ma = Marshmallow()
migrate = Migrate()

class BaseSchemaOpts(SchemaOpts):

    def __init__(self, meta, **kwargs):
        super().__init__(meta, **kwargs)
        self.allow_none = getattr(meta, 'allow_none', ())
        self.required = getattr(meta, 'required', ())

