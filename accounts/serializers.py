from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор пользователя.
    """

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'registration_date')

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

    def update(self, instance, validated_data):

        instance.username = validated_data.get('username', instance.usernme)

        return instance


class UserRegisterSerializer(serializers.ModelSerializer):

    """
    Регистрация пользователя.
    """
    password = serializers.CharField(max_length=128, label='Введите пароль', write_only=True)
    password2 = serializers.CharField(max_length=128, label='Повторите пароль', write_only=True)

    class Meta:

        model = CustomUser
        fields = ('username', 'email', 'password', 'password2')

    def save(self, *args, **kwargs):

        user = CustomUser(
            email=self.validated_data['email'],
            username=self.validated_data.get('username', ''),
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({password: 'Пароль не совпадает'})

        user.set_password(password)
        user.save()
        return user
