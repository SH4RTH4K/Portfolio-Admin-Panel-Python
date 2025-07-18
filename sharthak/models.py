from django.db import models


#Home SECTION
class Home(models.Model):
    name = models.CharField(max_length=20)
    greetings_1 = models.CharField(max_length=20)
    greetings_2 = models.CharField(max_length=20, null=True, blank=True)
    picture = models.ImageField(upload_to='static/assets/picture/')
    # save time when modified
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
# ABOUT SECTION
class About(models.Model):
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=20)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='static/assets/profile/')

    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.career
    
class Profile(models.Model):
    about = models.ForeignKey(About,
                              on_delete=models.CASCADE)
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length=200)


# SKILL SECTION
class Category(models.Model):
    name = models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skill'

    def __str__(self):
        return self.name


class Skills(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=20)


    # PORTFOLIO SECTION

class Portfolio(models.Model):
    image = models.ImageField(upload_to='static/assets/portfolio/')
    link = models.URLField(max_length=200)

    def __str__(self):
        return f'Portfolio ({self.id})'
