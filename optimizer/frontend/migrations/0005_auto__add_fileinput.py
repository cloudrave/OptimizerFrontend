# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FileInput'
        db.create_table(u'frontend_fileinput', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('problem', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Problem'])),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'frontend', ['FileInput'])


    def backwards(self, orm):
        # Deleting model 'FileInput'
        db.delete_table(u'frontend_fileinput')


    models = {
        u'frontend.algorithm': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Algorithm'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'key': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '11'})
        },
        u'frontend.fileinput': {
            'Meta': {'ordering': "('order',)", 'object_name': 'FileInput'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'problem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Problem']"})
        },
        u'frontend.input': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Input'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'problem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Problem']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'frontend.jarfile': {
            'Meta': {'object_name': 'JarFile'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'frontend.problem': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Problem'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'is_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'key': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '11'})
        },
        u'frontend.solution': {
            'Meta': {'object_name': 'Solution'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prob': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Problem']"}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['frontend']