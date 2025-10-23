# Hands-on EC2-05 (Version 2.0.0): Working with EC2 Snapshots and AMIs

## 🎯 Purpose
The purpose of this hands-on training is to teach students how to:
- Take snapshots of EC2 instances.
- Create Amazon Machine Images (AMIs) from EC2 instances.
- Understand the difference between snapshots and AMIs.
- Use the AWS Data Lifecycle Manager (DLM) for snapshot automation.
- Copy and share AMIs.

---

## 🧠 Learning Outcomes
At the end of this hands-on training, students will be able to:
- Take snapshots of EC2 instances from the AWS Management Console.
- Create AMIs from running instances.
- Understand how snapshots and AMIs differ in purpose and structure.
- Automate snapshot creation with the Data Lifecycle Manager.
- Copy and share AMIs across regions or accounts.

---

## 🗂 Outline
1. Creating an Image from the Snapshot of the Nginx Server and Launching a New Instance  
2. Creating an Image Using the Action Menu  
3. Using the Data Lifecycle Manager  
4. Making an AMI Public  

---

## 🧩 Part 1 - Creating an Image from the Snapshot of the Nginx Server and Launching a New Instance

1. **Launch an EC2 Instance** with the following configuration:
   - **Security Group:** Allow **SSH (22)** and **HTTP (80)** from anywhere.  
     *(Name: “SSH and HTTP”)*
   - **User Data:** (Paste the following script)
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

   - **Tag:** Since the Data Lifecycle Manager works based on tags, apply the following tag:
     ```
     Key: Name
     Value: SnapshotInstance
     ```

2. After the instance is running, **copy its Instance ID.**

3. From the EC2 Dashboard, go to **Snapshots → Create Snapshot.**
   - **Resource type:** Instance  
   - **Instance ID:** Select the Nginx instance  
   - **Name:** FirstSnapshotNginx  
   - Click **Create Snapshot.**

4. After the snapshot is created, open the **Actions** menu → **Create Image.**
   - **Name:** FirstAMINginx  
   - **Description:** FirstAMINginx  

5. Go to the **AMIs** section and verify that `FirstAMINginx` appears.

6. Click **Launch Instance**, select **My AMIs**, and choose **FirstAMINginx**.

7. Launch a new instance named **InstanceFromSnapshotAMI**.

8. Copy the public IP of the new instance and open it in your browser.  
   ✅ Confirm that the **Nginx Web Server** is working properly.

---

## 🧩 Part 2 - Creating an Image Using the “Action” Menu

1. Go back to the **SnapshotInstance** EC2 instance.  
2. From the **Actions** menu, select **Image → Create Image.**
   ```
   Name: SecondAMINginx
   Description: SecondAMINginx
   ```
3. Go to the **AMIs** section and confirm that `SecondAMINginx` appears.

4. After the AMI creation completes, open the **Snapshots** section again.  
   ✅ Notice that AWS automatically created a **new snapshot** for `SecondAMINginx`.

🧠 **Explanation:**  
Even if you do not manually create a snapshot, AWS automatically generates one when creating an image.  
Be careful — if you forget to delete these automatically generated snapshots, **AWS may charge you** for the additional storage.

---

## 🧩 Part 3 - Using the Data Lifecycle Manager (DLM)

1. From the EC2 Console, navigate to:  
   **Elastic Block Store → Lifecycle Manager → Create snapshot lifecycle policy**

2. **Policy Type:**  
   ```
   EBS snapshot policy
   ```

3. **Resource Type:**  
   ```
   Instance
   ```

4. **Description:**  
   ```
   Test policy
   ```

5. **Tags:** Select the tag applied to your instance earlier.
   ```
   Key: Name
   Value: SnapshotInstance
   ```

6. **IAM Role:**  
   Choose **Default role** (or create a new role with appropriate snapshot permissions).

7. **Schedule Configuration:**
   ```
   Schedule name : My_schedule
   Frequency     : Daily
   Every         : 24 Hours
   Starting at   : 03:00 UTC
   Retention Type: Count
   Retain        : 5
   ```

8. Enable **Copy tags from source** so that snapshots inherit the same tags.

9. **Cross-Region Copy:**  
   Uncheck “Enable cross-region copy”

10. **Cross-Account Sharing:**  
    Check “Enable cross-account sharing”

11. Review the **Policy Summary** carefully, then click **Enable Policy.**

12. Finally, click **Create Policy.**

✅ The DLM policy is now created and active.  
You can check it in the console under **Lifecycle Manager**.  
After verifying, **delete the policy** to avoid unnecessary scheduled snapshots.

---

## 🧩 Part 4 - Making an AMI Public

⚠️ **Instructor Note:** Tell students **not to perform this step simultaneously.**

1. Go to the **AMIs** section.  
2. Select **FirstAMINginx.**  
3. Click **Permissions → Make Public.**  
4. Wait a few minutes for the AMI to become public.  
5. Share the **AMI ID** (e.g., via Slack).  
6. Students can search for this AMI ID under **Community AMIs** in the AMI search bar.  
7. After testing, delete all **AMIs and Snapshots** to avoid additional costs.

---

## ✅ Summary

In this lab, you learned how to:
- Create snapshots and AMIs from running instances.
- Launch new instances from those images.
- Automate snapshot creation using the AWS Data Lifecycle Manager.
- Make AMIs publicly available for others.

You now understand how **AMI and Snapshot** work together and how they differ in purpose and use.
