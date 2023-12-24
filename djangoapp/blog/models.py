from django.contrib.auth.models import User
from django.db import models
from utils.rands import slugfy_new

class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        
    name = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True, default=None,
        null=True, blank=True, max_length=255,
    )
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugfy_new(self.name)
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.name
    
class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True, default=None, null=True,
        blank=True, max_length=255,
    )
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugfy_new(self.name)
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.name
    
class Page(models.Model):
    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'
        
    title = models.CharField(max_length=65,)
    slug = models.SlugField(
        unique=True, default='',
        null=False, blank=True, max_length=255
    )
    is_published = models.BooleanField(
        default=False,
        help_text='Marque para publicar a página'
        )
    content = models.TextField()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugfy_new(self.title, 4)
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.title
    
class Post(models.Model):
    class Meta:
        verbose_name = 'Post',
        verbose_name_plural = 'Posts',
        
    title = models.CharField(max_length=65,)
    slug = models.SlugField(
        unique=True, default='',
        null=False, blank=True, max_length=255
    )
    excerpt = models.CharField(max_length=255)
    is_published = models.BooleanField(
        default=False,
        help_text='Marque para publicar a post'
        )
    content = models.TextField()
    cover = models.ImageField(upload_to='posts/%Y/%m/', blank=True, default='')
    cover_in_post_content = models.BooleanField(
        default=True,
        help_text='Marque para exibir a capa dentro do post',
    )
    creat_at = models.DateTimeField(auto_now_add=True)
    creat_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='post_create_by'
    )
    update_at = models.DateTimeField(auto_now=True)
    update_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='post_update_by'
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, default=None,
    )
    tags = models.ManyToManyField(Tag, blank=True, default='',)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugfy_new(self.title, 4)
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.title