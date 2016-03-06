clear

# Git.
echo "\n*** Make gitcongig ***"
git_config="$HOME/.gitconfig"
if [ ! -f $git_config ]; then
	ln -s $HOME/web/gitconfig $git_config
fi

# Nginx.
echo "\n*** Configure nginx ***"
old_config="/etc/nginx/sites-enabled/default"
if [ -f $old_config ]; then rm $old_config; fi
new_config="/etc/nginx/sites-enabled/test.conf"
if [ ! -f $new_config ]; then
	sudo ln -s /home/box/web/etc/nginx.conf $new_config 
fi
sudo /etc/init.d/nginx restart

# Gunicorn.
echo "\n*** Configure gunicorn ***"
guni_config="/etc/gunicorn.d/test"
if [ ! -f $guni_config ]; then 
	sudo ln -s /home/box/web/etc/gunicorn.conf $guni_config
fi
sudo /etc/init.d/gunicorn restart

# Mysql
echo "\n*** Configure Mysql ***"
sudo /etc/init.d/mysql restart
echo "\tCreate table"
sudo mysql -uroot -e "CREATE DATABASE IF NOT EXISTS stepic;"
echo "\tCreate user"
sudo mysql -uroot -e "CREATE USER 'kirimaks'@'localhost' IDENTIFIED BY '1234';"
echo "\tChange privileges"
sudo mysql -uroot -e "GRANT ALL PRIVILEGES ON stepic.* to 'kirimaks'@'localhost';"
echo "\tFlush privileges"
sudo mysql -uroot -e "FLUSH PRIVILEGES;"
