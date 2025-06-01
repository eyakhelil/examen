from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json

def create_sync_task():
    schedule, _ = IntervalSchedule.objects.get_or_create(
        every=2,
        period=IntervalSchedule.MINUTES,
    )

    PeriodicTask.objects.update_or_create(
        name="Sync with lowcode",
        defaults={
            'interval': schedule,
            'task': 'api.tasks.sync_data_with_lowcode',
            'args': json.dumps([]),
        }
    )
