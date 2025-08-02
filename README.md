
# 🩺 VitalLens-AI-App

**VitalLens-AI-App** is an intelligent health diagnostics tool that leverages machine learning to provide predictive insights into a user’s vital health metrics. By analyzing parameters such as age, body temperature, weight, blood pressure, and cholesterol, the app classifies whether a user is likely at risk of underlying health issues like hypertension, hypercholesterolemia, or abnormal body temperature conditions — all without invasive tests.

This project is built with AWS Cloud technologies (Lambda, API Gateway, SageMaker, Amplify) using the AWS Free Tier, and integrates with a React-based frontend. It follows industry standards in cloud architecture and machine learning.


## ✅ Features

- 🔍 AI-driven prediction of health risks using basic vital signs.
- 📊 Trained model using `RandomForestClassifier` with realistic synthetic data.
- ☁️ Hosted on AWS (Amplify, Lambda, API Gateway, S3).
- 🧠 SageMaker-ready model training notebook (`sagemaker_notebook.ipynb`).
- 🔒 Secure, serverless backend using AWS Lambda.
- 📱 Interactive and mobile-responsive frontend (React).
- 📦 Easy to deploy and extend.
- 👩‍⚕️ Empowers early health intervention and monitoring in underserved regions.


## 🚀 Tech Stack

| Layer        | Technologies Used                             |
|--------------|------------------------------------------------|
| Frontend     | React.js, AWS Amplify, HTML5, CSS3             |
| Backend      | AWS Lambda (Python), API Gateway, S3           |
| ML Model     | Scikit-learn, pandas, numpy, joblib, SageMaker |
| DevOps       | GitHub, AWS CloudFormation, CI/CD via Amplify  |
| Hosting      | AWS Amplify (Frontend), S3 (Model/Assets)      |


## 📂 Project Structure


VitalLens-AI-App/
├── amplify/
│   └── backend-config.json
├── backend/
│   ├── lambda/
│   │   └── predict.py
│   └── model/
│       ├── generate\_health\_model.py
│       └── health\_model.pkl
├── cloudformation/
│   └── template.yaml
├── sagemaker/
│   └── sagemaker\_notebook.ipynb
├── react-app/
│   ├── public/
│   └── src/
│       ├── components/
│       └── App.js
├── LICENSE
├── README.md
└── .gitignore


## 📈 How It Works

1. **User Input**  
   The frontend collects age, weight, body temperature, blood pressure, and cholesterol level.

2. **Prediction Logic**  
   Data is sent via API Gateway to a Lambda function (`predict.py`) which loads a pre-trained model (`health_model.pkl`) and returns the prediction (Healthy / At Risk).

3. **Model Training**  
   Model is trained offline with synthetic yet realistic health data using `RandomForestClassifier` and stored as `health_model.pkl`.

4. **Cloud Hosting**  
   Frontend is hosted using AWS Amplify. Model and Lambda backend are deployed using CloudFormation.


## 🧠 Model Details

- Classifier: `RandomForestClassifier`
- Input Features: `age`, `weight`, `body_temp`, `bp_systolic`, `cholesterol`
- Output: `0` (Healthy), `1` (At Risk)
- Model File: `health_model.pkl`
- Training Data: Synthetic dataset of 1000 patients
- Notebook: `sagemaker/sagemaker_notebook.ipynb`

## 🌐 Live Demo (Coming Soon)

## ✅ Advantages of VitalLens-AI-App

* **Accessibility**: Remote health risk evaluation for underprivileged areas.
* **Preventive Care**: Early detection of high blood pressure and cholesterol risks.
* **Scalability**: Fully serverless architecture built with AWS Best Practices.
* **Customizability**: Easily extend the model to include more biomarkers or wearables data.
* **Educational**: Great for teaching ML + Cloud Computing integration.


## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/new`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new`)
5. Open a Pull Request


## 🙋‍♂️ Contact

Built by **[David Pascal](https://github.com/BishopDavid7)**
📧 Email: [p.fonjock@gmail.com](mailto:p.fonjock@gmail.com)
🌍 Location: Cameroon
🧑‍💻 Portfolio: [pascal-awsdevops.com](https://pascal-awsdevops.com)


## ⭐ Star This Project

If this project helped you, please give it a ⭐ on [GitHub](https://github.com/BishopDavid7/VitalLens-AI-App)!
