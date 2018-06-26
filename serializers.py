from rest_framework import serializers

from datetime import datetime
from django.utils import timezone
from django.utils.timezone import utc


TIME_CURRENT = datetime.max.replace(tzinfo=utc)

class TemporalModelNoDjagoSerializer(serializers.ModelSerializer):
    vf = serializers.HiddenField(default=timezone.now())
    vt = serializers.HiddenField(default=TIME_CURRENT)
    vflag = serializers.HiddenField(default=1)
    vu = serializers.HiddenField(default='Theodore')

    class Meta:
		model = None
		fields = '__all__'

    def create(self, validated_data):
        self.djangoid = self.Meta.model.objects.order_by(
            'djangoid').last().djangoid + 1
        validated_data['vu'] = 'dashboard'
        validated_data['djangoid'] = self.Meta.model.objects.order_by(
            'djangoid').last().djangoid + 1

        return self.Meta.model.objects.create(**validated_data)

    def update(self, instance, validated_data):

        time_now = timezone.now()

        old_record = {}
        new_record = {}

        for (key, value) in validated_data.items():
            old_record[key] = getattr(instance, key)
            new_record[key] = validated_data[key]
            setattr(instance, key, value)

        old_record['vt'] = time_now
        old_record['vflag'] = 0
        new_record['vf'] = time_now

        # TODO: change for real user
        new_record['vu'] = 'dashboard'

        self.Meta.model.objects.filter(
            pk=instance.pk, vflag=1).update(**new_record)

        self.delete_me(old_record)

        return instance

    def delete_me(self, old_record):
        obj = self.Meta.model.objects.create(**old_record)


class TemporalModelSerializer(serializers.ModelSerializer):
    vf = serializers.HiddenField(default=timezone.now())
    vt = serializers.HiddenField(default=TIME_CURRENT)
    vflag = serializers.HiddenField(default=1)
    vu = serializers.HiddenField(default='Theodore')

    class Meta:
		model = None
		fields = '__all__'

    def create(self, validated_data):
        # TODO: change for real user
        validated_data['vu'] = 'dashboard'
        return self.Meta.model.objects.create(**validated_data)

    def update(self, instance, validated_data):

        time_now = timezone.now()

        old_record = {}
        new_record = {}

        for (key, value) in validated_data.items():
            old_record[key] = getattr(instance, key)
            new_record[key] = validated_data[key]
            setattr(instance, key, value)

        old_record['vt'] = time_now
        old_record['vflag'] = 0
        new_record['vf'] = time_now

        # TODO: change for real user
        new_record['vu'] = 'dashboard'

        self.Meta.model.objects.filter(
            pk=instance.pk, vflag=1).update(**new_record)

        self.delete_me(old_record)

        return instance

    def delete_me(self, old_record):
        obj = self.Meta.model.objects.create(**old_record)


class TemporalHyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    vf = serializers.HiddenField(default=timezone.now())
    vt = serializers.HiddenField(default=TIME_CURRENT)
    vflag = serializers.HiddenField(default=1)
    vu = serializers.HiddenField(default='Theodore')

    class Meta:
        model = None
        fields = '__all__'

    def create(self, validated_data):
        # TODO: change for real user
        # validated_data['vu'] = self.context['request'].user.username
        validated_data['vu'] = 'dashboard'
        return self.Meta.model.objects.create(**validated_data)

    def update(self, instance, validated_data):

        time_now = timezone.now()

        old_record = {}
        new_record = {}

        for (key, value) in validated_data.items():
            old_record[key] = getattr(instance, key)
            new_record[key] = validated_data[key]
            setattr(instance, key, value)

        old_record['vt'] = time_now
        old_record['vflag'] = 0
        new_record['vf'] = time_now

        # TODO: change for real user
        # new_record['vu'] = self.context['request'].user.username
        new_record['vu'] = 'dashboard'

        self.Meta.model.objects.filter(
            pk=instance.pk, vflag=1).update(**new_record)

        self.delete_me(old_record)

        return instance

    def delete_me(self, old_record):
        obj = self.Meta.model.objects.create(**old_record)
