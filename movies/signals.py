from django.db.models.signals import post_save
from django.dispatch import receiver

from movies.models import SearchTerm
from movies.tasks import notify_of_new_search_term

@receiver(post_save, sender=SearchTerm, dispatch_uid="search_term_saved")
def search_term_saved(sender, instance, created, **kwargs):
    if created:
        # new SearchTerm was created
        # print(f"A new SearchTerm was created: '{instance.term}'")
        notify_of_new_search_term.delay(instance.term)



# References
# https://docs.djangoproject.com/en/3.2/topics/signals/
# https://docs.djangoproject.com/en/3.2/_modules/django/dispatch/dispatcher/#receiver
# https://docs.djangoproject.com/en/3.2/ref/signals/
# https://docs.djangoproject.com/en/3.2/ref/signals/#post-save
# https://github.com/django/django/blob/main/django/dispatch/dispatcher.py