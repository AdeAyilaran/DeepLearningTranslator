from peewee import Model, SqliteDatabase, CharField, TextField

# Name of the database, created using a Sqlite backend framework
db = SqliteDatabase('translations.db')


class TranslationModel(Model):
    text = TextField()
    base_lang = CharField()
    final_lang = CharField()
    translation = TextField(null=True)

    # Basically instructing to store the database using the above model
    class Meta:
        database = db

db.create_tables([TranslationModel])
