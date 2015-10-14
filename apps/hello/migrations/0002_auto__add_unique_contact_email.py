# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Contact', fields ['email']
        db.create_unique(u'hello_contact', ['email'])


    def backwards(self, orm):
        # Removing unique constraint on 'Contact', fields ['email']
        db.delete_unique(u'hello_contact', ['email'])


    models = {
        u'hello.contact': {
            'Meta': {'object_name': 'Contact'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['hello']