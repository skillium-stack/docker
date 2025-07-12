# Use the official Ubuntu base image
FROM ubuntu:latest

# Set the working directory
WORKDIR /myappnode


# Update package list and install Apache
RUN apt-get update && \
    apt-get install -y apache2

# Output message for PHP installation
RUN echo "Installing PHP............" && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:ondrej/php -y && \
    apt-get update && \
    apt-get install -y php7.0 php5.6 php5.6-mysql php5.6-curl php5.6-xml php5.6-mbstring php-xdebug libapache2-mod-php5.6 libapache2-mod-php7.0 && \
    a2dismod php7.0 && a2enmod php5.6 && a2enmod rewrite && a2enmod headers && \
    a2enmod authn_dbm && a2enmod authn_dbd && a2enmod authz_groupfile && \
    a2enmod auth_digest && a2enmod socache_shmcb && a2enmod dbd && \
    a2enmod dav && a2enmod dav_fs && a2enmod vhost_alias && a2enmod expires && \
    service apache2 restart && \
    update-alternatives --set php /usr/bin/php5.6

# Install zip & unzip
RUN echo "Install zip & unzip.........." && \
    apt-get install -y zip && \
    apt-get install -y unzip

# Install expect
RUN echo "Installing expect.........." && \
    apt-get install -y expect

# Copy the code to /var/www/html
COPY . /var/www/html

# Grant necessary permissions
RUN chown -R www-data:www-data /var/www/html \
    && chmod -R 755 /var/www/html

# Expose port 80 for the Apache server
EXPOSE 80

# Enable .htaccess files by setting AllowOverride to All
RUN sed -i 's/AllowOverride None/AllowOverride All/' /etc/apache2/apache2.conf


# Start Apache service
CMD ["apachectl", "-D", "FOREGROUND"]
