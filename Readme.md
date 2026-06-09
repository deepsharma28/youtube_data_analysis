# 🎥 YouTube Trending Data Pipeline on AWS

An end-to-end AWS Data Engineering project implementing a **Medallion Architecture (Bronze → Silver → Gold)** for YouTube Trending Analytics. The pipeline automates data ingestion, transformation, validation, aggregation, monitoring, and reporting using AWS services.

---

## 📑 Table of Contents

- [Architecture](#-architecture)
- [Data Flow](#-data-flow)
- [Bronze Layer](#-bronze-layer)
- [Silver Layer](#-silver-layer)
- [Data Quality Framework](#-data-quality-framework)
- [Gold Layer](#-gold-layer)
- [AWS Services Used](#-aws-services-used)
- [Pipeline Orchestration](#-pipeline-orchestration)
- [Monitoring & Alerts](#-monitoring--alerts)
- [Analytics Layer](#-analytics-layer)
- [Project Outcomes](#-project-outcomes)

---

## 🏗️ Architecture

![YouTube Data Pipeline](images/youtube-pipeline-architecture.png)

---

## 🔄 Data Flow

The pipeline follows a Medallion Architecture where raw YouTube Trending data is first ingested into the Bronze layer and stored in Amazon S3. AWS Lambda and AWS Glue then transform, cleanse, and standardize the data in the Silver layer while performing validation and quality checks. After passing the quality gate, AWS Glue creates business-ready aggregated datasets in the Gold layer. The final data is queried through Amazon Athena and visualized using BI tools such as Power BI and Amazon QuickSight. Monitoring, alerting, and orchestration are handled through CloudWatch, SNS, IAM, and Step Functions.

---

## 🥉 Bronze Layer

### Purpose
Store raw source data without modification.

### Components

| Service | Responsibility |
|----------|---------------|
| Amazon S3 | Raw data storage |
| AWS Glue Crawler | Metadata discovery |
| IAM | Access control |

### Data Stored

- Raw JSON files
- Raw CSV files
- Original source datasets
- Historical archive

---

## 🥈 Silver Layer

### Purpose
Clean, standardize, and validate data.

### Components

| Service | Responsibility |
|----------|---------------|
| AWS Lambda | JSON transformation |
| AWS Glue ETL | Data cleansing |
| Amazon S3 | Cleaned storage |
| Glue Catalog | Metadata registration |

### Transformations

- Null handling
- Duplicate removal
- Schema validation
- Data type conversion
- Standardized column names
- Parquet conversion

### Output

- Clean analytical datasets
- Curated parquet tables

---

## ✅ Data Quality Framework

Before data moves to Gold, validation checks are executed.

### Validation Checks

| Check | Purpose |
|---------|---------|
| Row Count Validation | Ensure records exist |
| Null Percentage Check | Detect excessive missing values |
| Duplicate Detection | Prevent duplicate records |
| Schema Validation | Verify expected structure |
| Data Type Validation | Validate column formats |

### Failure Handling

- Lambda validation execution
- SNS failure notification
- CloudWatch logging
- Pipeline stop on failure

---

## 🥇 Gold Layer

### Purpose
Generate business-ready analytical datasets.

### Aggregated Tables

| Table | Description |
|---------|------------|
| trending_analytics | Trending video metrics |
| channel_analytics | Channel performance analysis |
| category_analytics | Category-level insights |

### Output

- KPI datasets
- Analytical tables
- Reporting-ready parquet files

---

## ☁️ AWS Services Used

| Service | Purpose |
|----------|----------|
| Amazon S3 | Data Lake Storage |
| AWS Glue | ETL Processing |
| AWS Glue Catalog | Metadata Management |
| AWS Lambda | Data Transformation & Validation |
| Amazon Athena | SQL Analytics |
| Amazon SNS | Alert Notifications |
| Amazon CloudWatch | Monitoring & Logging |
| AWS Step Functions | Workflow Orchestration |
| AWS IAM | Roles & Permissions |

---

## ⚙️ Pipeline Orchestration

AWS Step Functions orchestrates the complete workflow:

```text
Ingestion
   ↓
Wait
   ↓
Silver Transformations
   ↓
Data Quality Validation
   ↓
Gold Aggregations
   ↓
Success Notification
```

---

## 🔔 Monitoring & Alerts

### Amazon SNS

- Success notifications
- Failure alerts
- Data quality alerts

### Amazon CloudWatch

- Pipeline logs
- Error tracking
- Operational monitoring

---

## 📊 Analytics Layer

The final Gold datasets are consumed through:

- Amazon Athena
- Power BI
- Amazon QuickSight

Business users can perform:

- Trending analysis
- Channel performance tracking
- Category comparisons
- KPI reporting

---

## 🚀 Project Outcomes

✅ Automated Data Pipeline

✅ Bronze-Silver-Gold Architecture

✅ Data Quality Validation Framework

✅ Event-Driven Processing

✅ Automated SNS Alerting

✅ Analytics-Ready Data Lake

✅ Athena Query Layer

✅ Power BI Dashboard Integration

---

## 👨‍💻 Author

**Deep Sharma**

Data Engineering | AWS | Python | SQL | Power BI

GitHub: https://github.com/deepsharma28

LinkedIn: https://linkedin.com/in/deep-m-sharma