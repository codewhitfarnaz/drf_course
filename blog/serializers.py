from rest_framework import serializers
from blog.models import Article

#
# class ArticleSerializer(serializers.Serializer):
#     id=serializers.IntegerField(required=False)
#     title=serializers.CharField()
#     #text=serializers.CharField()
    #status=serializers.BooleanField(required=False)


    # def create(self,validated_data):
    #     return Article.objects.create(**validated_data)

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields=("id","title","text","status")
        #read_only_fields=("title",)

    def validate_title(self,value):
        if value == "html":
            raise serializers.ValidationError("Please enter html")
        return value