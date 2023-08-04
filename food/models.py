from django.db import models
# Create your models here.


class Food(models.Model):
    CATEGORIE_CHOICES = (
        ("식품상세분류", "식품상세분류"),
        ("해조류", "해조류"),
        ("채소류", "채소류"),
        ("차류", "차류"),
        ("주류", "주류"),
        ("조미료류", "조미료류"),
        ("조리가공품류", "조리가공품류"),
        ("음료류", "음료류"),
        ("육류", "육류"),
        ("유지류", "유지류"),
        ("우유 및 유제품류", "우유 및 유제품류"),
        ("어패류 및 기타 수산물", "어패류 및 기타 수산물"),
        ("버섯류", "버섯류"),
        ("두류", "두류"),
        ("당류", "당류"),
        ("난류", "난류"),
        ("기타", "기타"),
        ("과실류", "과실류"),
        ("곡류 및 그 제품", "곡류 및 그 제품"),
        ("견과류 및 종실류", "견과류 및 종실류"),
        ("감자 및 전분류", "감자 및 전분류"),
    )

    no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    categorie = models.CharField(max_length=12, choices=CATEGORIE_CHOICES)
    energy = models.FloatField()
    moisture = models.FloatField()
    protein = models.FloatField()
    phosphorus = models.FloatField()
    potassium = models.FloatField()
    natrium = models.FloatField()

    class Meta:
        ordering = ['no']


class Diet(models.Model):
    CATEGORIE_CHOICES = (
        ("breakfast", "breakfast"),
        ("lunch", "lunch"),
        ("dinner", "dinner"),
    )
    dietid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(
        'accounts.User', related_name='diet', on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    threemeals = models.CharField(max_length=9, choices=CATEGORIE_CHOICES)

    class Meta:
        unique_together = (("threemeals", "created", "userid"),)


class Dish(models.Model):
    dishid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    hits = models.IntegerField()
    detail = models.TextField()
    userid = models.ForeignKey(
        'accounts.User', related_name='dish', on_delete=models.CASCADE)


class DietDetail(models.Model):
    dietdetailid = models.AutoField(primary_key=True)
    dietid = models.ForeignKey(
        Diet, related_name='dietdetail', on_delete=models.CASCADE)
    foodno = models.ForeignKey(
        Food, null=True, related_name='dietdetail', on_delete=models.CASCADE)
    dishid = models.ForeignKey(
        Dish, null=True, related_name='dietdetail', on_delete=models.CASCADE)
    weight = models.FloatField()


class DishDetail(models.Model):
    dishdetailid = models.AutoField(primary_key=True)
    dishid = models.ForeignKey(
        Dish, related_name='dishdetail', on_delete=models.CASCADE)
    foodno = models.ForeignKey(
        Food, related_name='dishdetail', on_delete=models.CASCADE)
    weight = models.FloatField()
