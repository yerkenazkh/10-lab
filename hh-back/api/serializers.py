from rest_framework import serializers

from api.models import Company, Vacancy

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = 'id', 'name', 'description', 'city', 'address'

class VacancySerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    description = serializers.CharField()
    salary = serializers.FloatField()
    company = CompanySerializer()

    def create(self, validated_data):
        vacancy = Vacancy.objects.create(name=validated_data.get('name'))
        return vacancy

    def update(self, validated_data):
        vacancy = Vacancy.objects.get()