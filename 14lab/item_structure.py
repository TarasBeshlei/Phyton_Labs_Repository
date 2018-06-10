from app import ma


class DeviceStructure(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'item_type', 'price', 'brand')