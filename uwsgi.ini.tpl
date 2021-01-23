[uwsgi]

chdir		=	/opt/webapps/alab/wagtail_dev/mysite
module		=	mysite.wsgi:application
home		=	/opt/webapps/alab/wagtail_dev_env
virtualenv	=	/opt/webapps/alab/wagtail_dev_env

master		=	true
enable-threads	=	true
processes	=	4
socket		=	/opt/webapps/alab/wagtail_dev/uwsgi.sock
chmod-socket	=	664
vacuum		=	true
daemonize	=	/opt/webapps/alab/wagtail_dev/log/uwsgi.log
