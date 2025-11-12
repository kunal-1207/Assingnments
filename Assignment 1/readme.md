# Linux Command Tasks Submission

**Project Title:** Linux Command Line Exercises  
**Your Name:** ________________________  
**Date:** ________________________  

---

## 1. Creating and Renaming Files/Directories

**Commands:**
```bash
mkdir test_dir
cd test_dir
touch example.txt
mv example.txt renamed_example.txt
````

**Screenshot:**
![Step 1 Screenshot](path/to/screenshot1.png)

**Explanation:**

* Created a directory named `test_dir`.
* Inside it, an empty file `example.txt` was created.
* Renamed `example.txt` to `renamed_example.txt` using `mv`.
* Demonstrates basic file and directory management in Linux.

---

## 2. Viewing File Contents

**Commands:**

```bash
cat /etc/passwd
head -n 5 /etc/passwd
tail -n 5 /etc/passwd
```

**Screenshot:**
![Step 2 Screenshot](path/to/screenshot2.png)

**Explanation:**

* `cat` displays the full contents of `/etc/passwd`.
* `head -n 5` shows the first 5 lines.
* `tail -n 5` shows the last 5 lines.
* Useful for quickly viewing parts of large files.

---

## 3. Searching for Patterns

**Command:**

```bash
grep "root" /etc/passwd
```

**Screenshot:**
![Step 3 Screenshot](path/to/screenshot3.png)

**Explanation:**

* `grep` searches for the word "root" in `/etc/passwd`.
* Displays all lines containing "root".
* Helps quickly locate specific entries in files.

---

## 4. Zipping and Unzipping

**Commands:**

```bash
zip -r test_dir.zip test_dir
unzip test_dir.zip -d unzipped_dir
```

**Screenshot:**
![Step 4 Screenshot](path/to/screenshot4.png)

**Explanation:**

* `zip -r` compresses the directory `test_dir` into `test_dir.zip`.
* `unzip` extracts it into a new directory `unzipped_dir`.
* Demonstrates file compression and extraction in Linux.

---

## 5. Downloading Files

**Command:**

```bash
wget https://example.com/sample.txt
```

**Screenshot:**
![Step 5 Screenshot](path/to/screenshot5.png)

**Explanation:**

* `wget` downloads a file from a specified URL.
* Useful for fetching files directly from the internet in the terminal.

---

## 6. Changing Permissions

**Commands:**

```bash
touch secure.txt
chmod 444 secure.txt
ls -l secure.txt
```

**Screenshot:**
![Step 6 Screenshot](path/to/screenshot6.png)

**Explanation:**

* Created `secure.txt`.
* `chmod 444` sets read-only permissions for everyone.
* Demonstrates file permission management in Linux.

---

## 7. Working with Environment Variables

**Commands:**

```bash
export MY_VAR="Hello, Linux!"
echo $MY_VAR
```

**Screenshot:**
![Step 7 Screenshot](path/to/screenshot7.png)

**Explanation:**

* `export` creates a new environment variable `MY_VAR`.
* `echo $MY_VAR` confirms the value is set.
* Useful for storing temporary session variables.

---

## GitHub Repository Link

[Insert GitHub repo link here](https://github.com/kunal-1207/Assingnments/tree/main/Assignment%201)

---



If you want, I can **also generate a ready-to-upload GitHub repository folder structure with this README.md and placeholders for screenshots**, so you can just drop your images and push.  

Do you want me to do that?
```
