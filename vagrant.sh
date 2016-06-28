#!/bin/bash
# USE vagrant_1.8.1_x86_64   with   virtualbox-5.0_5.0.10-104061-Ubuntu-trusty_amd64
# vagrant plugin install vagrant-vbguest

# update / upgrade
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get install make mc curl git python-software-properties -y
#Install java8
su -
sudo echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee /etc/apt/sources.list.d/webupd8team-java.list
sudo echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886
apt-get update
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | sudo /usr/bin/debconf-set-selections
apt-get install -y oracle-java8-installer
sudo apt-get install oracle-java8-set-default


#Installing mysql server with root password
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password root'
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password root'
sudo apt-get -y install mysql-server
# Allow external access to mysql with username:password
sudo sed -i '/bind-address/ s/^/#/g' /etc/mysql/my.cnf
mysql -uroot -proot -e"CREATE USER 'username'@'%' IDENTIFIED BY 'password';"
mysql -uroot -proot -e"GRANT ALL PRIVILEGES ON *.* TO 'username'@'%' WITH GRANT OPTION"
sudo service mysql restart

#Elasticsearch 1.73 installation
wget https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.7.3.deb
sudo dpkg -i elasticsearch-1.7.3.deb
sudo /usr/share/elasticsearch/bin/plugin -install mobz/elasticsearch-head
sudo service elasticsearch start

# install apache 2.4 and php 5.5
sudo apt-get update
sudo apt-get install -y apache2


# restart apache
sudo service apache2 restart

#Installing pip
sudo apt-get install -y python-pip

#mysql client
sudo apt-get install libmysqlclient-dev -y

#python dev
sudo apt-get install python-dev -y

#Installing Flask
sudo pip install Flask

#elasticsearch module for py
sudo pip install elasticsearch

#elasticsearch dsl
sudo pip install elasticsearch_dsl

#flask mysql 
sudo pip install flask-mysqldb

#start elasrtic after halt
sudo update-rc.d elasticsearch defaults 95 10
sudo /etc/init.d/elasticsearch start

#Cleanup
sudo apt-get autoremove -y

echo "vagrant.sh is executed."
