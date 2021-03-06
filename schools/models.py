from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

import os, csv

class School(models.Model):
    school_name = models.CharField(max_length=500)
    school_image = models.CharField(max_length=999)
    address = models.CharField(max_length=500)
    board = models.CharField(max_length=50)
    co_ed_status = models.CharField(max_length=50)
    ownership = models.CharField(max_length=50)
    sf_ratio = models.CharField(max_length=50)
    class_offered = models.CharField(max_length=50)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.school_name}"


class SchoolDetail(models.Model):
    school = models.ForeignKey(School, related_name='school', on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=500)
    webiste = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    lab = models.CharField(max_length=500)
    year_of_establishment = models.CharField(max_length=500)
    campus_size = models.CharField(max_length=500)
    campus_type = models.CharField(max_length=500)
    class_type = models.CharField(max_length=500)
    boarding = models.CharField(max_length=500)
    infrasturcure = models.CharField(max_length=500)
    safty_and_security = models.CharField(max_length=500)
    advance_facilities = models.CharField(max_length=500)
    extra_curricular = models.CharField(max_length=500)
    sports_and_fitness = models.CharField(max_length=500)
    disabled_friendly = models.CharField(max_length=500)
    hall_of_fame = models.CharField(max_length=99999)
    gallery = models.CharField(max_length=99999)

    def __str__(self):
        return f"{self.school.school_name}"


class SchoolsImportFile(models.Model):
    # upload to MEDIA_ROOT/temp
    schools_import = models.FileField(upload_to="temp",
                                      blank=False,
                                      null=False)

    def save(self, *args, **kwargs):
        if self.pk:
            old_import = SchoolsImportFile.objects.get(pk=self.pk)

            if old_import.schools_import:
                old_import.schools_import.delete(save=False)

        return super(SchoolsImportFile, self).save(*args, **kwargs)



# post save signal
@receiver(post_save, sender=SchoolsImportFile, dispatch_uid="add_records_to_schools_from_import_file")
def add_records_to_schools_from_import_file(sender, instance, **kwargs):
    to_import = os.path.join(settings.MEDIA_ROOT, instance.schools_import.name)

    with open(to_import) as f:
        reader = csv.DictReader(f)
        for row in reader:
            school_name = row['school_name']
            address = row['address'].strip('').strip('')
            board = row['Board']
            ownership = row['Ownership']
            co_ed = row['Co-Ed Status']
            sf_ratio=row['sf_ratio']
            school_image=row['school_image']
            class_offered=row['class_offered']

            phone_no=row['phone_no']
            email=row['email']
            webiste=row['website']
            gallery=row['gallery'].strip('[').strip(']').replace("'","")
            hall_of_fame=row['hall_of_fame'].strip('[').strip(']').replace("'","")
            disabled_friendly=row['Disabled Friendly'].strip('[').strip(']').replace("'","")
            lab=row['Lab'].strip('[').strip(']').replace("'","")
            sports_and_fitness=row['Sports and Fitness'].strip('[').strip(']').replace("'","")
            infrasturcure = row['Infrastructure'].strip('[').strip(']').replace("'","")
            safty_and_security = row['Safety and Security'].strip('[').strip(']').replace("'","")
            advance_facilities = row['Advanced Facilities'].strip('[').strip(']').replace("'","")
            extra_curricular = row['Extra Curricular'].strip('[').strip(']').replace("'","")
            boarding = row['Boarding'].strip('[').strip(']').replace("'","")
            class_type = row['Class'].strip('[').strip(']').replace("'","")
            campus_type = row['Campus Type']
            campus_size = row['Campus Size']
            yoe=row['Year of Establishment']

            # school_logo=re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', gallery)


            obj, created = School.objects.update_or_create(
                school_name=school_name,
                address=address,
                board=board,
                co_ed_status=co_ed,
                ownership=ownership,
                school_image=school_image,
                sf_ratio=sf_ratio,
                class_offered=class_offered
                )

            SchoolDetail.objects.update_or_create(
                school=obj,
                phone_no=phone_no,
                email=email,
                webiste=webiste,
                gallery=gallery,
                hall_of_fame=hall_of_fame,
                disabled_friendly=disabled_friendly,
                lab=lab,
                sports_and_fitness=sports_and_fitness,
                infrasturcure=infrasturcure,
                safty_and_security=safty_and_security,
                advance_facilities=advance_facilities,
                extra_curricular=extra_curricular,
                boarding=boarding,
                class_type=class_type,
                campus_type=campus_type,
                campus_size=campus_size,
                year_of_establishment=yoe,
            )


class SchoolReviews(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment = models.CharField(max_length=999)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name_plural = "School Reviews"
