from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date')
    body = models.TextField()

    #title 자기 제목으로
    def __str__(self):
        return self.title

    #body에 100자 제한
    def summary(self):
        return self.body[:100]

#댓글기능 구현
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.content