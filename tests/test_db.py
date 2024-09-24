from sqlalchemy import select

from fastapi_zero.models import User


def test_crate_user(session):
    user = User(
        username="teste2",
        email="teste1@gmail.com",
        password="teste",
    )
    session.add(user)
    session.commit()
    result = session.scalar(
        select(User).where(User.email == "teste1@gmail.com")
    )

    assert result.username == "teste2"
