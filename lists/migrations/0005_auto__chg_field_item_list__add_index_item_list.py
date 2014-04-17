# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'Item.list' to match new field type.
        db.rename_column(u'lists_item', 'list', 'list_id')
        # Changing field 'Item.list'
        db.alter_column(u'lists_item', 'list_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lists.List']))
        # Adding index on 'Item', fields ['list']
        db.create_index(u'lists_item', ['list_id'])


    def backwards(self, orm):
        # Removing index on 'Item', fields ['list']
        db.delete_index(u'lists_item', ['list_id'])


        # Renaming column for 'Item.list' to match new field type.
        db.rename_column(u'lists_item', 'list_id', 'list')
        # Changing field 'Item.list'
        db.alter_column(u'lists_item', 'list', self.gf('django.db.models.fields.TextField')())

    models = {
        u'lists.item': {
            'Meta': {'object_name': 'Item'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['lists.List']"}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"})
        },
        u'lists.list': {
            'Meta': {'object_name': 'List'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['lists']