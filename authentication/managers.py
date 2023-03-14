from django.contrib.auth.base_user import BaseUserManager

# from django.utils.translation import gettext as _

class CustomizeUserManager(BaseUserManager):

    ### custom user model manager where email is unique identifier
    ## for user authentication instead of usernames.
    
    def create_user(self,email,user_type,password,**extra_fields):
        if not email:
            raise ValueError('User email is required')
        
        if not user_type:
            raise ValueError('User user_type is required')
        
        email = self.normalize_email(email)
        user_type = user_type
        user = self.model(email=email,user_type=user_type,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    
    def create_superuser(self,email,user_type,password,**extra_fiels):
        extra_fiels.setdefault('is_staff',True)
        extra_fiels.setdefault('is_superuser',True)
        extra_fiels.setdefault('is_active',True)
        
        if extra_fiels.get('is_staff') is not True:
            raise ValueError('super must have is_staff = True')
        
        if extra_fiels.get('is_superuser') is not True:
            raise ValueError('super must have is_superuser = True')
        return self.create_user(email,user_type,password,**extra_fiels)