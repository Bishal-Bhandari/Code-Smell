from fastapi import APIRouter, Depends
from backend.schemas.review_schema import ReviewRequest
from backend.analysis_engine.analyzer import analyze_pr
from backend.auth.dependencies import get_current_user
from backend.services.usage_service import check_and_update_usage
from backend.db_service.db import db

router = APIRouter()


@router.post("/review")
async def review_code(
    request: ReviewRequest,
    current_user=Depends(get_current_user)
):

    # check subscription usage
    updated_user = check_and_update_usage(current_user)

    # Update usage in MongoDB
    await db.users.update_one(
        {"email": current_user["email"]},
        {
            "$set": {
                "usage_count": updated_user["usage_count"],
                "usage_reset_date": updated_user["usage_reset_date"],
            }
        }
    )

    # run AI analysis
    result = await analyze_pr(
        repo_url=request.repo_url,
        pr_number=request.pr_number
    )

    return result