# How to Launch Your Website (Cybro Marketing)

## Option 1: The Easiest Way (Netlify) - Takes 2 Minutes
1.  **Extract the Zip File** you just downloaded (`CybroMarketing_Website.zip`).
2.  Go to [Netlify Drop](https://app.netlify.com/drop).
3.  **Drag and drop** the extracted folder onto the page.
    *   Netlify will create a live URL instantly (e.g., `cybro-marketing-123.netlify.app`).
4.  **Connect Your Domain**:
    *   Click "Set up domain" in Netlify.
    *   Enter your domain (e.g., `cybromarketing.com`).
    *   Netlify will give you DNS instructions (usually adding a CNAME record where you bought your domain).

## Option 2: cPanel / Traditional Hosting (GoDaddy, Bluehost, Namecheap)
1.  **Log in to your Hosting cPanel**.
2.  Open **File Manager**.
3.  Go to the **public_html** folder.
4.  **Upload** the `CybroMarketing_Website.zip` file.
5.  Right-click the zip file and choose **Extract**.
6.  Ensure `index.html` is directly inside `public_html`, not in a subfolder.
    *   If it's in a subfolder, select all files and move them up to `public_html`.

## Option 3: GitHub Pages (For Tech-Savvy Users)
1.  Create a new repository on GitHub.
2.  Upload these files.
3.  Go to **Settings > Pages**.
4.  Set Source to **Main** branch.
5.  Save. Your site will be live at `username.github.io/repo-name`.

---
**Need Help?**
If you have a domain already purchased, let me know the provider (e.g., GoDaddy, Namecheap), and I can give specific instructions for that provider!

Update trigger for Vercel
