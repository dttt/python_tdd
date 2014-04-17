# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Item.list'
        db.add_column(u'lists_item', 'list',
                      self.gf('django.db.models.fields.TextField')(default='1'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Item.list'
        db.delete_column(u'lists_item', 'list')


    models = {
        u'lists.item': {
            'Meta': {'object_name': 'Item'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list': ('django.db.models.fields.TextField', [], {'default': "'1'"}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"})
        },
        u'lists.list': {
            'Meta': {'object_name': 'List'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['lists']