# Use an official PHP runtime as a parent image
FROM php:7.4-apache

# Install the mysqli extension
RUN docker-php-ext-install mysqli


# Add www-data user to the Docker group to avoid permission issues
RUN groupadd -r docker && usermod -aG docker www-data

# Set the working directory in the container
WORKDIR /var/www/html

# Copy the current directory contents into the container at /var/www/html
COPY . .

# Set permissions (optional, but recommended)
RUN chown -R www-data:www-data /var/www/html

# Expose port 80
EXPOSE 80

# Start Apache in the foreground
CMD ["apache2-foreground"]