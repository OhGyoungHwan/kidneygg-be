from django.contrib.auth.models import User
from rest_framework import serializers
from food.models import Food, Diet, Dish, DietDetail, DishDetail


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    diet = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Diet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'diet']


class DishDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishDetail
        fields = ["dishdetailid", "foodno", "weight"]


class DishSerializer(serializers.ModelSerializer):
    userid = serializers.ReadOnlyField(source='userid.username')
    dishdetail = DishDetailSerializer(many=True)

    class Meta:
        model = Dish
        fields = ["dishid", "userid", "title",
                  "hits", "detail", "dishdetail"]

    def create(self, validated_data):
        dishDetailList = validated_data.pop("dishdetail")
        dish = Dish.objects.create(title=validated_data.pop(
            "title"), detail=validated_data.pop("detail"), userid=validated_data.pop("userid"))
        for dishDetailOne in dishDetailList:
            DishDetail.objects.create(dishid=dish, **dishDetailOne)
        return dish


class DietDetailSerializer(serializers.ModelSerializer):
    foodno = FoodSerializer(read_only=True)
    foodid = serializers.PrimaryKeyRelatedField(
        queryset=Food.objects.all(),
        write_only=True,
    )

    class Meta:
        model = DietDetail
        fields = ["dietdetailid", "foodno", "dishid", "weight", "foodid"]
        ordering = ["dietdetailid"]


class DietSerializer(serializers.ModelSerializer):
    userid = serializers.ReadOnlyField(source='userid.username')
    dietdetail = DietDetailSerializer(many=True)

    class Meta:
        model = Diet
        fields = ["dietid", "userid", "created",
                  "threemeals", "dietdetail"]
        ordering = ["created"]

    def create(self, validated_data):
        dietDetailList = validated_data.pop("dietdetail")
        diet = Diet.objects.create(threemeals=validated_data.pop(
            "threemeals"), userid=validated_data.pop("userid"))
        for dietDetailOne in dietDetailList:
            no = dietDetailOne.pop("foodid")
            DietDetail.objects.create(
                dietid=diet, foodno=no, **dietDetailOne)
        return diet
