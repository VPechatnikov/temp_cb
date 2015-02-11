from django.db import models

#Denormalized for simplicity of POC.  For other use cases (to re-use pieces of the data model), hosts, pages, and pagestats can be separate entities 
class PageStats(models.Model):
    host = models.CharField(max_length=120, null=False,blank=False)
    page_title = models.TextField(null=True,blank=True)
    page_path = models.CharField(max_length=500, null=False, blank=False)  #for POC simplicity (indexing, uniqueness) use charfield with limited length.  
                                                                           #In reality, can use hash of the page's url to avoid limitations on 
                                                                           #the length of that path while still being able to put an index and uniqueness constraint on the hash
    cur_avg = models.FloatField(null=True)
    new_avg = models.FloatField(null=True)
    num_new_points = models.IntegerField(default=0)
    increasing = models.BooleanField(default=False)
    last_speed = models.FloatField(null=True)
    updated = models.DateTimeField(auto_now_add=True,auto_now=True)

    class Meta:
        index_together = ["host", "page_path"]
        unique_together = ["host", "page_path"]
