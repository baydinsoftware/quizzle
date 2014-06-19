# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Quiz'
        db.create_table(u'quiz_quiz', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'quiz', ['Quiz'])

        # Adding model 'Question'
        db.create_table(u'quiz_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quiz', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quiz.Quiz'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'quiz', ['Question'])

        # Adding model 'Answer'
        db.create_table(u'quiz_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quiz.Question'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'quiz', ['Answer'])

        # Adding model 'Result'
        db.create_table(u'quiz_result', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quiz', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quiz.Quiz'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('second_description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('votes', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'quiz', ['Result'])

        # Adding model 'Value'
        db.create_table(u'quiz_value', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('answer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quiz.Answer'])),
            ('result', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quiz.Result'])),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'quiz', ['Value'])

        # Adding model 'AsSecondResult'
        db.create_table(u'quiz_assecondresult', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('result', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['quiz.Result'], unique=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'quiz', ['AsSecondResult'])


    def backwards(self, orm):
        # Deleting model 'Quiz'
        db.delete_table(u'quiz_quiz')

        # Deleting model 'Question'
        db.delete_table(u'quiz_question')

        # Deleting model 'Answer'
        db.delete_table(u'quiz_answer')

        # Deleting model 'Result'
        db.delete_table(u'quiz_result')

        # Deleting model 'Value'
        db.delete_table(u'quiz_value')

        # Deleting model 'AsSecondResult'
        db.delete_table(u'quiz_assecondresult')


    models = {
        u'quiz.answer': {
            'Meta': {'object_name': 'Answer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quiz.Question']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'quiz.assecondresult': {
            'Meta': {'object_name': 'AsSecondResult'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'result': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['quiz.Result']", 'unique': 'True'})
        },
        u'quiz.question': {
            'Meta': {'object_name': 'Question'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quiz': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quiz.Quiz']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'quiz.quiz': {
            'Meta': {'object_name': 'Quiz'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'quiz.result': {
            'Meta': {'object_name': 'Result'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'quiz': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quiz.Quiz']"}),
            'second_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'quiz.value': {
            'Meta': {'object_name': 'Value'},
            'answer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quiz.Answer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'result': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quiz.Result']"}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['quiz']