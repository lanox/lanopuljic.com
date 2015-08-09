Title: Install Puppet Dashboard on CentOS 6.5
Date: 2014-05-20 23:10:23 +1000 
Category: Puppet
Tags: puppet,puppetdashboard,centOS 6.5
Author: Lano Puljic
Email: lano.puljic@gmail.com
Summary: Instructions on how to setup Puppet Dashboard on CentOS 6.5

Install Following Packages

```bash
yum -y install puppet-dashboard
```

Install MySQL

```bash
yum -y install mysql-server
```

Start service on next reboot
```bash
chkconfig mysqld on 3 4
service mysqld start
```

Set MySQL root user’s password
```bash
/usr/bin/mysqladmin -u root password 'new-password'
```

Create a database and database user:
```mysql
mysql -u root -p
mysql> CREATE DATABASE dashboard CHARACTER SET utf8;
mysql> CREATE USER 'dashboard'@'localhost' IDENTIFIED BY 'secret_password';
mysql> GRANT ALL PRIVILEGES ON dashboard.* TO 'dashboard'@'localhost';
```

Edit following config file and make changes to database,username,password you created in above step.

```bash
vi /usr/share/puppet-dashboard/config/database.yml

```

```yaml
production:
database: dashboard
username: dashboard
password: secret_password
encoding: utf8
adapter: mysql
 
development:
database: dashboard
username: dashboard
password: secret_password
encoding: utf8
adapter: mysql
```

Populate the database
```bash
cd /usr/share/puppet-dashboard
```

```ruby
rake db:migrate
```

Copy Apache vhost config file from the example Puppet Dashboard that is provided.

```bash
cp /usr/share/puppet-dashboard/ext/passenger/dashboard-vhost.conf /etc/httpd/conf.d/puppetdashboard.conf
```

Edit the puppetdashboar.conf file and change things to suite your environment.

```bash
vi /etc/https/conf.d/puppetdashboard.conf
```

Example of my configuration file is below.
```apache
# you may want to tune these settings
PassengerHighPerformance on
PassengerMaxPoolSize 12
PassengerPoolIdleTime 1500
# PassengerMaxRequests 1000
PassengerStatThrottleRate 120

Listen 3000
<VirtualHost *:3000>
        ServerName puppetmaster01.xonal.dev.com
        DocumentRoot /usr/share/puppet-dashboard/public/
        <Directory /usr/share/puppet-dashboard/public/>
                Options None
                Order allow,deny
                allow from all
        </Directory>
  ErrorLog /var/log/httpd/dashboard.example.com_error.log
  LogLevel warn
  CustomLog /var/log/httpd/dashboard.example.com_access.log combined
  ServerSignature On

</VirtualHost>
```

####Create logs for Dashboard

Make sure that log file exists and permissions are correct.
```bash
touch /usr/share/puppet-dashboard/log/production.log
chmod 0666 /usr/share/puppet-dashboard/log/production.log
```

Restart the https service
```bash
service httpd restar
```

If ther is no any errors you should be able to load puppet dashboard.

###Enable inventory support

When you add a node to puppet, Click on the node and you will see **INVENTORY** at first this will not display anything,
if you follow the instruction below you will get inventory working.

In a nutshell, you need to change just a few settings.

Go to settings.yml and change:

```yaml 
vi /usr/share/puppet-dashboard/config/settings.yml
```

Ensure that /usr/share/puppet-dashboard/config/settings.yaml has following
```yaml
# Hostname of the certificate authority.
ca_server: 'puppetmaster01.xonal.dev.com' # this is your puppetmaster FQDN

# The "inventory service" allows you to connect to a puppet master to retrieve and node facts
enable_inventory_service: true

# Hostname of the inventory server.
inventory_server: 'puppetmaster01.xonal.dev.com' # this is your puppetmaster FQDN
```

Make sure that service puppet-dashboard-workers is started on boot
```bash
chkconfig puppet-dashboard-workers on 34
service puppet-dashboard-workers start
```

Last but not lease make sure you have following in you /etc/puppet/puppet.conf

```bash
vi /etc/puppet/puppet.conf
```
```puppet
[master]
    reports = store, http
    reportdir = /var/lib/puppet/reports
    reporturl = http://puppetmaster01.xonal.dev.com:3000/reports/upload
```

####Configuring inventory to work on Puppet Dashboard

Edit auth.conf file

```bash
vi/etc/puppet/auth.conf file
```

Add follwoing lines.
```
path /facts
auth yes
method find, search
allow dashboard

Make sure its above this
path /
auth any
```

Generating Certificate for Dashboard so that NODE Inventory will work.

Generate your keypair for dashboard:

```bash
sudo -u puppet-dashboard rake cert:create_key_pair
```

Generate the cert request for dashboard:

```bash
sudo -u puppet-dashboard rake cert:request
```

On the puppetmaster, sign the cert:

```puppet
puppet cert sign dashboard
```

Get the cert from the puppetmaster

```bash
sudo -u puppet-dashboard rake cert:retrieve
```

Restart dashboard
```bash
service httpd restart
```

TA DA Loging to dashboard and see if it works.
