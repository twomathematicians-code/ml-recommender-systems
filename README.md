# 🎯 Recommender Systems — Hybrid Engine

<p>
  <img src="https://img.shields.io/badge/FAISS-Vector_Search-2196F3" />
  <img src="https://img.shields.io/badge/Scipy-SVD_Optimization-7B1FA2" />
  <img src="https://img.shields.io/badge/FastAPI-Production-009688" />
  <img src="https://img.shields.io/badge/AB_Testing-Built_In-FF9800" />
</p>

A production recommender supporting collaborative filtering, content-based, and hybrid approaches with A/B testing baked in.

## Run It

```bash
docker compose up -d
```

## What's Different Here

| Strategy | How It Works |
|:--|:--|
| `collaborative` | User-item matrix factorization via SVD |
| `content` | Item similarity via TF-IDF + cosine |
| `hybrid` | Blended scores from both |
| `popular` | Global trending with recency decay |
| `personalized` | User embedding + context features |

## API

```bash
# Get recommendations
curl -X POST http://localhost:8000/api/v1/recommend/user \
  -d '{"user_id": "U-42", "n_recommendations": 5, "strategy": "hybrid"}'

# A/B test two strategies
curl -X POST http://localhost:8000/api/v1/experiments/ab-test?strategy_a=collaborative&strategy_b=content
```

---

<p><i>Mahesh Solanki</i> · <a href="https://github.com/twomathematicians-code">GitHub</a></p>
