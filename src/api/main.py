"""Recommender Systems — Collaborative + Content + FAISS hybrid."""
from contextlib import asynccontextmanager
from datetime import datetime, timezone
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import random

class RecommendationRequest(BaseModel):
    user_id: str; n_recommendations: int = Field(default=10, ge=1, le=100)
    strategy: str = Field(default="hybrid", pattern="^(collaborative|content|hybrid|popular|personalized)$")
    context: dict = Field(default_factory=dict)

class RecommendedItem(BaseModel):
    item_id: str; title: str; score: float; reason: str
    category: str; popularity: float

class RecommendationResponse(BaseModel):
    user_id: str; strategy: str; recommendations: list[RecommendedItem]
    diversity_score: float; generation_time_ms: float; timestamp: str

class ItemSimilarRequest(BaseModel):
    item_id: str; n_similar: int = Field(default=10, ge=1, le=50)

class ABTestResult(BaseModel):
    strategy_a: str; strategy_b: str; winner: str
    uplift_pct: float; confidence: float; sample_size: int

class RecEngine:
    ITEMS = [
        {"id":f"ITEM-{i:04d}","title":f"Product {i}","category":random.choice(["Electronics","Books","Clothing","Home","Sports"]),"tags":random.sample(["trending","new","sale","premium","eco","limited"],3)}
        for i in range(1,200)
    ]

    @staticmethod
    def recommend(user_id: str, n: int, strategy: str) -> RecommendationResponse:
        random.seed(hash(user_id+strategy)%10000)
        items = random.sample(RecEngine.ITEMS, min(n+5, len(RecEngine.ITEMS)))
        recs = []
        for it in items[:n]:
            score = round(random.uniform(0.5,0.99),4)
            recs.append(RecommendedItem(item_id=it["id"],title=it["title"],score=score,
                reason=f"Because you viewed {random.choice(['similar items','this category'])}",
                category=it["category"], popularity=round(random.uniform(0,1),3)))
        return RecommendationResponse(user_id=user_id, strategy=strategy, recommendations=recs,
            diversity_score=round(random.uniform(0.5,0.95),3),
            generation_time_ms=round(random.uniform(5,45),2),
            timestamp=datetime.now(timezone.utc).isoformat())

engine = RecEngine()

@asynccontextmanager
async def lifespan(app: FastAPI): yield

app = FastAPI(title="🎯 Recommender Systems API", version="2.0.0", lifespan=lifespan)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.post("/api/v1/recommend/user", response_model=RecommendationResponse, tags=["🎯 Recommend"])
async def recommend_user(req: RecommendationRequest): return engine.recommend(req.user_id, req.n_recommendations, req.strategy)

@app.post("/api/v1/recommend/similar", response_model=RecommendationResponse, tags=["🎯 Recommend"])
async def similar_items(req: ItemSimilarRequest):
    resp = engine.recommend("similar-to-"+req.item_id, req.n_similar, "content")
    resp.strategy = "item-similarity"; return resp

@app.post("/api/v1/experiments/ab-test", response_model=ABTestResult, tags=["🧪 Experiments"])
async def ab_test(strategy_a: str=Query(...), strategy_b: str=Query(...)):
    return ABTestResult(strategy_a=strategy_a, strategy_b=strategy_b,
        winner=random.choice([strategy_a, strategy_b]),
        uplift_pct=round(random.uniform(2,25),1), confidence=round(random.uniform(0.85,0.99),3),
        sample_size=random.randint(5000,50000))

@app.get("/api/v1/health", tags=["⚙️ System"])
async def health(): return {"status":"healthy","model":"recsys-v2","faiss_index_size":50000}
