# flask-aws-ndb

Connecting Flask to AWS EC2 without a database

## Process of Connecting to AWS EC2

### Step 1: Create AWS Instance
Open AWS console, create a new instance with public access and launch the instance.

### Step 2: Setup Environment

1. Update system packages:
   ```bash
   sudo apt-get update
   ```

2. Install required packages:
   ```bash
   sudo apt install python3 python3-pip nginx git -y
   ```

3. Create a directory and clone the repository:
   ```bash
   mkdir flask-app
   cd flask-app
   git clone <your-git-repo>
   cd flask-aws-ndb
   ```

4. Install and setup virtual environment:
   ```bash
   sudo apt-get install python3-venv
   python3 -m venv venv
   source venv/bin/activate
   ```

5. Install dependencies and test the application:
   ```bash
   pip install -r requirements.txt
   python aws.py
   # Test with gunicorn
   gunicorn -w 3 -b 0.0.0.0:5000 aws:app
   ```

### Step 3: Configure Nginx

6. Create Nginx configuration file:
   ```bash
   sudo nano /etc/nginx/conf.d/flask-app.conf
   ```

   Add the following configuration:
   ```nginx
   server {
       listen 80;
       server_name <your-public-ip>;
       
       location / {
           proxy_pass http://127.0.0.1:5000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
       }
   }
   ```

7. Start and enable Nginx:
   ```bash
   sudo systemctl start nginx
   sudo systemctl enable nginx
   sudo systemctl status nginx
   ```

### Step 4: Setup Systemd Service

8. Create systemd service file:
   ```bash
   sudo nano /etc/systemd/system/flask-app.service
   ```

   Add the following configuration:
   ```ini
   [Unit]
   Description=Flask app
   After=network.target
   
   [Service]
   User=ubuntu
   WorkingDirectory=/home/ubuntu/flask-app/flask-aws-ndb
   ExecStart=/home/ubuntu/flask-app/flask-aws-ndb/venv/bin/gunicorn -w 3 -b 0.0.0.0:5000 aws:app
   Restart=always
   
   [Install]
   WantedBy=multi-user.target
   ```

9. Start and enable the service:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl start flask-app.service
   sudo systemctl enable flask-app.service
   sudo systemctl status flask-app.service
   ```

### Step 5: Verify Deployment

10. Check that both Nginx and the service are running. Open a web browser and navigate to your instance's public IP address to see your Flask app.
