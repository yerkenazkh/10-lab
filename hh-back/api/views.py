from django.http.response import JsonResponse
from api.models import Vacancy, Company
from api.serializers import CompanySerializer, VacancySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from rest_framework.views import APIView
from rest_framework import status

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated 

@permission_classes(IsAuthenticated, )
@api_view(['GET', 'POST'])
def companies(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return JsonResponse(serializer.data, safe=False)    
    elif request.method == 'POST':
        serializer = CompanySerializer(data=json.loads(request.body))
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "New company created!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['GET', 'PUT', 'DELETE'])
def company(request, id):
    if request.method == 'GET':
        try:
            company = Company.objects.get(id=id)
            serializer = CompanySerializer(company)
            return JsonResponse(serializer.data, safe=False)
        except:
            return JsonResponse({"error": "No company"})
    
    elif request.method == 'PUT':
        try:
            company = Company.objects.get(id=id)
        except:
            return JsonResponse({'error': 'no company with that id'})

        serializer = CompanySerializer(instance=company, data=json.loads(request.body))
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'updated successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)            
    
    elif request.method == 'DELETE':
        try:
            company = Company.objects.get(id=id)
        except:
            return JsonResponse({'error': 'no company with that id'})

        company.delete()
        return Response({'msg': 'deleted succesfully'}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def vacancies_by_company(request, id):
    if request.method == 'GET':
        company = Company.objects.get(id=id)
        vacancies = company.vacancy_set.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class VacancyViews(APIView):
    def get(self, request):
        try:
            vacancies = Vacancy.objects.all()
            serializer = VacancySerializer(vacancies, many=True)
            return JsonResponse(serializer.data, safe=False)
        except:
            return JsonResponse({"message": "no data"}, safe=False)

    def post(self, request):
        serializer = VacancySerializer(data=json.loads(request.body))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'Error': serializer.errors})

class VacancyDView(APIView):
    def get(self, request, id):
        try:
            vacancy = Vacancy.objects.get(id=id)
        except:
            return Response({'Errror': 'no vacancy'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        serializer = VacancySerializer(vacancy)
        return JsonResponse(serializer.data, safe=False)

    def put(self, request, id):
        try:
            vacancy = Vacancy.objects.get(id=id)
        except:
            return Response({'Errror': 'no vacancy'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer = VacancySerializer(instance=vacancy, data=json.loads(request.body))
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "updated succesfully"})
        return Response({"error": serializer.errors})

    def delete(self, request, id):
        try:
            vacancy = Vacancy.objects.get(id=id)
        except:
            return Response({'Errror': 'no vacancy'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        vacancy.delete()

        return Response({"message": "deleted succesfully"})