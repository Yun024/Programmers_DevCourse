from fastapi import APIRouter, HTTPException
from typing import List
from models import Member

router = APIRouter()

# 데이터 저장소
members_db = []

@router.get("/members", response_model=List[Member], summary="회원조회", description="모든 회원 정보를 조회합니다.")
async def get_members():
    return members_db

@router.post("/members", response_model=Member, summary="회원등록", description="새로운 회원을 등록합니다.")
async def create_member(member: Member):
    if any(existing_member.id == member.id for existing_member in members_db):
        raise HTTPException(status_code=400, detail="ID가 중복되었습니다.")
    members_db.append(member)
    return member

@router.delete("/members/{id}", response_model=List[Member], summary="회원삭제", description="주어진 ID의 회원을 삭제합니다.")
async def delete_member(id: int):
    global members_db
    members_db = [member for member in members_db if member.id != id]
    return members_db
