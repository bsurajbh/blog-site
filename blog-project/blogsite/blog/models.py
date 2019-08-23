from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model."""

    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(_('name'), max_length=30)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_superadmin = models.BooleanField(_('active'), default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_absolute_url(self):
        """Return URL."""
        return reverse("login")


class Category(models.Model):
    """Blog category."""

    name = models.CharField(_('name'), unique=True, max_length=200)

    def __str__(self):
        """Category string representation."""
        return self.name


class Post(models.Model):
    """post model."""

    author = models.ForeignKey(User,  on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        'blog.Category', related_name='category',
        on_delete=models.CASCADE, max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """Publish blog."""
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        """Approve comment on blog."""
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        """Given String representaion of class."""
        return self.title

    def get_absolute_url(self):
        """Return URL."""
        return reverse("post_detail", kwargs={'pk': self.pk})


class Comment(models.Model):
    """Comment model."""

    post = models.ForeignKey(
        'blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        """Approve comment."""
        self.approved_comment = True
        self.save()

    def __self__(self):
        """Given string representation."""
        return self.text

    def get_absolute_url(self):
        """Return URL."""
        return reverse('post_list')
