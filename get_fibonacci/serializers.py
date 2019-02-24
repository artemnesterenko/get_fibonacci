from rest_framework.exceptions import ValidationError
from rest_framework.fields import IntegerField
from rest_framework.serializers import Serializer


class SliceSerializer(Serializer):
    from_ = IntegerField(min_value=0, required=True)
    to = IntegerField(min_value=1, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # deal with the from field matching the python's reserved keyword
        for name in list(self.fields.keys()):
            if name.endswith("_"):
                field = self.fields.pop(name)
                self.fields[name[:-1]] = field

    def validate(self, attrs):
        attrs = super().validate(attrs)
        from_ = attrs["from_"]
        to = attrs["to"]
        if from_ >= to:
            raise ValidationError(
                'The "from" field value must be less than the "to" field value'
            )
        del attrs["from_"]
        attrs["from"] = from_
        return attrs
