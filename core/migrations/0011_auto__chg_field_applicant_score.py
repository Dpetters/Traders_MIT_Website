# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Applicant.score'
        db.alter_column('core_applicant', 'score', self.gf('django.db.models.fields.IntegerField')())


    def backwards(self, orm):
        
        # Changing field 'Applicant.score'
        db.alter_column('core_applicant', 'score', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=3))


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.applicant': {
            'Meta': {'object_name': 'Applicant'},
            'applicantPoll': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ApplicantPoll']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'graduation_year': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.GraduationYear']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'major': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Course']", 'null': 'True', 'blank': 'True'}),
            'negatives': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'positives': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'core.applicantpoll': {
            'Meta': {'object_name': 'ApplicantPoll'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'completed_by': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.ExecMember']", 'symmetrical': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'core.boardmember': {
            'Meta': {'ordering': "['user__first_name']", 'object_name': 'BoardMember'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'core.course': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'Course'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '42'}),
            'num': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'sort_order': ('django.db.models.fields.FloatField', [], {})
        },
        'core.execmember': {
            'Meta': {'ordering': "['user__first_name']", 'object_name': 'ExecMember', '_ormbases': ['core.BoardMember']},
            'blurb': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'boardmember_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.BoardMember']", 'unique': 'True', 'primary_key': 'True'}),
            'co_president': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'graduation_year': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.GraduationYear']", 'null': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 20, 21, 38, 37, 960116)'}),
            'left': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'major': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'first_major'", 'null': 'True', 'to': "orm['core.Course']"}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'core.graduationyear': {
            'Meta': {'object_name': 'GraduationYear'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.PositiveSmallIntegerField', [], {'unique': 'True'})
        }
    }

    complete_apps = ['core']
