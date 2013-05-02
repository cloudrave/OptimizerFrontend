from django.db import models

class Problem(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(blank=True)
    is_visible = models.BooleanField(default=True)
    url = models.CharField(max_length=11, help_text="MUST BE ONLY ONE WORD LONG, and please lowercase. Also, make it unique from other problems.")

    key = models.IntegerField(help_text="Use this field to enter the Java commandline numerical choice for this problem.")

    image = models.FileField(upload_to='problemImg/%Y/%m/%d')

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        ordering = ("name",)

class Input(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(blank=True)
    problem = models.ForeignKey(Problem)

    order = models.IntegerField(help_text="This specifies the order in which the argument should be inputted into the Java backend.")

    value = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        ordering = ("order",)

    def __unicode__(self):
        return "%s" % self.name

class Solution(models.Model):
    prob = models.ForeignKey(Problem)

    text = models.TextField(blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class Algorithm(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(blank=True)
    is_visible = models.BooleanField(default=True)
    url = models.CharField(max_length=11, help_text="MUST BE ONLY ONE WORD LONG, and please lowercase.")

    key = models.IntegerField(help_text="Use this field to enter the Java commandline numerical choice for this algorithm.")

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        ordering = ("name",)
