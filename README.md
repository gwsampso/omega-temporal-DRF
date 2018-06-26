# Omega Temporal DRF (Django Rest Framework)
Temporal data support for the Django DRF.

Any change in an object is implemented in three steps. 
1) Create a copy of the unchanged record - new_record 
2) Terminate old_record  - setting VFlag to 0 and VT to Current Time 
2) Update new_record with validated data

All temporal objects have the following fields:
VF (valid from), VT (valid to), VFlag (verson flag 1 = current, 0 = old), VU (user)

All Database Models must inherit from either TemporalModelManualDjangoID or TemporalModel