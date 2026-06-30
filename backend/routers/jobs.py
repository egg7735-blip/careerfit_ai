# backend/routers/jobs.py

from fastapi import APIRouter, HTTPException

router = APIRouter()

# 목업 데이터: 3일차에 실제 CSV 데이터로 교체한다
MOCK_JOBS = [
    {
        "id": 1,
        "company": "현대모비스",
        "company_size": "대기업",
        "title": "기계설계 엔지니어",
        "experience_years": 0,
        "required_skills": ["기계설계", "CAD", "3D 모델링"],
        "preferred_skills": ["SolidWorks", "CATIA", "기계요소설계"],
        "description": "자동차 부품의 설계 및 개발을 수행하고 제품 성능 개선과 설계 검증 업무를 담당합니다.",
        "deadline": "2026-09-01"
    },
    {
        "id": 2,
        "company": "KRAFTON",
        "company_size": "대기업",
        "title": "사운드 디자이너",
        "experience_years": 1,
        "required_skills": ["사운드 디자인", "DAW", "효과음 제작"],
        "preferred_skills": ["Wwise", "FMOD", "Field Recording"],
        "description": "게임의 효과음과 환경음을 제작하고 오디오 시스템을 구축하여 몰입감 있는 플레이 경험을 제공합니다.",
        "deadline": "2026-08-20"
    },
    {
        "id": 3,
        "company": "두산로보틱스",
        "company_size": "대기업",
        "title": "로봇 기구설계 엔지니어",
        "experience_years": 0,
        "required_skills": ["기계설계", "CAD", "기계요소설계"],
        "preferred_skills": ["SolidWorks", "ANSYS", "협동로봇"],
        "description": "협동로봇의 기구 설계 및 구조 해석을 수행하고, 제품 성능 개선과 신제품 개발에 참여합니다.",
        "deadline": "2026-09-10"
    }
]


@router.get("/jobs", tags=["Jobs"])
def get_jobs():
    """
    취업 공고 목록을 반환하는 엔드포인트.
    현재는 목업 데이터를 반환하며, 3일차에 실제 데이터로 교체한다.
    """

    return {
        "count": len(MOCK_JOBS),
        "jobs": MOCK_JOBS
    }


@router.get("/jobs/{job_id}", tags=["Jobs"])
def get_job_by_id(job_id: int):
    """
    특정 공고의 상세 정보를 반환한다.
    """

    for job in MOCK_JOBS:
        if job["id"] == job_id:
            return job

    raise HTTPException(
        status_code=404,
        detail=f"공고 ID {job_id}를 찾을 수 없습니다."
    )