from django.db import models

# Create your models here.
class RequestEntry(models.Model):
    input_json = models.TextField()
    output_json = models.TextField()
    function_name = models.CharField(max_length=100)
    success = models.BooleanField()
    test_res = models.NullBooleanField(null=True)
    previous_request = models.ForeignKey('RequestEntry', blank=True, null=True)

    def __str__(self):
        return str(self.id)