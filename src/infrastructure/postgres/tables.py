"""
UserData
    email: nullable
    tg_nickname: nullable
User
    username
    password
    roll: RollEnum
Tag
    name
Page
    name
    about
    is_private

    tags: m2m with tag
    owner: fk to User
    followers: m2m with User
    follow_requests: m2m with User
    unblock_date # время до которого страница будет заблокана

    maybe add separated models followers and follow_requests

"""
from datetime import datetime
from uuid import UUID, uuid4
from typing import List, Optional
import asyncio

from sqlalchemy import (
    ForeignKey,
    String,
    DateTime,
    UniqueConstraint,
    select,
    func,
)
from sqlalchemy.orm import (
    Mapped, 
    mapped_column, 
    relationship, 
    joinedload
)

from src.config.db_settings import Base, async_session
from domain.auth.value_objects import RoleEnum


class BaseModel(Base):
    """Abstract class to implement id field"""
    __abstract__ = True
    id: Mapped[UUID] = mapped_column(
        primary_key=True, index=True, unique=True, default=uuid4()
    )

"""
UserModel:UserModel - FollowersModel
UserModel:UserModel - FollowRequestsModel
PageModel:TagModel - PagesTagesModel

it's like a m2m table
1: 1 1
2: 1 1
- it's a bad case because the same page has the same tag twice - it's bullshit
implementation question
UniqueConstraint vs PrimaryKey by few fields - btw is it even possible to solve this issue by PKs?

"""

class UserDataModel(BaseModel):
    __tablename__ = 'users_data'
    email: Mapped[Optional[str]] = mapped_column(unique=True, index=True)
    tg_nickname: Mapped[Optional[str]] = mapped_column(unique=True, index=True)

    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE")
    )

    user: Mapped["UserModel"] = relationship(back_populates='user_data')


class UserModel(BaseModel): 
    __tablename__ = 'users'
    username: Mapped[str] = mapped_column(
        String(49), unique=True, index=True
    )
    password: Mapped[str] = mapped_column(String(155))
    unblock_date: Mapped[Optional[datetime]]
    roll: Mapped[RoleEnum]

    user_data: Mapped["UserDataModel"] = relationship(
        back_populates='user')
    pages: Mapped[List["PageModel"]] = relationship(
        back_populates='owner')
    follower_page_links: Mapped[List["PagesFollowersModel"]] = relationship(
        back_populates="follower")
    requester_page_links: Mapped[List["PagesRequestsModel"]] = relationship(
        back_populates="requester"
    )


class TagModel(BaseModel):
    """Tags for pages"""
    __tablename__ = 'tags'
    name: Mapped[str] = mapped_column(
        String(49), unique=True, index=True
    )

    tag_page_links: Mapped[List["PagesTagsModel"]] = relationship(
        back_populates='tag')
    

class PageModel(BaseModel):
    __tablename__ = 'pages'
    name: Mapped[str] = mapped_column(
        String(49), unique=True, index=True
    )
    about: Mapped[Optional[str]] = mapped_column(String(1024))
    is_private: Mapped[bool] = mapped_column(default=False)
    unblock_date: Mapped[Optional[datetime]]

    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL")
    )

    owner: Mapped["UserModel"] = relationship(back_populates='pages')
    page_tag_links: Mapped[List["PagesTagsModel"]] = relationship(
        back_populates='page')
    page_follower_links: Mapped[List["PagesFollowersModel"]] = relationship(
        back_populates='page'
    )
    page_requester_links: Mapped[List["PagesRequestsModel"]] = relationship(
        back_populates='page'
    )
    posts: Mapped[List["PostModel"]] = relationship(
        back_populates="page"
    )

    # follow_requests: Mapped[List["UserModel"]] = relationship(
    #     back_populates='requested_pages'
    # )


class PagesFollowersModel(BaseModel):
    __tablename__ = "pages_followers"
    follower_id: Mapped[UUID] = mapped_column(
        ForeignKey('users.id', ondelete='CASCADE'))
    page_id: Mapped[UUID] = mapped_column(
        ForeignKey('pages.id', ondelete='CASCADE'))
    created_at: Mapped[datetime] = mapped_column(
        default=func.now)
    
    follower: Mapped["UserModel"] = relationship(
        back_populates="follower_page_links")
    page: Mapped["PageModel"] = relationship(
        back_populates="page_follower_links")


class PagesRequestsModel(BaseModel):
    __tablename__ = "pages_requests"
    requester_id: Mapped[UUID] = mapped_column(
        ForeignKey('users.id', ondelete='CASCADE'))
    page_id: Mapped[UUID] = mapped_column(
        ForeignKey('pages.id', ondelete='CASCADE'))
    created_at: Mapped[datetime] = mapped_column(
        default=func.now)
    
    requester: Mapped["UserModel"] = relationship(
        back_populates="requester_page_links")
    page: Mapped["PageModel"] = relationship(
        back_populates="page_requester_links")


class PagesTagsModel(Base):
    __tablename__ = "pages_tags"
    page_id: Mapped[UUID] = mapped_column(
        ForeignKey('pages.id', ondelete='CASCADE'), primary_key=True)
    tag_id: Mapped[UUID] = mapped_column(
        ForeignKey('tags.id', ondelete="CASCADE"), primary_key=True)

    page: Mapped[PageModel] = relationship(
        back_populates="page_tag_links")
    tag: Mapped[TagModel] = relationship(
        back_populates="tag_page_links")
    

class PostModel(BaseModel):
    __tablename__ = 'posts'
    title: Mapped[str] = mapped_column(String(1024))
    body: Mapped[str] = mapped_column(String(16384))
    created_at: Mapped[datetime] = mapped_column(
        default=func.now, index=True)
    
    page_id: Mapped[UUID] = mapped_column(
        ForeignKey('pages.id', ondelete='CASCADE'))

    page: Mapped["PageModel"] = relationship(
        back_populates="posts"
    )

async def test_db():
    async with async_session() as session:
        print("wassap")
        stmt = (
            select(PageModel)
            .options(
                joinedload(PageModel.page_tag_links).joinedload(PagesTagsModel.tag)
                )
            )
        result = await session.execute(stmt)
        pages = result.scalars().unique().all()
        # ===
        print(pages)
        for p in pages:
            print(p.page_tag_links)
            for pt in p.page_tag_links:
                print(pt.tag.name)
        return pages



# class FollowersModel(BaseModel):
#     __tablename__ = "pages_followers"
#     page_id: Mapped[UUID] = mapped_column(
#         ForeignKey('pages.id', ondelete='CASCADE'))
#     user_id: Mapped[UUID] = mapped_column(
#         ForeignKey('tags.id', ondelete="CASCADE"))
#     created_at: Mapped[DateTime] = mapped_column(
#         server_default=func.now(), nullable=False
#     )

#     page: Mapped[PageModel] = relationship(back_populates="")
#     user: Mapped[TagModel] = relationship(back_populates="")

#     __table_args__ = (
#         UniqueConstraint("page_id", "user_id", name="uq_page_id_user_id"),
#     )
# maybe add separated models followers and follow_requests



# class PagesTagesModel(BaseModel):
    