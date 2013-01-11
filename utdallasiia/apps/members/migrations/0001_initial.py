# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DegreePlan'
        db.create_table('members_degreeplan', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('degree', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('members', ['DegreePlan'])

        # Adding model 'MemberProfile'
        db.create_table('members_memberprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('netid', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('phone_number', self.gf('django_localflavor_us.models.PhoneNumberField')(max_length=20)),
            ('street_address', self.gf('django.db.models.fields.CharField')(max_length=95)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('state', self.gf('django_localflavor_us.models.USStateField')(max_length=2)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('tshirt_size', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('classification', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('graduation_month', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('graduation_year', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('citizen_resident', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('is_student', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_employer', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_current', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_paid', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('members', ['MemberProfile'])

        # Adding M2M table for field degree_plans on 'MemberProfile'
        db.create_table('members_memberprofile_degree_plans', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('memberprofile', models.ForeignKey(orm['members.memberprofile'], null=False)),
            ('degreeplan', models.ForeignKey(orm['members.degreeplan'], null=False))
        ))
        db.create_unique('members_memberprofile_degree_plans', ['memberprofile_id', 'degreeplan_id'])


    def backwards(self, orm):
        # Deleting model 'DegreePlan'
        db.delete_table('members_degreeplan')

        # Deleting model 'MemberProfile'
        db.delete_table('members_memberprofile')

        # Removing M2M table for field degree_plans on 'MemberProfile'
        db.delete_table('members_memberprofile_degree_plans')


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
        'members.degreeplan': {
            'Meta': {'object_name': 'DegreePlan'},
            'degree': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'members.memberprofile': {
            'Meta': {'object_name': 'MemberProfile'},
            'citizen_resident': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'classification': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'degree_plans': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['members.DegreePlan']", 'symmetrical': 'False'}),
            'graduation_month': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'graduation_year': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_employer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_paid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_student': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'netid': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone_number': ('django_localflavor_us.models.PhoneNumberField', [], {'max_length': '20'}),
            'state': ('django_localflavor_us.models.USStateField', [], {'max_length': '2'}),
            'street_address': ('django.db.models.fields.CharField', [], {'max_length': '95'}),
            'tshirt_size': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['members']