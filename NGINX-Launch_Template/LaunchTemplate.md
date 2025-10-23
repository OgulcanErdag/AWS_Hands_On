# Hands-on EC2-03 (Version 2.0.0): Creating an Instance with Launch Template and Versioning

## 🎯 Purpose

The purpose of this hands-on training is to teach students how to create, configure, and manage **Launch Templates** in the AWS EC2 Console — including adding user data scripts and versioning Launch Templates for incremental updates.

---

## 🧠 Learning Outcomes

At the end of this hands-on training, students will be able to:

- Create and configure Launch Templates on the AWS EC2 Console.
- Launch EC2 instances using Launch Templates.
- Modify Launch Templates and manage multiple template versions.
- Use `user data` to automate server configuration.

---

## 🗂 Outline

1. Creating a Launch Template
2. Modifying a Launch Template (Versioning)

---

## 🧩 Part 1 - Creating a Launch Template

### Step 1 - Create a Security Group

1. Create a new **Security Group** for use with your Launch Template.

   **Name:** Launch_Temp_Sec_Group  
   **Inbound Rules:**

   - SSH (22) → Anywhere (0.0.0.0/0)
   - HTTP (80) → Anywhere (0.0.0.0/0)

---

### Step 2 - Create a Launch Template

2. Open the **Amazon EC2 Console** at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).
3. In the navigation pane, under **Instances**, choose **Launch Templates**.
4. Click **Create launch template**.
5. Enter a name and description for your first version.

   ```textf
   Name: MyFirstTemplate
   Template version description: Origin
   ```

6. **Auto Scaling Guidance:** Keep default.
7. **Template Tags:** Keep default.
8. **Source Template:** Keep default.
9. **Amazon Machine Image (AMI):** Amazon Linux 2023 AMI (SSD Volume Type).
10. **Instance Type:** t3.micro
11. **Key Pair:** Select your existing PEM key (e.g., your.pem).
12. **Security Groups:** Select `Launch_Temp_Sec_Group`.
13. **Storage:** Keep default (8 GiB, gp3 SSD root volume).
14. **Resource Tags:**

```text
Key: Name
Value: Webserver-Origin
Resource Type: Instance
```

15. **Network Interfaces:** Keep default.
16. **Advanced Details:** Keep default.

---

### Step 3 - Launch an Instance from the Template

17. Go to **Launch Templates**.
18. Select `MyFirstTemplate` → **Actions** → **Launch instance from template**.
19. Set **Number of instances:** 1.
20. Keep all other settings as default, then click **Launch instance from template**.
21. Go to the **Instances** page and verify that the instance has been created successfully.

---

## 🧩 Part 2 - Modifying Launch Templates (Versioning)

### Step 1 - Create Launch Template Version 2

22. Go to **Launch Templates** in the EC2 console.
23. Select the template named `MyFirstTemplate` → **Actions** → **Modify template (Create new version)**.
24. Add the following version description:

```text
Version Description: V2 Nginx
```

25. **Key Pair:** Select your PEM key.
26. **Resource Tags:**

```text
Key: Name
Value: Webserver-V2
Resource Type: Instance
```

27. Scroll down to **Advanced Details** and add the following script under **User data**:

```bash
#!/bin/bash
dnf update -y
dnf install nginx -y
systemctl enable nginx
systemctl start nginx
```

28. Click **Create template version**.
29. Go to **Launch Templates** and open `MyFirstTemplate`.
30. Under the **Versions** tab, select **Version 2**.

```text
Version: 2
Description: V2 Nginx
```

31. Click **Actions** → **Launch instance from template**.
32. Set **Number of instances:** 1 and click **Launch instance from template**.
33. Go to the **Instances** page and verify the new EC2 instance.
34. Copy the instance’s **Public IP** and open it in a browser to verify that the **Nginx Web Server** is running.

---

### Step 2 - Create Launch Template Version 3

35. In the EC2 console, open **Launch Templates**.
36. Select `MyFirstTemplate` → **Actions** → **Modify template (Create new version)**.
37. Add the following version description:

```text
Version Description: V3 Nginx
```

38. **Key Pair:** Select your PEM key.
39. **Resource Tags:**

```text
Key: Name
Value: Webserver-V3
Resource Type: Instance
```

40. Scroll down to **Advanced Details** and add this **User Data** script:

```bash
#!/bin/bash
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

41. Click **Create template version**.
42. Return to **Launch Templates** and select your template.
43. Under **Versions**, choose **Version 3**.

```text
Version: 3
Description: V3 Nginx
```

44. Click **Actions** → **Launch instance from template**.
45. Set **Number of instances:** 1 and launch the instance.
46. Go to the **Instances** page and verify the new EC2 instance.
47. Copy the **Public IP**, open it in a browser, and confirm that the **Nginx web page with the custom image** loads successfully.

---

## ✅ Summary

In this lab, you learned how to:

- Create a Launch Template on the AWS EC2 Console.
- Launch EC2 instances using the template.
- Create multiple versions of the same template with different user data configurations.
- Automate Nginx setup directly from Launch Template versions.

Each version of a Launch Template allows you to evolve your server setup while maintaining previous configurations — a key concept for **scalable and consistent infrastructure automation** on AWS.
