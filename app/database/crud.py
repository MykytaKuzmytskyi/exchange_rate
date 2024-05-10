from sqlalchemy import select

from app.database.models import ExchangeRate, async_session


async def get_rate_list() -> [ExchangeRate]:
    async with async_session() as session:
        query = select(ExchangeRate)
        rate_list = await session.execute(query)
        return [rate for rate in rate_list.scalars()]


async def set_rate(time, rate) -> None:
    async with async_session() as session:
        session.add(ExchangeRate(time=time, rate=rate))
        await session.commit()

