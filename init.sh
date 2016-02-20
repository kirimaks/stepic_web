# Git.
ln -s ~/web/gitconfig ~/.gitconfig 

# Nginx.
sudo rm /etc/nginx/sites-enabled/default 
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

# Gunicorn.
sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
