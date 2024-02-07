from icecream import ic

from neomodel import (config, StructuredNode, StringProperty, IntegerProperty, BooleanProperty,
    UniqueIdProperty, RelationshipTo)

config.DATABASE_URL = 'bolt://neo4j:newPassword@localhost:7687'


class ContactInfo(StructuredNode):
    uid = UniqueIdProperty()
    isPrimary = BooleanProperty(required=True)
    address = StringProperty(unique_index=True, required=False)
    email = StringProperty(unique_index=True, required=False)
    phone = StringProperty(unique_index=True, required=False)

class Organization(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(required=True)
    contact = RelationshipTo(ContactInfo, 'CONTACT_INFO')

class Household(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    contact = RelationshipTo(ContactInfo, 'CONTACT_INFO')

class Contribution(StructuredNode):
    uid = UniqueIdProperty()
    amount = IntegerProperty(required=True)
    recipient = RelationshipTo(Organization, 'CONTRIBUTED_TO')
    giver = RelationshipTo(Organization, 'CONTRIBUTED_BY')

class Person(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(required=True)
    org = RelationshipTo(Organization, 'IN_ORG')
    contact = RelationshipTo(ContactInfo, 'CONTACT_INFO')
    house = RelationshipTo(Household, 'FROM')

adam = Person(name='Adam Miller').save()
adam.save()
adam_contact = ContactInfo(
    address='123 Fake St',
    isPrimary=True,
).save()
adam.contact.connect(adam_contact)

miller_household = Household(name='Miller').save()
adam.house.connect(miller_household)

instil = Organization(name='Instil').save()
instil.contact.connect(adam_contact)
adam.org.connect(instil)

twloha = Organization(name='To Write Love On Her Arms').save()
twlo_founder = Person(name='Jamie Tworkowski').save()
jamie_contact = ContactInfo(
    address='456 Real St',
    isPrimary=True,
).save()
twloha.contact.connect(jamie_contact)

tworkowski_household = Household(name='Tworkowski').save()
tworkowski_household.contact.connect(jamie_contact)

adam_donation = Contribution(amount=100).save()
adam_donation.recipient.connect(twloha)
adam_donation.giver.connect(instil)
