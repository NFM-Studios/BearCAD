from django.conf import settings

# List of available status options

MAKE_CHOICES = getattr(settings, 'MAKE_CHOICES', (
    (0, 'Albany'),
    (1, 'Annis'),
    (2, 'Benefactor'),
    (3, 'BF'),
    (4, 'Bollokan'),
    (5, 'Bravado'),
    (6, 'Brute'),
    (7, 'Buckingham'),
    (8, 'Canis'),
    (9, 'Chariot'),
    (10, 'Cheval'),
    (11, 'Classique'),
    (12, 'Coil'),
    (13, 'Desclasse'),
    (14, 'Dewbauchee'),
    (15, 'Dinka'),
    (16, 'DUDE'),
    (17, 'Dundreary'),
    (18, 'Emperor'),
    (19, 'Enus'),
    (20, 'Fathom'),
    (21, 'Gallivanter'),
    (22, 'Grotti'),
    (23, 'HVY'),
    (24, 'Hijack'),
    (25, 'Imponte'),
    (26, 'Invetero'),
    (27, 'Jacksheepe'),
    (28, 'JoBuilt'),
    (29, 'Karin'),
    (30, 'Kraken'),
    (31, 'Lampadati'),
    (32, 'Liberty City Cycles'),
    (33, 'Maibatsu Corporation'),
    (34, 'Mammoth'),
    (35, 'MTL'),
    (36, 'Nagasaki'),
    (37, 'Obey'),
    (38, 'Ocelot'),
    (39, 'Overflod'),
    (40, 'Pegassi'),
    (41, 'Pfister'),
    (42, 'Principle'),
    (43, 'Progen'),
    (44, 'Schyster'),
    (45, 'Shitzu'),
    (46, 'Speedophile'),
    (47, 'Stanley'),
    (48, 'Steel Horse'),
    (49, 'Tuffade'),
    (50, 'Ubermacht'),
    (51, 'Vapid'),
    (52, 'Vulcar'),
    (53, 'Weeny'),
    (54, 'Western Company'),
    (55, 'Western Motorcyle Company'),
    (56, 'Willard'),
    (57, 'Zirconium'),
    (58, 'None'),
))

MODEL_CHOICES = getattr(settings, 'MODEL_CHOICES', (


))

# List of the different status that define a ticket as closed.
#CLOSED_STATUSES = getattr(settings, 'TICKETS_CLOSED_STATUSES', (3, 4))
