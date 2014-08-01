# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Application'
        db.delete_table(u'oauth2_provider_application')

        # Adding model 'Application'
        db.create_table(u'oauth2_provider_application', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('client_id', self.gf('django.db.models.fields.CharField')(default=u'ceeyfdYph0Yp3Rp@z41W?;6@VbOI08pk7YvSY??m', unique=True, max_length=100)),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=24, blank=True)),
            ('redirect_uris', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('client_type', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('authorization_grant_type', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('client_secret', self.gf('django.db.models.fields.CharField')(default=u'cnp-:2TeYe@hz=YA:eyldYvmJ1_P9SRCi3oAL_DQ8kN2MGJRWLi-_c1vd5o:X2bcbRo9_p!uOiHqzKX-XIkU6olpSwwG2vw=Li!dxYyufn@Sl9!ly?=OBim3:6Ug4FqE', max_length=255, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'oauth2_provider', ['Application'])


        # Renaming column for 'RefreshToken.user' to match new field type.
        db.rename_column(u'oauth2_provider_refreshtoken', 'user_id', 'user')
        # Changing field 'RefreshToken.user'
        db.alter_column(u'oauth2_provider_refreshtoken', 'user', self.gf('django.db.models.fields.CharField')(max_length=24))
        # Removing index on 'RefreshToken', fields ['user']
        db.delete_index(u'oauth2_provider_refreshtoken', ['user_id'])


        # Renaming column for 'Grant.user' to match new field type.
        db.rename_column(u'oauth2_provider_grant', 'user_id', 'user')
        # Changing field 'Grant.user'
        db.alter_column(u'oauth2_provider_grant', 'user', self.gf('django.db.models.fields.CharField')(max_length=24))
        # Removing index on 'Grant', fields ['user']
        db.delete_index(u'oauth2_provider_grant', ['user_id'])


        # Renaming column for 'AccessToken.user' to match new field type.
        db.rename_column(u'oauth2_provider_accesstoken', 'user_id', 'user')
        # Changing field 'AccessToken.user'
        db.alter_column(u'oauth2_provider_accesstoken', 'user', self.gf('django.db.models.fields.CharField')(max_length=24))
        # Removing index on 'AccessToken', fields ['user']
        db.delete_index(u'oauth2_provider_accesstoken', ['user_id'])


    def backwards(self, orm):
        # Adding index on 'AccessToken', fields ['user']
        db.create_index(u'oauth2_provider_accesstoken', ['user_id'])

        # Adding index on 'Grant', fields ['user']
        db.create_index(u'oauth2_provider_grant', ['user_id'])

        # Adding index on 'RefreshToken', fields ['user']
        db.create_index(u'oauth2_provider_refreshtoken', ['user_id'])

        # Adding model 'Application'
        db.create_table(u'oauth2_provider_application', (
            ('redirect_uris', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('client_id', self.gf('django.db.models.fields.CharField')(default='30f17d266183cd455bc57ce8548a439db3491353', max_length=100, unique=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('client_secret', self.gf('django.db.models.fields.CharField')(default='18e68df61ad8e1af355644ddf6a636b269b6309aafbd2a34d4f5ed6c5562e44c0792c5b2441571e85cbf8a85249dca5537dedb6fd6f60e134f4a60f3865c8395', max_length=255, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('client_type', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('authorization_grant_type', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'oauth2_provider', ['Application'])

        # Deleting model 'Application'
        db.delete_table(u'oauth2_provider_application')


        # Renaming column for 'RefreshToken.user' to match new field type.
        db.rename_column(u'oauth2_provider_refreshtoken', 'user', 'user_id')
        # Changing field 'RefreshToken.user'
        db.alter_column(u'oauth2_provider_refreshtoken', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Renaming column for 'Grant.user' to match new field type.
        db.rename_column(u'oauth2_provider_grant', 'user', 'user_id')
        # Changing field 'Grant.user'
        db.alter_column(u'oauth2_provider_grant', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Renaming column for 'AccessToken.user' to match new field type.
        db.rename_column(u'oauth2_provider_accesstoken', 'user', 'user_id')
        # Changing field 'AccessToken.user'
        db.alter_column(u'oauth2_provider_accesstoken', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

    models = {
        u'oauth2_provider.accesstoken': {
            'Meta': {'object_name': 'AccessToken'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oauth2_provider.Application']"}),
            'expires': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scope': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '24'})
        },
        u'oauth2_provider.application': {
            'Meta': {'object_name': 'Application'},
            'authorization_grant_type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'client_id': ('django.db.models.fields.CharField', [], {'default': "u'dij!PGOa@W5nhV._y9UO_iTnuxauI=WjwDDTH7K4'", 'unique': 'True', 'max_length': '100'}),
            'client_secret': ('django.db.models.fields.CharField', [], {'default': "u'=bFK3:WUll!O?MLl;7=eJ3ChrJxHZ5_RpvFM=kT7aYj3eyZX8A!7RU@LKNe@HsYOab050tu?9Z6@K2rQMkb_J@04pJ::guuiOxhZX0lk7Ar??cjd-VotUC=F=ucIMEK9'", 'max_length': '255', 'blank': 'True'}),
            'client_type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'redirect_uris': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '24', 'blank': 'True'})
        },
        u'oauth2_provider.grant': {
            'Meta': {'object_name': 'Grant'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oauth2_provider.Application']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'expires': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'redirect_uri': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'scope': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '24'})
        },
        u'oauth2_provider.refreshtoken': {
            'Meta': {'object_name': 'RefreshToken'},
            'access_token': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'refresh_token'", 'unique': 'True', 'to': u"orm['oauth2_provider.AccessToken']"}),
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oauth2_provider.Application']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '24', 'blank': 'True'})
        }
    }

    complete_apps = ['oauth2_provider']