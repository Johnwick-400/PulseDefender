
# PulseDefender

## 📖 Overview

This project focuses on the detection and mitigation of **Distributed Denial-of-Service (DDoS) attacks**, specifically distinguishing between **High-Rate** and **Low-Rate** attacks. DDoS attacks aim to disrupt the availability of network services by overwhelming them with malicious traffic. While high-rate attacks are easier to detect due to their intensity, low-rate attacks are more subtle and difficult to identify.

Our system leverages **machine learning techniques** to accurately classify network traffic as normal, high-rate DDoS, or low-rate DDoS, ensuring proactive defense and network reliability.

---

## 🎯 Objectives

- Analyze and understand the behavior of DDoS attacks.
- Categorize attacks based on their rate (High-Rate vs. Low-Rate).
- Preprocess and prepare a dataset for effective classification.
- Train machine learning models to detect and classify DDoS attacks.
- Evaluate model performance and optimize detection accuracy.
- Suggest mitigation techniques based on classification results.

---

## 📁 Dataset

We used a **publicly available dataset** containing network traffic logs with labeled DDoS attack types. The dataset includes:

- **Normal Traffic**
- **High-Rate DDoS Attacks** (e.g., UDP flood, ICMP flood)
- **Low-Rate DDoS Attacks** (e.g., Slowloris, Low-Rate HTTP flood)

Each record contains features such as:
- Source IP, Destination IP
- Protocol (TCP/UDP/ICMP)
- Packet Size
- Time Interval
- Number of Packets
- Flags and Status Codes

---

## 🛠️ Technologies Used

- 🐍 Python
- 📊 Pandas, NumPy
- 📈 Scikit-learn
- 🔍 Matplotlib, Seaborn
- 🧠 Machine Learning (Random Forest, SVM, Logistic Regression)
- 💾 Jupyter Notebook / Google Colab

---

## ⚙️ Implementation Steps

1. **Data Collection & Preprocessing**
   - Loaded the dataset, handled missing values
   - Label encoded categorical features
   - Performed feature scaling and data normalization

2. **Exploratory Data Analysis (EDA)**
   - Visualized the distribution of attack types
   - Analyzed traffic patterns over time

3. **Feature Selection**
   - Selected important features using correlation and feature importance scores

4. **Model Training**
   - Trained multiple classifiers (Random Forest, SVM, Logistic Regression)
   - Used cross-validation for robustness

5. **Model Evaluation**
   - Measured accuracy, precision, recall, F1-score
   - Plotted confusion matrix and ROC-AUC curves

6. **Attack Detection & Classification**
   - Classified incoming traffic as Normal, High-Rate DDoS, or Low-Rate DDoS

7. **Mitigation Strategy**
   - Suggested dynamic rate-limiting and traffic filtering techniques for each class of attack

---

## 🔍 Results

| Model             | Accuracy | Precision | Recall | F1-Score |
|------------------|----------|-----------|--------|----------|
| XGboost Classifier | 97.8%    | 98.2%     | 97.5%  | 97.8%    |
| SVM               | 95.6%    | 96.1%     | 95.2%  | 95.6%    |
| Random Forest  | 93.4% | 94.0%     | 93.1%  | 93.5%    |

- Random Forest outperformed other models in both high-rate and low-rate attack detection.
- Confusion matrix confirmed minimal false negatives (critical in real-world detection).

---

## 🚧 Limitations

- Real-time detection not implemented (but can be extended using streaming libraries).
- Dataset may not represent emerging or zero-day attack patterns.
- Assumes labeled data availability for training.

---

## 💡 Future Enhancements

- Integrate with real-time traffic monitoring tools (e.g., Wireshark, Zeek).
- Build a dashboard for live visualization and alerting.
- Extend the model to support anomaly detection for unknown attack types.
- Use deep learning (e.g., LSTM, CNN) for better temporal pattern recognition.

---

## 🙌 Authors

- **Veesam Parasuram Pavan Teja**  
  Final Year B.Tech Student  
  Lendi Institute Of Engineering and Technology

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 📬 Contact

For queries or collaboration, reach out to me at:  
📧 pavantejveesam26@gmail.com  
🔗 [https://www.linkedin.com/in/pavantejveesam/]
