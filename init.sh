sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/gask.conf /etc/gunicorn.d/test
sudo /etc/init.d/nginx restart
sudo /etc/init.d/gunicorn restart

