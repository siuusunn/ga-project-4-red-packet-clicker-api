from .common import UserSerializer
from pockets.serializers.common import PocketSerializer # this uses absolute path. Absolute paths in django have the manage.py as the root

# genre serializer gets us the standard fields (in this case it's going to return {"id": 1, "name": "Rock"})

class PopulatedUserSerializer(UserSerializer):
  pockets = PocketSerializer(many=True)

# the populated genre serializer will get all the usual keys from the genre serializer
# but will add another which is populated by the Album Serializer