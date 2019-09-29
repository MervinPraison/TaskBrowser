from django.db import models
from django.utils import timezone
import datetime
from mptt.models import MPTTModel, TreeForeignKey
import collections
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError

class Task(MPTTModel):
    task_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, unique=True)
    start_date = models.DateTimeField('Start date',null=True, blank=True)
    end_date = models.DateTimeField('End date', blank=True, null=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
    def __str__(self):
        return self.name
    
    def status_check(self, task):
        if task.start_date > timezone.now():
            return "Scheduled"
        elif task.end_date < timezone.now():
            return "Complete"
        elif task.start_date < timezone.now() and task.end_date > timezone.now():
            return "Running"
        else:
            return "NULL"
    def status(self):
        status ="NULL"
        SubTask = Task.objects.get(pk=self.task_id).get_descendants()
        if not SubTask:
            if self.start_date or self.end_date: status = self.status_check(self)
        else:
            ChildStatus = []
            for st in SubTask:
                if st.start_date or st.end_date: ChildStatus.append(self.status_check(st))
            counter=collections.Counter(ChildStatus)
            if counter['Running']>=2:
                status = "Multi-Runs"
            elif counter['Running']==1:
                status = "Running"
            elif counter['Complete']>=1 and counter['Scheduled']>=1:
                status = "Idle"
            elif counter['Scheduled']>=1:
                status = "Scheduled"
            elif counter['Complete']>=1:
                status = "Complete"
            else:
                status = "NULL"
        return status
    def Start_Timestamp(self):
        SubTask = Task.objects.get(pk=self.task_id).get_descendants()
        if not SubTask:
            if self.start_date: return self.start_date
            else: return "NULL"
        else:
            StartDates = []
            SubTask = Task.objects.get(pk=self.task_id).get_descendants()
            for st in SubTask:
                if st.start_date: StartDates.append(st.start_date)
            if StartDates: return min(StartDates)
            else: return
    def End_Timestamp(self):
        SubTask = Task.objects.get(pk=self.task_id).get_descendants()
        if not SubTask:
            if self.end_date: return self.end_date
            else: return "NULL"
        else:
            EndDates = []
            SubTask = Task.objects.get(pk=self.task_id).get_descendants()
            for st in SubTask:
                if st.end_date: EndDates.append(st.end_date)
            if EndDates: return max(EndDates)
            else: return
    def isparent(self):
        if self.parent:
            return self.parent
        else:
            return "NULL"
    def duration(self):
        SubTask = Task.objects.get(pk=self.task_id).get_descendants()
        if not SubTask:
            return self.taskduration(self)
        else:
            Net_Duration = []
            for st in SubTask:
                if st.start_date and st.start_date: Net_Duration.append(self.taskduration(st))
            if not Net_Duration: return 0
            else: return sum(Net_Duration)
    def taskduration(self,task):
        if task.start_date:
            if task.end_date > task.start_date:
                duration = task.end_date - task.start_date
                days, seconds = duration.days, duration.seconds
                hours = days * 24 + seconds // 3600
                minutes = hours * 60 * 60// 60
                return minutes
            else:
                return 'Error'
        else:
            return 0
    def clean(self):
        if self.parent and (self.start_date or self.end_date):
            if self.start_date > self.end_date:
                raise ValidationError({
                    NON_FIELD_ERRORS: ['Start date need to be before end date',],
                })
        if not self.parent and (self.start_date or self.end_date):
            raise ValidationError({
                NON_FIELD_ERRORS: ['Start and end date needs to be empty for Parent task or Choose a Parent task'],
            })
    
    def was_recently_started(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.start_date <= now
    
    was_recently_started.admin_order_field = 'start_date'
    was_recently_started.boolean = True
    was_recently_started.short_description = 'Started recently?'
