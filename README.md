# AI Packet Analyzer

AI-powered web application to analyze PCAP files and detect network issues with root cause analysis (RCA).

---

## 🚀 Overview

AI Packet Analyzer is a Flask-based web tool that allows users to upload packet capture (PCAP) files and receive intelligent analysis of network behavior.

It combines:

* Packet parsing using PyShark (tshark)
* Structured traffic summarization
* AI-driven troubleshooting and root cause analysis

This project is designed for:

* Network engineers
* SOC analysts
* DevOps / SRE teams
* Anyone troubleshooting network issues

---

## 🔍 Features

* 📂 Upload PCAP files via web interface
* 🧠 AI-based packet analysis
* 📊 Structured output including:

  * Executive summary
  * Detected anomalies
  * Protocol-level analysis (TCP, DNS, etc.)
  * Root cause hypothesis
  * Recommended actions
* ⚡ Lightweight Flask backend
* 🔧 Easy to extend for advanced network analytics

---

## 🛠 Tech Stack

* **Python 3.x**
* **Flask** (Web framework)
* **PyShark** (Packet parsing)
* **tshark** (Wireshark CLI engine)
* **OpenAI API** (AI analysis)

---

## 📂 Project Structure

```
ai-packet-analyzer/
│
├── app.py                # Flask web server
├── analyzer.py           # Packet analysis + AI logic
├── requirements.txt      # Dependencies
├── README.md             # Documentation
│
├── templates/
│   └── index.html        # Web UI
│
├── uploads/              # Uploaded PCAP files (ignored in git)
│
└── .gitignore
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-packet-analyzer.git
cd ai-packet-analyzer
```

---

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Install tshark (Required)

```bash
sudo apt update
sudo apt install tshark
```

Verify installation:

```bash
tshark -v
```

---

### 5. Set OpenAI API Key

```bash
export OPENAI_API_KEY="your_api_key_here"
```

(Optional: add to `~/.bashrc` for persistence)

---

### 6. Run the Application

```bash
python3 app.py
```

---

### 7. Access the Web Interface

Open your browser:

```
http://127.0.0.1:5000
```

---

## 🧪 Usage

1. Open the web interface
2. Upload a `.pcap` file
3. Click **Analyze**
4. View structured AI-generated report

Output includes:

* Network anomalies
* Protocol insights
* Root cause analysis
* Recommended fixes

---

## 🧠 How It Works

1. **PCAP Upload**

   * User uploads file via Flask UI

2. **Packet Parsing**

   * PyShark processes packets using tshark

3. **Data Summarization**

   * Extracts key fields:

     * Source / Destination IP
     * Protocol
     * Packet info

4. **AI Analysis**

   * Structured prompt sent to OpenAI model
   * Model returns network diagnosis

5. **Result Display**

   * Rendered in browser

---

## ⚠️ Limitations

* Large PCAP files (>10MB) may impact performance
* Analysis is based on sampled packets (not full capture)
* AI output is inference-based (not deterministic)

---

## 🔐 Security Considerations

* `.gitignore` excludes:

  * PCAP files
  * Upload directory
  * Virtual environment
* Never commit API keys
* Validate uploaded files in production

---

## 🔮 Future Enhancements

* Flow-based traffic analysis
* TCP retransmission detection (deterministic)
* DNS anomaly detection
* BGP route analysis (advanced feature)
* Real-time packet stream analysis
* Dashboard with charts & metrics
* User authentication & multi-session support

---

## 📈 Potential Use Cases

* Network troubleshooting automation
* SOC analysis assistant
* Packet inspection learning tool
* Enterprise network diagnostics

---

## 👨‍💻 Author

**Subrat**
Senior Network Consultant

---

## 📄 License

This project is intended for educational and research purposes.
