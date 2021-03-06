# encoding: utf-8
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Adding field 'Device.health_status'
        db.add_column('lava_scheduler_app_device', 'health_status', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'Device.last_health_report_job'
        db.add_column('lava_scheduler_app_device', 'last_health_report_job', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'Health Report Job', unique=True, null=True, to=orm['lava_scheduler_app.TestJob']), keep_default=False)

    def backwards(self, orm):

        # Deleting field 'Device.health_status'
        db.delete_column('lava_scheduler_app_device', 'health_status')

        # Deleting field 'Device.last_health_report_job'
        db.delete_column('lava_scheduler_app_device', 'last_health_report_job_id')

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
        'lava_scheduler_app.device': {
            'Meta': {'object_name': 'Device'},
            'current_job': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lava_scheduler_app.TestJob']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'device_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lava_scheduler_app.DeviceType']"}),
            'health_status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '200', 'primary_key': 'True'}),
            'last_health_report_job': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'Health Report Job'", 'unique': 'True', 'null': 'True', 'to': "orm['lava_scheduler_app.TestJob']"}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lava_scheduler_app.Tag']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'lava_scheduler_app.devicestatetransition': {
            'Meta': {'object_name': 'DeviceStateTransition'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'device': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'transitions'", 'to': "orm['lava_scheduler_app.Device']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lava_scheduler_app.TestJob']", 'null': 'True', 'blank': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'new_state': ('django.db.models.fields.IntegerField', [], {}),
            'old_state': ('django.db.models.fields.IntegerField', [], {})
        },
        'lava_scheduler_app.devicetype': {
            'Meta': {'object_name': 'DeviceType'},
            'name': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'primary_key': 'True', 'db_index': 'True'})
        },
        'lava_scheduler_app.tag': {
            'Meta': {'object_name': 'Tag'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'lava_scheduler_app.testjob': {
            'Meta': {'object_name': 'TestJob'},
            'actual_device': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'+'", 'null': 'True', 'blank': 'True', 'to': "orm['lava_scheduler_app.Device']"}),
            'definition': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log_file': ('django.db.models.fields.files.FileField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'requested_device': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'+'", 'null': 'True', 'blank': 'True', 'to': "orm['lava_scheduler_app.Device']"}),
            'requested_device_type': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'+'", 'null': 'True', 'blank': 'True', 'to': "orm['lava_scheduler_app.DeviceType']"}),
            'results_link': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'submit_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'submit_token': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['linaro_django_xmlrpc.AuthToken']", 'null': 'True', 'blank': 'True'}),
            'submitter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lava_scheduler_app.Tag']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'linaro_django_xmlrpc.authtoken': {
            'Meta': {'object_name': 'AuthToken'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_used_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'secret': ('django.db.models.fields.CharField', [], {'default': "'wxahi36scmitudt29p0u6qx6ktiq2d0od7uuq0ptklddiiayy1g1yf24p51qlbgbsns74dfdq0bwzz1uh0o4ps5981c2eu0hdrix0smnz4sftf9uros2z002t7gttc5h'", 'unique': 'True', 'max_length': '128'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'auth_tokens'", 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['lava_scheduler_app']
