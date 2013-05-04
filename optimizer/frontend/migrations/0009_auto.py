# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field functional_algorithms on 'Problem'
        db.create_table(u'frontend_problem_functional_algorithms', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('problem', models.ForeignKey(orm[u'frontend.problem'], null=False)),
            ('algorithm', models.ForeignKey(orm[u'frontend.algorithm'], null=False))
        ))
        db.create_unique(u'frontend_problem_functional_algorithms', ['problem_id', 'algorithm_id'])


    def backwards(self, orm):
        # Removing M2M table for field functional_algorithms on 'Problem'
        db.delete_table('frontend_problem_functional_algorithms')


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
            'default_value': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'problem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Problem']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
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
            'functional_algorithms': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['frontend.Algorithm']", 'symmetrical': 'False'}),
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