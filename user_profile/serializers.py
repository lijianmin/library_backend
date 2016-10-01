from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer
from user_profile.models import UserProfile
from django.contrib.auth.models import User, Group

from allauth.account import app_settings as allauth_settings
from allauth.utils import email_address_exists
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

class UserRegisterSerializer(serializers.Serializer):
    
    # core fields for User
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    username = serializers.CharField(required=True, write_only=True)
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    # User Profile fields
    mobile_no = serializers.CharField(required=True, write_only=True)
    country = serializers.CharField(required=True, write_only=True)

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address."))
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                _("The two password fields didn't match."))
        return data

    def get_cleaned_data(self):
        return {
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'username': self.validated_data.get('username', ''),
            'mobile_no': self.validated_data.get('mobile_no', ''),
            'country': self.validated_data.get('country', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        user.save()
        
        profile = UserProfile.objects.create(user=user)
        profile.country = self.cleaned_data.get('country')
        profile.mobile_no = self.cleaned_data.get('mobile_no')
        profile.save()

        return user

"""

class UserProfile(models.Model):

    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    country = (
        ('SG','Singapore'),
    )

    country = models.CharField(max_length = 4, choices = country, default='SG')

    gender = (
        ('M', 'Female'),
        ('F', 'Male'),
    )

    gender = models.CharField(max_length = 2, choices = gender, default='F')

    # The additional attributes we wish to include.
    zip_code = models.CharField(max_length = 10)
    birthday = models.DateTimeField(null=True)
    home_address = models.TextField()
    mobile_no = models.CharField(max_length = 20)


"""
class UserProfileSerializer(serializers.ModelSerializer):

    country = serializers.CharField(source="userprofile.country", required=True)
    gender = serializers.CharField(source="userprofile.gender", required=True)
    zip_code = serializers.CharField(source="userprofile.zip_code")
    birthday = serializers.DateField(source="userprofile.birthday")
    home_address = serializers.CharField(source="userprofile.home_address", max_length=None)
    mobile_no = serializers.CharField(source="userprofile.mobile_no", required=True)

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('country', 'gender', 'zip_code','birthday', 'home_address', 'mobile_no', )
    
    def create(self, validated_data):
        
        #Create and return a new `AgentUserProfile` instance, given the validated data.
        
        profile = validated_data.pop('UserProfile')
        user = User.objects.create(**validated_data)

        return UserProfile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('UserProfile', {})
        country = profile_data.get('country')
        gender = profile_data.get('gender')
        zip_code = profile_data.get('zip_code')
        birthday = profile_data.get('birthday')
        home_address = profile_data.get('home_address')
        mobile_no = profile_data.get('mobile_no')

        instance = super(UserProfileSerializer, self).update(instance, validated_data)

        # get and update agent user profile
        profile = instance.userprofile

        if profile_data and country \
            and gender and zip_code and birthday \
            and home_address and mobile_no:

            profile.country = country
            profile.gender = gender
            profile.zip_code = zip_code
            profile.birthday = birthday
            profile.home_address = home_address
            profile.mobile_no = mobile_no
            
            profile.save()

        return instance