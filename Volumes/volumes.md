# Hands-on EC2-04 (Version 2.0.0): Extending and Partitioning EBS Volumes

## 🎯 Purpose

The purpose of this hands-on training is to teach students how to add, attach, extend, and partition Elastic Block Store (EBS) volumes on running Amazon Linux 2023 EC2 instances. Students will also learn how to automatically mount EBS volumes after instance reboots.

---

## 🧠 Learning Outcomes

At the end of this hands-on training, students will be able to:

- Understand the difference between root and additional volumes.
- List and verify the status of primary (root) and secondary (additional) volumes.
- Create and attach new EBS volumes from the AWS Management Console.
- Create and mount file systems on EBS volumes.
- Extend partitions and resize file systems to utilize added capacity.
- Configure automatic mounting (auto-mount) of EBS volumes on reboot.

---

## 🗂 Outline

1. Extend the Root Volume
2. Create, Attach, Mount, and Extend an Additional EBS Volume
3. Auto-Mount EBS Volumes and Partitions on Reboot

---

## 🧩 Part 1 - Extend the Root Volume

1. **Launch an EC2 instance** in the `us-east-1a` Availability Zone.

2. **Check which volumes are attached** to the instance. Only the root volume should appear.

   ```bash
   lsblk
   df -h
   ```

3. **Check the file system** of the root volume’s partition.

   ```bash
   sudo file -s /dev/nvme0n1
   ```

4. **Increase the root volume size** from 8 GB to 12 GB in the AWS Console:

   - Go to **Volumes** → select the instance’s root volume → **Modify Volume**.

5. **List block devices and file system usage** again:

   ```bash
   lsblk
   df -h
   ```

   The volume size should reflect the change, but the partition and file system will still show the old size.

6. **Extend the partition** to occupy all newly available space.

   ```bash
   sudo growpart /dev/nvme0n1 1
   ```

7. **Resize the XFS file system** to use all available space on the extended partition.

   ```bash
   sudo xfs_growfs /dev/nvme0n1p1
   ```

8. **Verify the changes** by listing block devices and disk usage again:
   ```bash
   lsblk
   df -h
   ```
   The partition and file system should now reflect the increased size.

---

## 🧩 Part 2 - Create, Attach, Mount, and Extend an Additional EBS Volume

### Section 1 - Create and Attach a New Volume

1. **Create a new EBS volume** in the same Availability Zone (`us-east-1a`) with a size of 2 GB.  
   ⚠️ Make sure the instance and the new volume are in the **same AZ**.

2. **Attach the new volume** from the AWS Console:

   - Select the instance you created earlier.
   - Set **Device name:** `/dev/sdf` _(it will appear as `/dev/nvme1n1` inside the instance)_.

3. **List block devices** and verify that both root and secondary volumes are visible:
   ```bash
   lsblk
   df -h
   ```

---

### Section 2 - Mount the New Volume

1. **Check the format of the root volume** (for reference):

   ```bash
   sudo file -s /dev/nvme0n1
   ```

2. **Check the new volume** to see if it is already formatted or contains data:

   ```bash
   sudo file -s /dev/nvme1n1
   ```

3. If not formatted, **create a new file system** on the new volume:

   ```bash
   sudo mkfs -t ext4 /dev/nvme1n1
   ```

4. **Verify** the volume format again:

   ```bash
   sudo file -s /dev/nvme1n1
   ```

5. **Create a mount point directory** for the new volume:

   ```bash
   sudo mkdir /mnt/2nd-vol
   ```

6. **Mount the volume** to the mount point:

   ```bash
   sudo mount /dev/nvme1n1 /mnt/2nd-vol/
   ```

7. **Confirm** that the volume is successfully mounted:

   ```bash
   lsblk
   ```

8. **Check available space** on the mount point:

   ```bash
   df -h
   ```

9. **Verify data presence:**
   ```bash
   ls /mnt/2nd-vol/
   ```
   If it is empty, create a sample file to verify persistence later:
   ```bash
   cd /mnt/2nd-vol
   sudo touch hello.txt
   ls
   ```

---

### Section 3 - Enlarge and Resize the New Volume

1. **Modify the volume** in the AWS Console, increasing its size from 2 GB → 4 GB.

2. **Check block devices** again to confirm the size change:

   ```bash
   lsblk
   ```

3. **Verify file system space** (still shows old size):

   ```bash
   df -h
   ```

4. **Resize the file system** to utilize the new capacity:

   ```bash
   sudo resize2fs /dev/nvme1n1
   ```

5. **Check available space** again to confirm the new capacity:

   ```bash
   df -h
   ```

6. **Verify data persistence:**
   ```bash
   ls /mnt/2nd-vol/
   ```

---

## 🧩 Part 3 - Auto-Mount EBS Volumes and Partitions on Reboot

1. **Reboot the instance** to demonstrate that the mount point disappears after restart:

   ```bash
   sudo reboot now
   ```

2. **After reboot**, confirm the new volume is still attached but not mounted:

   ```bash
   lsblk
   ```

3. **Back up the fstab configuration file:**

   ```bash
   sudo cp /etc/fstab /etc/fstab.bak
   ```

4. **Open the fstab file for editing:**

   ```bash
   sudo nano /etc/fstab
   ```

5. **Add the following entry** (UUIDs can also be used instead of device paths):

   ```bash
   /dev/nvme1n1   /mnt/2nd-vol   ext4   defaults,nofail   0   0
   ```

6. Save and exit (`CTRL + X`, then `Y`, then `Enter`).

7. **Reboot** the instance again to confirm persistence:

   ```bash
   sudo reboot now
   ```

8. **Verify** all volumes and partitions are listed and mounted:

   ```bash
   lsblk
   df -h
   ```

9. **Check if the data still persists:**
   ```bash
   ls /mnt/2nd-vol/
   ```

---

## ✅ Summary

In this lab, you learned how to:

- Extend the root EBS volume of an EC2 instance.
- Create, attach, and mount a secondary EBS volume.
- Extend and resize partitions to utilize added capacity.
- Configure automatic mounting using `/etc/fstab` to preserve persistence after reboot.

This hands-on exercise builds essential skills for managing **EBS storage** efficiently on AWS EC2 instances.
