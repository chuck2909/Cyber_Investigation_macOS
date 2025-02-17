# 🔍 Real-World Cyber Investigation: macOS Network Threat Detection

🚀 By Carlos
📅 Date: 2/17/2025

🔴 Ever Wonder What’s Running on Your Mac?

Ever felt like your Mac is doing things behind your back? Maybe an app is sending data somewhere weird, or your network has unknown connections you don’t recognize.

This project is a complete cybersecurity investigation & automation script that lets any macOS user analyze their network traffic in a way that:

✅ Is beginner-friendly—no hacking skills needed, just follow simple steps.

✅ Uses real SOC techniques—the same ones companies use to detect threats.

✅ Runs an automated Python script—because nobody wants to do this manually every time.

🛠️ Quick Setup (For Any macOS User)

You don’t need to be a hacker, engineer, or SOC analyst—just follow these simple steps:

1️⃣ Install Python & Required Modules

Open Terminal and run:

python3 -m pip install requests

2️⃣ Clone This GitHub Repo

git clone https://github.com/chuck2909/Cyber_Investigation_macOS.git

cd macOS-Network-Investigation

3️⃣ Run the Network Scan

python3 network_monitor.py

✅ This will scan your Mac’s network activity and log all external connections.

4️⃣ View the Results

After running, open the report:

cat network_analysis.log

✅ If you see Google, AWS, or Cloudflare, you’re fine.
🚨 If you see weird IPs from unknown places, dig deeper.

## 📊 Sample Output (What You’ll See)

🔍 Scanning active connections...

74.125.0.166 - United States - Google LLC
44.213.202.176 - United States - Amazon.com
142.251.35.174 - United States - Google LLC

✅ Analysis complete! Results saved to: network_analysis.log

✅ Safe connections? You’re good.
🚨 Weird foreign IPs? Time to investigate.


## 🔍 Advanced Mode: Analyze Your System Logs

If you want to go deeper, scan all logs on your Mac for external connections:

python3 log_analyzer.py

✅ This will check all saved logs for hidden network activity.
✅ Great for spotting past suspicious connections.


## 🛡️ Why This Matters (For Cybersecurity & Privacy)
	•	Most Mac users have no clue what’s happening on their network.
	•	Companies take cybersecurity seriously—so should you.
	•	Automating threat detection makes network monitoring easy & repeatable.

📌 If you’re applying for SOC Analyst, Blue Team, or Cybersecurity roles, this project is a great portfolio piece!

📢 Contributing & Next Steps

✅ Future Features:
	•	Automate alerts for suspicious IPs.
	•	Integrate with VirusTotal for real-time threat checks.
	•	Turn this into a simple macOS app (no Terminal needed).

✅ Want to help? Fork this repo & contribute!

## 😂 Bonus: Cybersecurity Humor

“sudo chmod -R 777 /” – because who needs security, right?”
(Don’t actually run this. Unless you want a bad day.)


## 🔥 Final Thoughts

This project started as a personal curiosity but became a full cybersecurity analysis & automation tool. Whether you’re:
✅ A Mac user who just wants to know what’s going on with your network
✅ A cybersecurity student looking for real-world investigation experience
✅ A SOC analyst who needs a quick network visibility tool

This script has something for you. 🚀
