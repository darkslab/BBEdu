from django.contrib.auth import get_user_model
from django.db.models import (
    CASCADE,
    BooleanField,
    CharField,
    DateTimeField,
    FloatField,
    ForeignKey,
    Model,
)
from django.utils.translation import pgettext_lazy


class JobProgress(Model):
    job_name = CharField(pgettext_lazy("Model field", "job name"), max_length=50)
    user = ForeignKey  ( get_user_model(), on_delete=CASCADE, related_name="job_progresses", )
    started_at = DateTimeField(pgettext_lazy("Model field", "started at"), auto_now_add=True, db_index=True, editable=False)
    finished_at = DateTimeField(pgettext_lazy("Model field", "finished at"), null=True, blank=True, default=None)
    percentage = FloatField(pgettext_lazy("Model field", "progress in percents"), default=0)
    is_finished = BooleanField(default=False)

    def __str__(self):
        return f"{self.started_at}|{self.started_at}"
