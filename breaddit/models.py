from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]


class Comment(models.Model):

    class Status:
        ACTIVE = "active"
        DELETED = "deleted"
        HIDDEN = "hidden"
        SPAM = "spam"
        UNAPPROVED = "unapproved"

        CHOICES = (
            (ACTIVE, "Active"),
            (DELETED, "Deleted"),
            (HIDDEN, "Hidden"),
            (SPAM, "Spam"),
            (UNAPPROVED, "Unapproved"),
        )

    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="comments")
    status = models.CharField(max_length=255, default=Status.ACTIVE, choices=Status.CHOICES)

    def __str__(self):
        return self.body

    class Meta:
        ordering = ["-created_at"]
