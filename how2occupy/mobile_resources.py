from djangorestframework.resources import ModelResource
from how2occupy.mobile_models import MyModel

class MyModelResource(ModelResource):
    model = MyModel
    fields = ('foo', 'bar', 'baz', 'url')
    ordering = ('created',)
