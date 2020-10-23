from django.db import models
from accounts.models import Profile
from django.contrib.auth.models import User
import uuid
from django.contrib import messages
from django.urls import reverse
# Create your models here.

class Genre(models.Model):
    name=models.CharField(max_length=200,help_text="Enter a Genra(e.g Detective)")
    def __str__(self):
        return self.name

class Book(models.Model):
    
    title=models.CharField(max_length=200)
    author=models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)
    summary=models.TextField(max_length=1000,help_text="Enter a brief desciption of Book")
    isbn=models.CharField("ISBN",max_length=13,help_text="13 Character ISBN Number")
    genre=models.ManyToManyField(Genre,help_text="Select a genre for this book!")
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
class Reviews(models.Model):
    book=models.ForeignKey("Book",on_delete=models.PROTECT,db_constraint=False,null=True)
    Reviewuser=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    review=models.CharField(max_length=200)
    

class BookInstance(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,help_text="Unique ID")
    book=models.ForeignKey("Book",on_delete=models.PROTECT,db_constraint=False,null=True)
    imprint=models.CharField(max_length=200)
    due_back=models.DateField(null=True,blank=True)
    LOAN_STATUS =(
        ('a','Available'),
        ('r','Reserved'),
    )
    BookUser=models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    Languages=(
        ('ab', 'Abkhaz'),
        ('aa', 'Afar'),
        ('af', 'Afrikaans'),
        ('ak', 'Akan'),
        ('sq', 'Albanian'),
        ('am', 'Amharic'),
        ('ar', 'Arabic'),
        ('an', 'Aragonese'),
        ('hy', 'Armenian'),
        ('as', 'Assamese'),
        ('av', 'Avaric'),
        ('ae', 'Avestan'),
        ('ay', 'Aymara'),
        ('az', 'Azerbaijani'),
        ('bm', 'Bambara'),
        ('ba', 'Bashkir'),
        ('eu', 'Basque'),
        ('be', 'Belarusian'),
        ('bn', 'Bengali'),
        ('bh', 'Bihari'),
        ('bi', 'Bislama'),
        ('bs', 'Bosnian'),
        ('br', 'Breton'),
        ('bg', 'Bulgarian'),
        ('my', 'Burmese'),
        ('ca', 'Catalan; Valencian'),
        ('ch', 'Chamorro'),
        ('ce', 'Chechen'),
        ('ny', 'Chichewa; Chewa; Nyanja'),
        ('zh', 'Chinese'),
        ('cv', 'Chuvash'),
        ('kw', 'Cornish'),
        ('co', 'Corsican'),
        ('cr', 'Cree'),
        ('hr', 'Croatian'),
        ('cs', 'Czech'),
        ('da', 'Danish'),
        ('dv', 'Divehi; Maldivian;'),
        ('nl', 'Dutch'),
        ('dz', 'Dzongkha'),
        ('en', 'English'),
        ('eo', 'Esperanto'),
        ('et', 'Estonian'),
        ('ee', 'Ewe'),
        ('fo', 'Faroese'),
        ('fj', 'Fijian'),
        ('fi', 'Finnish'),
        ('fr', 'French'),
        ('ff', 'Fula'),
        ('gl', 'Galician'),
        ('ka', 'Georgian'),
        ('de', 'German'),
        ('el', 'Greek, Modern'),
        ('gn', 'Guaraní'),
        ('gu', 'Gujarati'),
        ('ht', 'Haitian'),
        ('ha', 'Hausa'),
        ('he', 'Hebrew (modern)'),
        ('hz', 'Herero'),
        ('hi', 'Hindi'),
        ('ho', 'Hiri Motu'),
        ('hu', 'Hungarian'),
        ('ia', 'Interlingua'),
        ('id', 'Indonesian'),
        ('ie', 'Interlingue'),
        ('ga', 'Irish'),
        ('ig', 'Igbo'),
        ('ik', 'Inupiaq'),
        ('io', 'Ido'),
        ('is', 'Icelandic'),
        ('it', 'Italian'),
        ('iu', 'Inuktitut'),
        ('ja', 'Japanese'),
        ('jv', 'Javanese'),
        ('kl', 'Kalaallisut'),
        ('kn', 'Kannada'),
        ('kr', 'Kanuri'),
        ('ks', 'Kashmiri'),
        ('kk', 'Kazakh'),
        ('km', 'Khmer'),
        ('ki', 'Kikuyu, Gikuyu'),
        ('rw', 'Kinyarwanda'),
        ('ky', 'Kirghiz, Kyrgyz'),
        ('kv', 'Komi'),
        ('kg', 'Kongo'),
        ('ko', 'Korean'),
        ('ku', 'Kurdish'),
        ('kj', 'Kwanyama, Kuanyama'),
        ('la', 'Latin'),
        ('lb', 'Luxembourgish'),
        ('lg', 'Luganda'),
        ('li', 'Limburgish'),
        ('ln', 'Lingala'),
        ('lo', 'Lao'),
        ('lt', 'Lithuanian'),
        ('lu', 'Luba-Katanga'),
        ('lv', 'Latvian'),
        ('gv', 'Manx'),
        ('mk', 'Macedonian'),
        ('mg', 'Malagasy'),
        ('ms', 'Malay'),
        ('ml', 'Malayalam'),
        ('mt', 'Maltese'),
        ('mi', 'Māori'),
        ('mr', 'Marathi (Marāṭhī)'),
        ('mh', 'Marshallese'),
        ('mn', 'Mongolian'),
        ('na', 'Nauru'),
        ('nv', 'Navajo, Navaho'),
        ('nb', 'Norwegian Bokmål'),
        ('nd', 'North Ndebele'),
        ('ne', 'Nepali'),
        ('ng', 'Ndonga'),
        ('nn', 'Norwegian Nynorsk'),
        ('no', 'Norwegian'),
        ('ii', 'Nuosu'),
        ('nr', 'South Ndebele'),
        ('oc', 'Occitan'),
        ('oj', 'Ojibwe, Ojibwa'),
        ('cu', 'Old Church Slavonic'),
        ('om', 'Oromo'),
        ('or', 'Oriya'),
        ('os', 'Ossetian, Ossetic'),
        ('pa', 'Panjabi, Punjabi'),
        ('pi', 'Pāli'),
        ('fa', 'Persian'),
        ('pl', 'Polish'),
        ('ps', 'Pashto, Pushto'),
        ('pt', 'Portuguese'),
        ('qu', 'Quechua'),
        ('rm', 'Romansh'),
        ('rn', 'Kirundi'),
        ('ro', 'Romanian, Moldavan'),
        ('ru', 'Russian'),
        ('sa', 'Sanskrit (Saṁskṛta)'),
        ('sc', 'Sardinian'),
        ('sd', 'Sindhi'),
        ('se', 'Northern Sami'),
        ('sm', 'Samoan'),
        ('sg', 'Sango'),
        ('sr', 'Serbian'),
        ('gd', 'Scottish Gaelic'),
        ('sn', 'Shona'),
        ('si', 'Sinhala, Sinhalese'),
        ('sk', 'Slovak'),
        ('sl', 'Slovene'),
        ('so', 'Somali'),
        ('st', 'Southern Sotho'),
        ('es', 'Spanish; Castilian'),
        ('su', 'Sundanese'),
        ('sw', 'Swahili'),
        ('ss', 'Swati'),
        ('sv', 'Swedish'),
        ('ta', 'Tamil'),
        ('te', 'Telugu'),
        ('tg', 'Tajik'),
        ('th', 'Thai'),
        ('ti', 'Tigrinya'),
        ('bo', 'Tibetan'),
        ('tk', 'Turkmen'),
        ('tl', 'Tagalog'),
        ('tn', 'Tswana'),
        ('to', 'Tonga'),
        ('tr', 'Turkish'),
        ('ts', 'Tsonga'),
        ('tt', 'Tatar'),
        ('tw', 'Twi'),
        ('ty', 'Tahitian'),
        ('ug', 'Uighur, Uyghur'),
        ('uk', 'Ukrainian'),
        ('ur', 'Urdu'),
        ('uz', 'Uzbek'),
        ('ve', 'Venda'),
        ('vi', 'Vietnamese'),
        ('vo', 'Volapük'),
        ('wa', 'Walloon'),
        ('cy', 'Welsh'),
        ('wo', 'Wolof'),
        ('fy', 'Western Frisian'),
        ('xh', 'Xhosa'),
        ('yi', 'Yiddish'),
        ('yo', 'Yoruba'),
        ('za', 'Zhuang, Chuang'),
        ('zu', 'Zulu'),
    )
    status=models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',

    )
    Lang=models.CharField(
        max_length=2,
        choices=Languages,
        blank=True,
        default='m',
        help_text='Languages',

    )
    class Meta:
        ordering=['due_back']

    def __str__(self):
         return f'{self.id}({self.book.title})'

class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    data_of_birth=models.DateField(null=True,blank=True)
    date_of_death=models.DateField('Died',null=True,blank=True)
    class Meta:
        ordering=['last_name','first_name']
    def __str__(self):
        return f'{self.last_name}{self.first_name}'
