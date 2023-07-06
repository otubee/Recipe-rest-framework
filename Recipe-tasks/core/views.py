from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from . serializer import RecipeSerializer
from . models import Recipe
from django.db.models import Q

# Create your views here.

@api_view(['GET'])
def home(request):
  data = ['recipes/', 'recipes/?query=tribe', 'recipe/id', 'create', ]
  return Response(data)

@api_view(['GET'])
def homeView(request):
  query = request.GET.get('query')

  if query == None:
    query = ''

  recipes = Recipe.objects.filter(Q(tribe__icontains = query) | Q(recipeType__icontains = query))
  
  serializer = RecipeSerializer(recipes, many=True)
  return Response(serializer.data)

@api_view(['POST'])
def createView(request):
  recipes = Recipe.objects.create(
    tribe = request.data['tribe'],
    recipeType = request.data['recipeType'],
    ingredients = request.data['ingredients'],
    ingredientsQty = request.data['ingredientsQty'],
    desc = request.data['desc'],
  )
  serializer = RecipeSerializer(recipes, many=False)
  return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def recipeDetails(request, id):
  data = id
  recipes = Recipe.objects.get(id=id)

  if request.method == 'GET':
    serializer = RecipeSerializer(recipes, many=False)
    return Response(serializer.data)
  
  if request.method == 'PUT':
    recipes.tribe = request.data['tribe']
    recipes.recipeType = request.data['recipeType']
    recipes.ingredients = request.data['ingredients']
    recipes.ingredientsQty = request.data['ingredientsQty']
    recipes.desc = request.data['desc']
    recipes.save()
    serializer = RecipeSerializer(recipes, many=False)
    return Response(serializer.data)

  if request.method == 'DELETE':
    recipes.delete()
    return Response('Recipe deleted')
