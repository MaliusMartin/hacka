

from django.db import models

class InputData(models.Model):
    gender_inequality_index = models.FloatField()
    maternal_mortality_ratio = models.FloatField()
    adolescent_birth_rate = models.FloatField()
    women_parliament_seats = models.FloatField()
    female_secondary_education = models.FloatField()
    male_secondary_education = models.FloatField()
    female_labour_force = models.FloatField()
    male_labour_force = models.FloatField()

    def __str__(self):
        return f"{self.id} - {self.gender_inequality_index} | {self.maternal_mortality_ratio} | {self.adolescent_birth_rate} | {self.women_parliament_seats} | {self.female_secondary_education} | {self.male_secondary_education} | {self.female_labour_force} | {self.male_labour_force}"
