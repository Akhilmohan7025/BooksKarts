from django.db import models

# Create your models here.


# create a model districts with fields district name,population,first dose vaccination rate,second dose vaccination rate
# 10 orm queries





class Districts(models.Model):
    District_name=models.CharField(max_length=120)
    Population=models.PositiveIntegerField()
    Fdv_rate=models.PositiveIntegerField()
    Sdv_rate=models.PositiveIntegerField()

    def __str__(self):
        return self.District_name

    # ORM queries
    # CRUD
    #
    # C>>Create

    # refname=Modelname(field_name=value,field_name=value,,,,,,)
    # refname.save()


    # print the details of Idukki district
    # loc=Districts.objects.get(id=1)
    #     print(loc.District_name,loc.Population,loc.Fdv_rate,loc.Sdv_rate)
    #     loc()

    # print the details of the districts whoose population is less than 1000000
    # loc=Districts.objects.filter(Population__lt=4500)
    # loc


    # u>>upadate
    #
    # update the population of palakkad to 6000
    #     loc=Districts.objects.get(id=2)
    #     loc
    #     loc.District_name
    #     loc.Population=6000
    #     loc.save()

    # # update the name of the district ernakulam to kochi
    #   loc.Districts.objects.get(id=4)
    # loc=Districts.objects.get(id=4)
    #   loc
    #   loc.District_name
    #   loc.District_name="kochi"
    #    loc.save()

    # #  Aggregate function
    #
    #
    # # eg:max,min,average e.t.c
    # # we need to import these aggregate functions
    # # from django.db.models import Avg,Sum,Count,Max,Min

    #     from django.db.models import Max

    # find the highest population from the districts

    # dis_hp=Districts.objects.all().aggregate(Max("Population"))
    # dis_hp

    # find the highest vaccination rate


        # dis_hvr=Districts.objects.all().aggregate(Max("Fdv_rate"))
        # dis_hvr

    # find the lowest vaccination rate
        # from django.db.models import Min
        # dis_lvr=Districts.objects.all().aggregate(Min("Fdv_rate"))
        # dis_lvr




