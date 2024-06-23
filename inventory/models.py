# flake8: noqa
import json

from django.db.models import Model, BinaryField, DateField, ForeignKey, CharField, IntegerField, ManyToManyField, TextField, BooleanField, URLField, CASCADE
from core.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.conf import settings
from django.urls import reverse


def uri(name, *args):
    domain = settings.ACTIVITYPUB_DOMAIN
    path = reverse(name, args=args)
    return "http://{domain}{path}".format(domain=domain, path=path)


class URIs(object):
    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)


class Organization(Model):
    name = CharField(max_length=255)
    description = TextField(blank=True)
    website = URLField(blank=True)
    street_line_1 = CharField(max_length=255)
    street_line_2 = CharField(max_length=255, blank=True)
    city = CharField(max_length=80)
    state = CharField(max_length=80)
    zipcode = CharField(max_length=10)

    def __str__(self):
        return self.name


class Person(Model):
    ap_id = TextField(null=True)
    remote = BooleanField(default=False)

    username = CharField(max_length=100)
    name = CharField(max_length=100)
    following = ManyToManyField('self', symmetrical=False, related_name='followers')

    @property
    def uris(self):
        if self.remote:
            return URIs(id=self.ap_id)

        return URIs(
            id=uri("person", self.username),
            following=uri("following", self.username),
            followers=uri("followers", self.username),
            outbox=uri("outbox", self.username),
            inbox=uri("inbox", self.username),
        )

    def to_activitystream(self):
        json = {
            "type": "Person",
            "id": self.uris.id,
            "name": self.name,
            "preferredUsername": self.username,
        }

        if not self.remote:
            json.update({
                "following": self.uris.following,
                "followers": self.uris.followers,
                "outbox": self.uris.outbox,
                "inbox": self.uris.inbox,
            })
        return json


class Product(Model):
    name = CharField(max_length=200)

    def __str__(self):
        return self.name


class QuantitativeUnit(Model):
    name = CharField(max_length=20)

    def __str__(self):
        return self.name


class InventoryItem(Model):
    product = ForeignKey(Product, on_delete=CASCADE)
    expiration_date = DateField(null=True, blank=True, auto_now_add=False)
    person = ManyToManyField(User)
    quantity = IntegerField(default=0)
    unit = ForeignKey(QuantitativeUnit, on_delete=CASCADE, blank=True, default='')
    ordering_fields = ['expiration_date']
    ordering = ['expiration_date']

    def __str__(self):
        return self.product.name


class Note(Model):
    ap_id = TextField(null=True)
    remote = BooleanField(default=False)

    person = ForeignKey(Person, related_name='notes', on_delete=CASCADE)
    content = CharField(max_length=500)
    likes = ManyToManyField(Person, related_name='liked')

    @property
    def uris(self):
        if self.remote:
            ap_id = self.ap_id
        else:
            ap_id = uri("note", self.person.username, self.id)
        return URIs(id=ap_id)

    def to_activitystream(self):
        return {
            "type": "Note",
            "id": self.uris.id,
            "content": self.content,
            "actor": self.person.uris.id,
        }


class Activity(Model):

    ap_id = TextField()
    payload = BinaryField()
    created_at = DateField(auto_now_add=True)
    person = ForeignKey(Person, related_name='activities', on_delete=CASCADE)
    remote = BooleanField(default=False)

    @property
    def uris(self):
        if self.remote:
            ap_id = self.ap_id
        else:
            ap_id = uri("activity", self.person.username, self.id)
        return URIs(id=ap_id)

    def to_activitystream(self):
        payload = self.payload.decode("utf-8")
        data = json.loads(payload)
        data.update({
            "id": self.uris.id
        })
        return data


@receiver(post_save, sender=Person)
@receiver(post_save, sender=Note)
@receiver(post_save, sender=Activity)
def save_ap_id(sender, instance, created, **kwargs):
    if created and not instance.remote:
        instance.ap_id = instance.uris.id
        instance.save()
