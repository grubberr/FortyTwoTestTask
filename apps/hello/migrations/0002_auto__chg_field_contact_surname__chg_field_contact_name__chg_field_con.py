# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Contact.surname'
        db.alter_column(u'hello_contact', 'surname', self.gf('django.db.models.fields.CharField')(max_length=256))

        # Changing field 'Contact.name'
        db.alter_column(u'hello_contact', 'name', self.gf('django.db.models.fields.CharField')(max_length=256))

        # Changing field 'Contact.skype'
        db.alter_column(u'hello_contact', 'skype', self.gf('django.db.models.fields.CharField')(max_length=256))

    def backwards(self, orm):

        # Changing field 'Contact.surname'
        db.alter_column(u'hello_contact', 'surname', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Contact.name'
        db.alter_column(u'hello_contact', 'name', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Contact.skype'
        db.alter_column(u'hello_contact', 'skype', self.gf('django.db.models.fields.CharField')(max_length=200))

    models = {
        u'hello.contact': {
            'Meta': {'object_name': 'Contact'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['hello']