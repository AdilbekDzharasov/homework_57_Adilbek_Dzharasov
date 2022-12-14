from django.db import models


class Task(models.Model):
    summary = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        verbose_name='Summary'
    )
    description = models.TextField(
        max_length=3000,
        null=True,
        blank=True,
        verbose_name='Description'
    )
    status = models.ForeignKey(
        to='webapp.Status',
        related_name='status',
        on_delete=models.PROTECT,
        verbose_name='Status'
    )
    type = models.ForeignKey(
        to='webapp.Type',
        related_name='type',
        on_delete=models.PROTECT,
        verbose_name='Type'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    def __str__(self):
        return f"{self.summary}"

