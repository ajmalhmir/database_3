# Customer Management API

A Django REST API for managing customer information including name, phone, and balance. This application is configured for deployment on AWS EC2.

## Features

- Create, Read, Update, and Delete (CRUD) operations for customer data
- RESTful API endpoints
- Django REST Framework for API development
- Configured for AWS EC2 deployment with Nginx and Gunicorn

## API Endpoints

- `GET /api/customers/` - List all customers
- `POST /api/customers/` - Create a new customer
- `GET /api/customers/{id}/` - Retrieve a specific customer
- `PUT /api/customers/{id}/` - Update a customer (full update)
- `PATCH /api/customers/{id}/` - Partial update a customer
- `DELETE /api/customers/{id}/` - Delete a customer

## Customer Model

- `name`: Customer's full name
- `phone`: Customer's phone number
- `balance`: Customer's account balance
- `created_at`: Timestamp when the customer was created
- `updated_at`: Timestamp when the customer was last updated

## Setup and Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start the development server: `python manage.py runserver`

## Testing the API

You can use the included `test_api.py` script to test the API functionality:

```bash
python test_api.py
```

This script demonstrates creating, retrieving, updating, and deleting customers through the API.

## Deploying to AWS EC2

### Prerequisites

- An AWS account
- An EC2 instance running Ubuntu
- Basic knowledge of AWS services

### Deployment Steps

1. Launch an EC2 instance with Ubuntu
2. Configure security groups to allow HTTP (port 80) and HTTPS (port 443) traffic
3. Connect to your EC2 instance via SSH
4. Copy the UserData.sh script content to the EC2 User Data section when launching the instance, or run it manually after connecting

```bash
# If running manually after connecting to EC2
sudo -i
curl -o userdata.sh https://raw.githubusercontent.com/ajmalhmir/database_3/main/UserData.sh
chmod +x userdata.sh
./userdata.sh
```

5. The script will automatically:
   - Clone the repository
   - Install system dependencies
   - Set up a Python virtual environment
   - Install Python dependencies
   - Configure Gunicorn and Nginx
   - Start the application

6. Access your application at your EC2 instance's public IP address

7. Access the admin panel at `http://your-ec2-ip/admin/` using the default credentials:
   - Username: `admin`
   - Password: `admin`

   **Note:** It is highly recommended to change these default credentials immediately after first login

### Production Database Configuration

For production deployment, it's recommended to use a more robust database like PostgreSQL instead of SQLite. The settings.py file includes a commented configuration for PostgreSQL that you can uncomment and configure with your database credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': 'myrdshost.rds.amazonaws.com',
        'PORT': '5432',
    }
}
```

You can use Amazon RDS for PostgreSQL as your database service.

### Environment Variables

The application is configured to use environment variables for sensitive settings in production. Set these environment variables on your EC2 instance:

```bash
# Set these in your EC2 environment
export DJANGO_SECRET_KEY='your-secure-secret-key'
export DJANGO_DEBUG='False'
```

You can add these to your ~/.bashrc file or set them in your systemd service file for persistence.

### Security Considerations

1. **HTTPS**: For production, configure HTTPS with Let's Encrypt or AWS Certificate Manager
2. **Firewall**: Configure security groups to only allow necessary traffic
3. **Database**: Use a separate database server with restricted access
4. **Secret Key**: Use a strong, unique secret key for production
5. **Debug**: Ensure DEBUG is set to False in production
6. **Static Files**: Configure proper static file serving with WhiteNoise (already included)
7. **Admin Access**: Restrict admin access to trusted IPs or VPN

### Scaling and Monitoring

1. **Load Balancing**: For high traffic, consider using an AWS Application Load Balancer with multiple EC2 instances
2. **Auto Scaling**: Configure Auto Scaling groups to handle traffic spikes
3. **Monitoring**: Use AWS CloudWatch to monitor your EC2 instance and set up alarms
4. **Logging**: Configure centralized logging with CloudWatch Logs
5. **Backups**: Regularly backup your database and critical files

### Troubleshooting

1. **Check Logs**: View Nginx logs at `/var/log/nginx/error.log` and Gunicorn logs with `sudo journalctl -u gunicorn`
2. **Service Status**: Check service status with `sudo systemctl status gunicorn` and `sudo systemctl status nginx`
3. **Permissions**: Ensure proper file permissions with `sudo chown -R ubuntu:www-data /home/ubuntu/database_3`
4. **Firewall**: Verify security group settings in AWS console
5. **Static Files**: If static files aren't loading, run `python manage.py collectstatic` again
6. **Database Issues**: If you encounter database errors like "no such table" when accessing the admin panel, it means migrations haven't been applied. SSH into your instance and run:
   ```bash
   cd /home/ubuntu/database_3
   source venv/bin/activate
   python manage.py migrate
   ```
   Note: The updated deployment script now includes automatic migrations

### Maintenance and Updates

1. **Code Updates**: To update your application:
   ```bash
   cd /home/ubuntu/database_3
   git pull
   source venv/bin/activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py collectstatic --noinput
   sudo systemctl restart gunicorn
   sudo systemctl restart nginx
   ```

2. **System Updates**: Regularly update your EC2 instance:
   ```bash
   sudo apt update
   sudo apt upgrade -y
   ```

3. **Backup Before Updates**: Always backup your database and critical files before updates

## Conclusion

This Customer Management API is now ready for deployment on AWS EC2. The project includes all necessary configuration files and scripts for a smooth deployment process. By following the instructions in this README, you can have your application up and running in production with proper security, scaling, and maintenance procedures in place.

For any issues or questions, please refer to the troubleshooting section or open an issue in the GitHub repository.