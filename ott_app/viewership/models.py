from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    """
    User Manager Model
    """

    use_in_migration = True

    def create_user(self, id, password=None, **extra_fields):
        """
        Overriding the create_user method

        Args:
            id (Char): customer_id
            password (Char, optional): customer_password. Defaults to None.
        Returns:
            Obj: User Object
        """
        if not id:
            raise ValueError("Customer ID is Required")
        user = self.model(id=id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id, password, **extra_fields):
        """
        Overriding the create_superuser method

        Args:
            id (Char): customer_id
            password (Char, optional): customer_password. Defaults to None.
        Returns:
            Obj: User Object
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff = True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser = True")

        return self.create_user(id, password, **extra_fields)


class Customer(AbstractBaseUser):
    """
    Customer Model
    """

    username = None
    id = models.CharField(max_length=8, primary_key=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=100)
    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "id"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser


class Viewership(models.Model):
    """
    Viewership Model
    """

    timestamp = models.DateTimeField(auto_now=True)
    video_title = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
