#!/usr/bin/bash
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo service nginx restart
