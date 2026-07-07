# 🛡️ SentryCart AI Cluster Demo: Behavioral Fraud & Bot Detection

An end-to-end unsupervised anomaly clustering framework paired with an interactive high-fidelity dashboard to mathematically isolate, flag, and quarantine automated traffic spikes (bot scripts) across e-commerce checkout nodes. 

This repository serves as a comprehensive practice in building, evaluating, and deploying an unsupervised spatial clustering model on multi-dimensional, unlabeled security telemetry.

---

## 🚀 Key Features

- **Unsupervised Anomaly Filter:** Powered by Scikit-Learn’s `IsolationForest` engine to identify malicious scripts based on spatial density patterns and structural path lengths without relying on historical fraud labels.
- **Enterprise-Grade UI/UX:** Built with Streamlit featuring a fully customized, injected Obsidian-Dark CSS layout configured for high-fidelity security simulations.
- **Asynchronous Log Terminal:** Features a streaming line-by-line terminal component leveraging Streamlit session-state to mimic real multi-threaded socket server deployments.
- **Dual Categorization States:** Dynamically partitions active sessions into a green cluster (`Inlier Configuration Match`) or a red containment zone (`Structural Outlier Separation`).
- **Real-Time Telemetry Panels:** Tracks live behavioral metrics (e.g., clicks/min, navigation latency delays, proxy routing signatures) against mathematical baseline boundaries.
- **Production Serialization:** Serializes trained spatial weight matrices into a lightweight `security_model.pkl` file via Joblib for instant integration into backend microservice layers.

---

## 🧠 Machine Learning Core & Mechanics

Traditional rule-based guardrails fail against highly adaptive bot networks. This pipeline approaches fraud as a spatial boundary segmentation problem:

1. **The Security Matrix:** Generates and processes a 1,000-sample matrix tracking 5 distinct operational user dimensions (including interaction frequencies, navigation intervals, and geometric network signatures).
2. **Density Isolation:** Rather than profiling normal behavior, the `IsolationForest` architecture isolates anomalies by randomly partitioning feature spaces. Because automated scripts exhibit extreme, zero-latency characteristics, they require significantly fewer structural splits to isolate compared to organic human profiles.
3. **Hyperplane Filtering:** Normal human browsing cadences cluster tightly inside a high-density hyperplane, while anomalous high-frequency automated vectors drift distinctly outside safe cluster boundaries.

---

## 🛠️ Tech Stack

- **Core Language:** Python 3.9+
- **Machine Learning & Modeling:** Scikit-Learn (`IsolationForest`)
- **Data Engineering:** Pandas, NumPy
- **Model Serialization:** Joblib (`security_model.pkl`)
- **Dashboard UI Framework:** Streamlit (Custom Obsidian-Dark CSS Injections)
