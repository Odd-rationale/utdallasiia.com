from utdallasiia.apps.members import signals
from south.modelsinspector import add_introspection_rules

add_introspection_rules([], ["^django_localflavor_us\.models\.USStateField"])
add_introspection_rules([], ["^django_localflavor_us\.models\.USPostalCodeField"])
add_introspection_rules([], ["^django_localflavor_us\.models\.PhoneNumberField"])
