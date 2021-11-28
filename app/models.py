from django.db import models
# from django.db.models.enums import Choices
# import psycopg2
# conn = psycopg2.connect(database ="",  # input db info !!
#                             user = "",  
#                             password = "",  
#                             host = "",  
#                             port = "") #ket noi  toi database
# cur = conn.cursor()
# def getCityList():
#     cur.execute("select city,city from city group by city")
#     city = cur.fetchall()
#     return city
# def getDistrictList(city):
#     cur.execute("select district,district from city where city = '%s'" % (city))
#     dis = cur.fetchall()
#     return dis
# # Create your models here.
# class City(models.Model):
#     city = models.CharField(choices = getCityList())

#     def __str__(self):
#         return self.city

# class District(models.Model):
#     city = models.ForeignKey(City, on_delete=models.CASCADE)
#     dis = models.CharField()

#     def __str__(self):
#         return self.name
