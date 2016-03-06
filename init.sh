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
#echo "\tDrop table"
#sudo mysql -uroot -e "drop database if exists stepic;"
echo "\tCreate table"
sudo mysql -uroot -e "CREATE DATABASE IF NOT EXISTS stepic;"
echo "\tCreate user"
sudo mysql -uroot -e "create user 'kirimaks'@'localhost' identified by '1234';"
echo "\tChange privileges"
sudo mysql -uroot -e "grant all privileges on stepic to kirimaks;"
echo "\tFlush privileges"
sudo mysql -uroot -e "flush privileges;"
