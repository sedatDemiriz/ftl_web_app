from django.db import models as m
from django.contrib.auth.models import User

# Static Models, content shouldn't be changed by users
class FTL_Ship(m.Model):

    UNKNOWN_SHIP = 'Unknown Ship'
    UNKNOWN_SHIP_NAME = 'Unknown Ship Name'
    
    designation = m.CharField(max_length=20, default=UNKNOWN_SHIP) # Kestrel A, Fed B, Engi C etc.
    name = m.CharField(max_length=30, default=UNKNOWN_SHIP_NAME) # ship name string, not important
    # systems = m.CharField(max_length=30) # list of systems the ship comes with (JSONField)
    # weapons = m.CharField(max_length=500) # make a jsondump when populating this or (JSONField)

    def __str__(self):
        return f"{self.designation}: {self.name}"

class FTL_Weapon(m.Model):
    name = m.CharField(max_length=50) # Weapon name
    price = m.IntegerField() # in-game purchase price in scrap
    _type = m.CharField(max_length=50) # beam, projectile, bomb, missile
    power = m.IntegerField() # power requirement
    projectile_count = m.IntegerField() # number of shots
    description = m.CharField(max_length=200) # notes

class FTL_Augment(m.Model):
    name = m.CharField(max_length=50) # Augment name
    price = m.IntegerField() # in-game purchase price in scrap
    description = m.CharField(max_length=200) # notes

class FTL_Crew(m.Model):
    race = m.CharField(max_length=50) # all races in the game
    attributes = m.CharField(max_length=200) # attributes, notes
    description = m.CharField(max_length=200) # notes

class FTL_System(m.Model):
    name = m.CharField(max_length=50) # System name
    price = m.IntegerField() # in-game purchase price in scrap
    description = m.CharField(max_length=200) # notes

# Dynamic Models, additions made from users submitting runs through front-end
class User_Submitted_Run(m.Model):

    HARD = 'Hard'
    NORMAL = 'Normal'
    EASY = 'Easy'
    DIFFICULTY_CHOICES = [
        (HARD, HARD),
        (NORMAL, NORMAL),
        (EASY, EASY),
    ]

    WIN = 'Win'
    LOSS = 'Loss'
    RESULT_CHOICES = [
        (WIN, WIN),
        (LOSS, LOSS),
    ]

    SHIPS_LIST = FTL_Ship.objects.all()
    SHIP_CHOICES = [(ship.designation, ship.designation) for ship in SHIPS_LIST]

    username = m.CharField(max_length=50) # from registered users
    ship_used = m.CharField(max_length=20, choices=SHIP_CHOICES, default=FTL_Ship.UNKNOWN_SHIP) # from ftl_ships
    difficulty = m.CharField(max_length=6, choices=DIFFICULTY_CHOICES, default=NORMAL) # selected difficulty of the run
    result = m.CharField(max_length=10, choices=RESULT_CHOICES, default=LOSS) # win/loss
    scrap_collected = m.IntegerField() # total scrap collected, according to FTL
    beacons_explored = m.IntegerField() # unique beacons visited, according to FTL
    ships_defeated = m.IntegerField() # enemy ships killed, according to FTL
    crew_hired = m.IntegerField() # crew received, according to FTL
    score = m.IntegerField() # final score for run, according to FTL
    datetime = m.DateTimeField(auto_now=True) # date and time of run
    metadata = m.CharField(max_length=50) # json with whole-run info?
    
    def __str__(self):
        return f"{self.difficulty} {self.ship_used} {self.result} by {self.username} on {self.datetime_shorthand()}"

    def datetime_shorthand(self):
        return str(self.datetime).split('.')[0]

class Community_Announcement(m.Model):
    title = m.CharField(max_length=50) # title for announcement
    author = m.CharField(max_length=50) # from registered users
    datetime = m.DateTimeField() # date of posting
    content = m.CharField(max_length=300) # how to do markdown?

    def __str__(self):
        return f"Announcement titled \"{self.title}\" by {self.author} at {self.datetime_shorthand()}"

    def datetime_shorthand(self):
        return str(self.datetime).split('+')[0]

class Community_Guide(m.Model):
    title = m.CharField(max_length=50) # title for guide
    author = m.CharField(max_length=50) # from registered users
    datetime = m.DateTimeField() # date of posting
    content = m.CharField(max_length=300) # how to do markdown? JSONfield?

class FTL_Game_Update(m.Model):
    title = m.CharField(max_length=50) # title for update
    author = m.CharField(max_length=50) # from registered admins?
    datetime = m.DateTimeField() # date of update
    content = m.CharField(max_length=300) # how to do markdown?

class FTL_Bingo_Squares(m.Model):
    text = m.CharField(max_length=200)
    author = m.ForeignKey(User, on_delete=m.CASCADE)