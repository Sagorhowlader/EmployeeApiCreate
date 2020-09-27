from  rest_framework import  serializers
from .models import emp_info

class emp_infoSerializers(serializers.ModelSerializer):
        class Meta:
                model=emp_info
                fields='__all__'