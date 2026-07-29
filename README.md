# 🎯 ML Recommender Systems

[![CI/CD](https://github.com/twomathematicians-code/ml-recommender-systems/actions/workflows/ci.yml/badge.svg)](https://github.com/twomathematicians-code/ml-recommender-systems/actions)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker)](https://hub.docker.com/)
[![FAISS](https://img.shields.io/badge/FAISS-Vector_Search-00BFFF)](https://github.com/facebookresearch/faiss)

**Production recommendation engine with collaborative filtering, content-based, and hybrid approaches — FAISS-powered vector search for real-time recommendations at scale.**

---

## 🎯 Recommendation Modules

| Module | Algorithm | Use Case |
|---|---|---|
| **Collaborative Filtering** | Matrix Factorization (SVD) | User-item interactions |
| **Content-Based** | TF-IDF + Cosine Similarity | Item metadata matching |
| **Hybrid Recommender** | Ensemble + FAISS Index | Best of both worlds |
| **Vector Search** | FAISS + Embeddings | Real-time similar items |

---

## 🚀 Quick Start

```bash
git clone https://github.com/twomathematicians-code/ml-recommender-systems.git
cd ml-recommender-systems
docker-compose up --build
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/v1/recommend/user` | User-based recommendations |
| `POST` | `/api/v1/recommend/item` | Similar items |
| `POST` | `/api/v1/recommend/hybrid` | Hybrid recommendations |
| `GET` | `/api/v1/health` | Health check |

---

## 👤 Author

**Mahesh Solanki** — [LinkedIn](https://linkedin.com/in/maheshsolanki-16b9a6a5) | [GitHub](https://github.com/twomathematicians-code)
