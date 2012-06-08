# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Author'
        db.create_table('blog_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('blog', ['Author'])

        # Adding model 'Post'
        db.create_table('blog_post', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('blog', ['Post'])

        # Adding M2M table for field authors on 'Post'
        db.create_table('blog_post_authors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm['blog.post'], null=False)),
            ('author', models.ForeignKey(orm['blog.author'], null=False))
        ))
        db.create_unique('blog_post_authors', ['post_id', 'author_id'])

        # Adding model 'Galeria'
        db.create_table('blog_galeria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('blog', ['Galeria'])

        # Adding model 'Foto'
        db.create_table('blog_foto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('galeria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Galeria'])),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('blog', ['Foto'])


    def backwards(self, orm):
        
        # Deleting model 'Author'
        db.delete_table('blog_author')

        # Deleting model 'Post'
        db.delete_table('blog_post')

        # Removing M2M table for field authors on 'Post'
        db.delete_table('blog_post_authors')

        # Deleting model 'Galeria'
        db.delete_table('blog_galeria')

        # Deleting model 'Foto'
        db.delete_table('blog_foto')


    models = {
        'blog.author': {
            'Meta': {'object_name': 'Author'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'blog.foto': {
            'Meta': {'object_name': 'Foto'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'galeria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Galeria']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'blog.galeria': {
            'Meta': {'object_name': 'Galeria'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'blog.post': {
            'Meta': {'object_name': 'Post'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['blog.Author']", 'symmetrical': 'False'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['blog']
