# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'SchoolYear'
        db.create_table('core_schoolyear', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=42)),
            ('name_plural', self.gf('django.db.models.fields.CharField')(max_length=43, unique=True, null=True)),
        ))
        db.send_create_signal('core', ['SchoolYear'])

        # Adding model 'GraduationYear'
        db.create_table('core_graduationyear', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.PositiveSmallIntegerField')(unique=True)),
        ))
        db.send_create_signal('core', ['GraduationYear'])

        # Adding model 'Course'
        db.create_table('core_course', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=42)),
            ('num', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('sort_order', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('core', ['Course'])

        # Adding model 'BoardMember'
        db.create_table('core_boardmember', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal('core', ['BoardMember'])

        # Adding model 'ExecMember'
        db.create_table('core_execmember', (
            ('boardmember_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.BoardMember'], unique=True, primary_key=True)),
            ('profile_created', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('school_year', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.SchoolYear'], null=True, blank=True)),
            ('graduation_year', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.GraduationYear'], null=True, blank=True)),
            ('major', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='first_major', null=True, to=orm['core.Course'])),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 3, 3, 20, 39, 14, 430000))),
            ('left', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 3, 3, 20, 39, 14, 430000))),
        ))
        db.send_create_signal('core', ['ExecMember'])


    def backwards(self, orm):
        
        # Deleting model 'SchoolYear'
        db.delete_table('core_schoolyear')

        # Deleting model 'GraduationYear'
        db.delete_table('core_graduationyear')

        # Deleting model 'Course'
        db.delete_table('core_course')

        # Deleting model 'BoardMember'
        db.delete_table('core_boardmember')

        # Deleting model 'ExecMember'
        db.delete_table('core_execmember')


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
        'core.boardmember': {
            'Meta': {'object_name': 'BoardMember'},
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
            'Meta': {'object_name': 'ExecMember', '_ormbases': ['core.BoardMember']},
            'boardmember_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.BoardMember']", 'unique': 'True', 'primary_key': 'True'}),
            'graduation_year': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.GraduationYear']", 'null': 'True', 'blank': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 3, 3, 20, 39, 14, 430000)'}),
            'left': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 3, 3, 20, 39, 14, 430000)'}),
            'major': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'first_major'", 'null': 'True', 'to': "orm['core.Course']"}),
            'profile_created': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'school_year': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.SchoolYear']", 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'core.graduationyear': {
            'Meta': {'object_name': 'GraduationYear'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.PositiveSmallIntegerField', [], {'unique': 'True'})
        },
        'core.schoolyear': {
            'Meta': {'object_name': 'SchoolYear'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '42'}),
            'name_plural': ('django.db.models.fields.CharField', [], {'max_length': '43', 'unique': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['core']
