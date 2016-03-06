clear

# Git.
echo "\n*** Make gitcongig ***"
ln -s ~/web/gitconfig ~/.gitconfig 

# Nginx.
echo "\n*** Configure nginx ***"
sudo rm /etc/nginx/sites-enabled/default 
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

# Gunicorn.
echo "\n*** Configure gunicorn ***"
sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart

# Mysql
echo "\n*** Configure Mysql ***"
echo "\tCreate table"
sudo mysql -uroot -e "CREATE DATABASE IF NOT EXISTS stepic;"
echo "\tCreate user"
sudo mysql -uroot -e "CREATE USER 'kirimaks'@'localhost' IDENTIFIED BY '1234';"
echo "\tChange privileges"
sudo mysql -uroot -e "GRANT ALL PRIVILEGES ON stepic.* to 'kirimaks'@'localhost';"
echo "\tFlush privileges"
sudo mysql -uroot -e "FLUSH PRIVILEGES;"
