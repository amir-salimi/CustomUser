from rest_framework import serializers

from django.contrib.auth import get_user_model, login, authenticate

from rest_framework.exceptions import ValidationError, AuthenticationFailed

User = get_user_model()

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "phone", "password",]

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', "email", "password", "phone"]
        extra_kwargs = {
            'password': {"write_only" : True}
        }

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(
        label=("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        max_length=128,
        write_only=True
    )

    class Meta:
        model = User
        fileds = ["email", "password"]

    def validate(self, data):
        email = data["email"]
        password = data["password"]
        if email and password :
            username = User.objects.get(email=email)
            try:
                user = authenticate(request=self.context.get('request'), username=username.username, password=password)
            except:
                user = None
            if user is not None:
                login(self.context.get('request'), user)
            else:
                raise AuthenticationFailed
        else:
            raise AuthenticationFailed

        data['user'] = user
        return data
