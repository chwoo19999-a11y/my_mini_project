from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Like, Comment


@receiver(post_save, sender=Like)
def increment_likes_count(sender, instance, created, **kwargs):
    """좋아요 생성 시 카운트 증가"""
    if created:
        destination = instance.destination
        destination.likes_count += 1
        destination.save(update_fields=['likes_count'])


@receiver(post_delete, sender=Like)
def decrement_likes_count(sender, instance, **kwargs):
    """좋아요 삭제 시 카운트 감소"""
    destination = instance.destination
    if destination.likes_count > 0:
        destination.likes_count -= 1
        destination.save(update_fields=['likes_count'])


@receiver(post_save, sender=Comment)
def increment_comments_count(sender, instance, created, **kwargs):
    """댓글 생성 시 카운트 증가"""
    if created:
        destination = instance.destination
        destination.comments_count += 1
        destination.save(update_fields=['comments_count'])


@receiver(post_delete, sender=Comment)
def decrement_comments_count(sender, instance, **kwargs):
    """댓글 삭제 시 카운트 감소"""
    destination = instance.destination
    if destination.comments_count > 0:
        destination.comments_count -= 1
        destination.save(update_fields=['comments_count'])
