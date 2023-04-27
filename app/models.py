from django.db import models
from django.contrib.auth.models import User
# Create your models here.


from django.db import models
import json

class ListField(models.TextField):
    """
    A custom field that allows a list of values to be stored as a TextField.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        if value is None:
            return []
        return json.loads(value)

    def to_python(self, value):
        if isinstance(value, list):
            return value
        if value is None:
            return []
        return json.loads(value)

    def get_prep_value(self, value):
        if isinstance(value, str):
            return value
        return json.dumps(value)


direct=[
    ('DT','DT'),
    ('DTE','DTE'),
    ('PAC','PAC'),
    ('DAF','DAF'),
]
cate=[
    ('admin','admin'),
    ('directeur','directeur'),
    ('chef labo','chef labo'),
    ('operateur','operateur'),
    ('reception','reception'),
]
class employer(models.Model):

    user=models.OneToOneField(User , on_delete=models.CASCADE )
    mdp=models.CharField(max_length=50 , default='')
    photo=models.ImageField(blank=True , null=True)
    categorie=models.CharField(choices=cate, max_length=100)
    direction=models.CharField(choices=direct,max_length=50 , null=True )

    def __str__(self):
        return self.user.username
    
types=[
    ('carton' , 'catron'),
    ('verre' , 'verre'),
    ('type 3' , 'type 3'),
    ('type 4' , 'type 4'),
    ('type 5' , 'type 5'),
]

suffix_dict={
    'carton':'ct',
    'verre':'vr',
    'type 3':'t3',
    'type 4':'t4',
}

class materiaux(models.Model):
    type=models.CharField(max_length= 50 , choices=types)
    nom=models.CharField(max_length=50)
    suffix=models.CharField(max_length=10 , blank=True , null=True)
    delai=models.IntegerField()
    

    def save(self, *args, **kwargs):
            self.suffix=suffix_dict[self.type]
            super().save(*args, **kwargs)
    def __str__(self):
         return self.nom
    

class holidays(models.Model):
    first_day=models.DateField()
    last_day=models.DateField()
    occasion=models.CharField(max_length= 150)
    days=ListField(default=[])
    weekends=ListField(default=[])
    unpaid_day=models.IntegerField(default=0)

    def save(self , *args , **kargs):
        self.unpaid_day=len(self.days)-len(self.weekends) 
        super(holidays , self).save(*args,**kargs)

    def __str__(self):
        return self.occasion