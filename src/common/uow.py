from abc import ABC, abstractmethod

from src.config.db_settings import async_session
# from src.registration.modules.repos import UserRepository, TraderRepository, TraderGroupRepository
# from src.registration.models.models import UserModel, TraderModel, TraderGroupModel
# from src.traders.modules.repositories import RatesRepository, InvoicesRepository
# from src.traders.models import TraderRatesModel, TraderInvoiceModel
# from src.traders.modules.repositories import BalanceRepository
# from src.traders.models import TraderBalanceModel
# from src.requisites.modules.repositories import RequisiteRepository, BankRepository, PaymentSystemRepository, RequisiteBlockRepository
# from src.requisites.models import RequisiteModel, BankModel, PaymentSystemModel, RequisiteBlockModel


class UnitOfWork(ABC):

    @abstractmethod
    def __init__(self): ...

    @abstractmethod
    async def __aenter__(self): ...

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb): ...

    @abstractmethod
    async def commit(self): ...

    @abstractmethod
    async def rollback(self): ...


class UnitOfWorkImpl(UnitOfWork):
    def __init__(self):
        self.session_factory = async_session

    async def __aenter__(self):
        self.session = self.session_factory()

        # register repositories to UoW
        # self.user_repo = UserRepository(self.session, UserModel)
        # self.trader_repo = TraderRepository(self.session, TraderModel)
        # self.trader_group_repo = TraderGroupRepository(self.session, TraderGroupModel)
        # self.rates_repo = RatesRepository(self.session, TraderRatesModel)
        # self.balances_repo = BalanceRepository(self.session, TraderBalanceModel)
        # self.requisites_repo = RequisiteRepository(self.session, RequisiteModel)
        # self.banks_repo = BankRepository(self.session, BankModel)
        # self.invoices_repo = InvoicesRepository(self.session, TraderInvoiceModel)
        # self.payment_sys_repo = PaymentSystemRepository(self.session, PaymentSystemModel)
        # self.requisite_blocks_repo = RequisiteBlockRepository(self.session, RequisiteBlockModel)

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type:
                await self.rollback()
            else:
                await self.commit()
        finally:
            await self.session.close()

    async def rollback(self):
        await self.session.rollback()

    async def commit(self):
        await self.session.commit()
