from django.db import models
from django.utils import timezone
import datetime

class Task(models.Model):
    task_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField('Start date')
    end_date = models.DateTimeField('End date')
    parent = models.ForeignKey("self",blank=True, null=True ,related_name='children', on_delete=models.DO_NOTHING, related_query_name='child')
    def __str__(self):
        return self.name
    def status(self):
        if self.start_date >= timezone.now():
            return "Scheduled"
        elif self.end_date <= timezone.now():
            return "Complete"
        elif self.start_date <= timezone.now() and self.end_date >= timezone.now():
            return "Multi-Runs"
        else:
            return "Idle"
    def isparent(self):
        if self.parent:
            return self.parent
        else:
            return "NULL"
    def duration(self):
        if self.end_date > self.start_date:
            duration = self.end_date - self.start_date
            days, seconds = duration.days, duration.seconds
            hours = days * 24 + seconds // 3600
            minutes = hours * 60 * 60// 60
            return minutes
        else:
            return 'Error'
    def was_recently_started(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.start_date <= now
    
    was_recently_started.admin_order_field = 'start_date'
    was_recently_started.boolean = True
    was_recently_started.short_description = 'Started recently?'
    
                                                  

   