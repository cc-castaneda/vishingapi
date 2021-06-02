from django.db import models

class ReportNumber(models.Model):
    search_number_id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=15, unique=True)
    times_consulted = models.IntegerField()
    rating = models.DecimalField(max_digits=10, decimal_places=2)
    creation_date = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'TelephoneNumbers'
    
    def __str__(self):
        return self.number


class ReportNumberByUser(models.Model):
    telephone_number_id = models.ForeignKey(ReportNumber, on_delete=models.CASCADE)
    user_report = models.CharField(max_length=15, unique=True)
    qualify = models.DecimalField(max_digits=10, decimal_places=2)
    commentaries = models.CharField(max_length=150)
    creation_date = models.DateField(auto_now=True)

    class Meta:
        ordering = ["-user_report"]
        verbose_name_plural = 'Reports'
    
    def __str__(self):
        return self.name