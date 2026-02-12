# flask-aws-ndb
Connecting the flask to aws ec2 without database


#Process of connecting to aws ec2 
step 1 ---> open aws console , create new instance with public access and launch the instances
step2 ----> Commands ----> 1. sudo apt-get update
                           2. sudo apt install python3 python3-pip nginx git -y
                           3. create a directory using cmd --> mkdir flask-app , next cd flask-app , next  git clone git repo 
                           4. Install venv --> sudo get python3-venv , then create venv  python -m venv venv , source venv/bin/activate 
                           5. then install dep --> pip install -r requirements.txt , run the python app.py , check the gunicorn -w 3 -b 0.0.0.0:5000 app:app --                                    locally runs
                           6. Create a Nginx conf file --> sudo nano etc/conf.d/flask-app.conf 
                              Here it is looks like    server{
                                                          listen 80;
                                                          server_name public IP address;
                                                          location / {
                                                    proxy_pass http://127.0.0.1:5000;
                                                    proxy_set_header Host $host;
                                                    proxy_set_header X-Real-IP $remote_addr;
                               proxy_set_header X-Forwarded- For$proxy_add_x_forwarded_for;  }}
                              7.Then start the nginx --> sudo systemctl start nginx , sudo systemctl enable nginx , sudo systemctl status nginx
                              8.Create new dir --> sudo mkdir etc/systemd/flask-app.service 
                                  [Unit]
                                  Description=Flask app
                                  After=network.target 
                                  [Service]
                                  User=ubuntu
                                  WorkingDirectory= /home/ubuntu/flask-app/flask-aws-ndb
                                  ExecStart=/home/ubuntu/flask-app/flask-aws-ndb/venv/bin/gunicorn -w 3 -b 0.0.0.0:5000 aws:app
                                  Restart=always
                                  [Install]
                                  WantedBy=multi-user.target
                                9. check the service --> sudo systemctl daemon-restart , sudo systemctl restart flask-app.service,sudo systemctl status flask-app.service
                                10. Check the both the nginx and service files status if its running , goes to new tab paste the public-ip , then u can see ur flask app
