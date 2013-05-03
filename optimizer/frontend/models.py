from django.db import models

class JarFile(models.Model):
    file = models.FileField(upload_to='backend.jar')

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

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

    order = models.IntegerField(help_text="This specifies the order in which the argument should be inputted into the Java backend. MAKE SURE THIS IS UNIQUE FROM OTHER INPUTS AND MATCHES FOR USE WITH THE JAR FILE.")

    value = models.CharField(max_length=20, blank=True)
    default_value = models.CharField(max_length=20, blank=True, help_text="If a default value is specified that will be used to cue the user as to what input is reasonable.")

    class Meta:
        ordering = ("order",)

    def __unicode__(self):
        return "%s" % self.name

class FileInput(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(blank=True)
    problem = models.ForeignKey(Problem)

    order = models.IntegerField(help_text="This specifies the order in which the argument should be inputted into the Java backend. MAKE SURE THIS IS UNIQUE FROM OTHER INPUTS AND MATCHES FOR USE WITH THE JAR FILE.")

    file = models.FileField(upload_to='inputs/%Y/%m/%d')

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
