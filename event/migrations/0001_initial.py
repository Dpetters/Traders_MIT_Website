# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Event'
        db.create_table('event_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 4, 29, 14, 32, 13, 466000), auto_now_add=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=85)),
            ('end_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('attending_employers', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('start_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('rsvp_message', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('remote_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('event', ['Event'])


    def backwards(self, orm):
        
        # Deleting model 'Event'
        db.delete_table('event_event')


    models = {
        'event.event': {
            'Meta': {'object_name': 'Event'},
            'attending_employers': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 4, 29, 14, 32, 13, 466000)', 'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '85'}),
            'remote_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'rsvp_message': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'start_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['event']
