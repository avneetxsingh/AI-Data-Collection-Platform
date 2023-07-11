from django.db import models

# Create your models here.

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    query_type = models.CharField(max_length=100, blank=True, null=True)
    query = models.TextField(blank=True, null=True)
    perplexity_result = models.TextField(blank=True, null=True)
    link1 = models.URLField(max_length=500, blank=True, null=True)
    link2 = models.URLField(max_length=500, blank=True, null=True)
    link3 = models.URLField(max_length=500, blank=True, null=True)
    link4 = models.URLField(max_length=500, blank=True, null=True)
    link5 = models.URLField(max_length=500, blank=True, null=True)
    softage_answer = models.TextField(blank=True, null=True)
    assigned = models.BooleanField(default=False, null=True)
    answer_by = models.CharField(max_length=100, blank=True, null=True)
    date = models.CharField(max_length=100, blank=True, null=True)
    fluency = models.IntegerField(null=True, blank=True)
    perceived_utility = models.IntegerField(null=True, blank=True)
    backed_by_citation = models.IntegerField(null=True, blank=True)
    state_reg_citation = models.IntegerField(null=True, blank=True)
    citation_precision = models.CharField(max_length=10, null=True, blank=True)
    citation_feedback = models.CharField(max_length=1000, null=True, blank=True)
    P_ID = models.IntegerField(null=True, blank=True)