# Hands-on EC2-02 (Version 2.0.0): How to Install Nginx Web Server on Amazon Linux 2023

## 🎯 Purpose
The purpose of this hands-on training is to provide students with basic knowledge of how to install and configure the Nginx Web Server on an Amazon Linux 2023 EC2 instance.

---

## 🧠 Learning Outcomes
At the end of this hands-on training, students will be able to:
- Launch an AWS EC2 instance using the Amazon Linux 2023 AMI.
- Connect to an EC2 instance using SSH.
- Install and start the Nginx Web Server.
- Configure Nginx to serve a simple HTML page.
- Create a basic Bash script to automate Nginx setup.
- Use EC2 user data to automatically install and configure a web server on launch.

---

## 🗂 Outline
1. Launching an EC2 Instance and Connecting via SSH  
2. Installing and Configuring the Nginx Web Server  
3. Automating Web Server Installation Using a User Data Script

---

## 🧩 Part 1 - Launching an EC2 Instance and Connecting via SSH

1. **Launch an EC2 instance** using the following configuration:  
   - **AMI:** Amazon Linux 2023  
   - **Instance Type:** t3.micro  
   - **Security Group:** Allow inbound connections from anywhere on ports 22 (SSH) and 80 (HTTP).

2. **Connect to the instance** using SSH from your local terminal:
   ```bash
   ssh -i [your-key.pem] ec2-user@[your-ec2-public-ip]
   ```

---

## 🧩 Part 2 - Installing and Configuring Nginx Web Server

1. **Update installed packages** on your EC2 instance.
   ```bash
   sudo dnf update -y
   ```

2. **Install the Nginx Web Server.**
   ```bash
   sudo dnf install nginx -y
   ```

3. **Start the Nginx service.**
   ```bash
   sudo systemctl start nginx
   ```

4. **Check from your browser** by visiting your EC2 instance’s **public IP or DNS name.**  
   Example: `http://ec2-xx-xx-xx-xx.compute-1.amazonaws.com`

5. **Navigate to the Nginx root directory.**
   ```bash
   cd /usr/share/nginx/html
   ```

6. **List the directory contents and update folder permissions.**
   ```bash
   ls -la
   sudo chmod -R 777 /usr/share/nginx/html
   ```

7. **Remove the existing `index.html`.**
   ```bash
   sudo rm index.html
   ```

8. **Download new web files (`index.html` and `ken.jpg`)** using `wget` from GitHub.  
   Repository: [https://github.com/awsdevopsteam/route-53](https://github.com/awsdevopsteam/route-53)
   ```bash
   wget https://raw.githubusercontent.com/awsdevopsteam/route-53/master/index.html
   wget https://raw.githubusercontent.com/awsdevopsteam/route-53/master/ken.jpg
   ```

9. **Restart the Nginx service** to apply the new files.
   ```bash
   sudo systemctl restart nginx
   ```

10. **Enable Nginx to start automatically on boot.**
    ```bash
    sudo systemctl enable nginx
    ```

11. **Check from your browser** to verify that the web server is working properly.

12. **(Optional)**: If you want to add new content, ensure proper folder permissions:
    ```bash
    sudo chmod -R 777 /usr/share/nginx/html
    ```

> ⚠️ **Note:** Running `chmod -R 777 /` (root directory) is extremely dangerous. It gives full read/write/execute permissions to all users on the system.

13. **Create an additional HTML page.**
    ```bash
    echo "Second Page" | sudo tee /usr/share/nginx/html/index_2.html
    ```

14. **Access the new page** by adding `/index_2.html` to your instance’s public DNS.  
    Example:  
    `http://ec2-54-144-132-10.compute-1.amazonaws.com/index_2.html`

---

## 🧩 Part 3 - Automating Web Server Installation Using User Data

15. **Launch a new EC2 instance** with the same configuration as before:  
    - **AMI:** Amazon Linux 2023  
    - **Instance Type:** t3.micro  
    - **Security Group:** Allow SSH (22) and HTTP (80).

16. **Add the following user data script** during instance launch to automate installation and configuration:
    ```bash
    #! /bin/bash
    dnf update -y
    dnf install nginx -y
    systemctl start nginx
    cd /usr/share/nginx/html
    chmod -R 777 /usr/share/nginx/html
    rm index.html
    wget https://raw.githubusercontent.com/awsdevopsteam/route-53/master/index.html
    wget https://raw.githubusercontent.com/awsdevopsteam/route-53/master/ken.jpg
    systemctl restart nginx
    systemctl enable nginx
    ```

17. **Review and launch the instance.**  
    Once it’s running, check from your web browser if the **Nginx Web Server** works automatically.

18. **Verify Nginx is serving the page** using the `curl` command from your terminal.
    ```bash
    curl http://<your-public-dns>
    ```

---

## ✅ Summary
In this hands-on exercise, you learned how to:
- Launch and connect to an Amazon Linux 2023 EC2 instance.  
- Install and configure the Nginx Web Server.  
- Serve static HTML content via Nginx.  
- Automate Nginx setup using a **user data** Bash script.

This provides a foundational understanding of deploying and automating **web servers** on AWS EC2.
