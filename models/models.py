import config.environment as env
from sqlalchemy import Column, Date, DateTime, Float, ForeignKey, String, Text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Algorithm(Base):
    __tablename__ = 'algorithm'

    id = Column(INTEGER(11), primary_key=True)
    algorithm_id = Column(INTEGER(11), nullable=False)
    algorithm_name = Column(String(255, 'utf8_unicode_ci'))
    match_condition_id = Column(String(100, 'utf8_unicode_ci'), nullable=False)
    match_condition_content = Column(Text(collation='utf8_unicode_ci'))
    created_date = Column(DateTime, nullable=False)
    last_updated = Column(DateTime, nullable=False)


class AlgorithmParameter(Base):
    __tablename__ = 'algorithm_parameters'

    id = Column(INTEGER(11), primary_key=True)
    ticker_id = Column(String(100, 'utf8_unicode_ci'), nullable=False)
    bb_hoi_tu = Column(Float)
    bb_phan_ky = Column(Float)
    macd_levels = Column(String(255, 'utf8_unicode_ci'))
    rsi_top = Column(String(255, 'utf8_unicode_ci'))
    rsi_bottom = Column(String(255, 'utf8_unicode_ci'))
    volum_times = Column(INTEGER(11))
    volum_rollback_days = Column(INTEGER(11))
    created_date = Column(DateTime, nullable=False)
    last_updated = Column(DateTime, nullable=False)


class AlgorithmAnalysis(Base):
    __tablename__ = 'algorithm_analysis'

    id = Column(INTEGER(11), primary_key=True)
    ticker_id = Column(String(100, 'utf8_unicode_ci'), nullable=False)
    matching_date = Column(DateTime)
    algorithm_id = Column(INTEGER(11))
    bb_distance = Column(Float)
    macd_9 = Column(Float)
    macd_signal = Column(Float)
    rsi_value = Column(Float)
    volumn_value = Column(INTEGER(11))
    vol_times = Column(INTEGER(11))
    matching_condition_1 = Column(String(100, 'utf8_unicode_ci'))
    matching_condition_2 = Column(String(100, 'utf8_unicode_ci'))
    matching_condition_3 = Column(String(100, 'utf8_unicode_ci'))
    matching_condition_4 = Column(String(100, 'utf8_unicode_ci'))
    matching_condition_5 = Column(String(100, 'utf8_unicode_ci'))
    matching_condition_6 = Column(String(100, 'utf8_unicode_ci'))
    created_date = Column(DateTime, nullable=False)
    last_updated = Column(DateTime, nullable=False)


class Industry(Base):
    __tablename__ = 'industry'

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(20, 'utf8_unicode_ci'), nullable=False)
    name_vn = Column(String(200, 'utf8_unicode_ci'))
    name_en = Column(String(200, 'utf8_unicode_ci'))
    created_date = Column(DateTime, nullable=False)
    last_updated = Column(DateTime, nullable=False)


class IndustryGroup(Base):
    __tablename__ = 'industry_group'

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(20, 'utf8_unicode_ci'), nullable=False)
    name_vn = Column(String(200, 'utf8_unicode_ci'))
    name_en = Column(String(200, 'utf8_unicode_ci'))
    created_date = Column(DateTime, nullable=False)
    last_updated = Column(DateTime, nullable=False)


class Sector(Base):
    __tablename__ = 'sector'

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(20, 'utf8_unicode_ci'), nullable=False)
    name_vn = Column(String(200, 'utf8_unicode_ci'))
    name_en = Column(String(200, 'utf8_unicode_ci'))
    created_date = Column(DateTime, nullable=False)
    last_updated = Column(DateTime, nullable=False)


class StockExchange(Base):
    __tablename__ = 'stock_exchange'

    id = Column(INTEGER(11), primary_key=True)
    exchange_code = Column(String(20, 'utf8_unicode_ci'), nullable=False, index=True)
    exchange_name_vn = Column(String(200, 'utf8_unicode_ci'))
    exchange_name_en = Column(String(200, 'utf8_unicode_ci'))
    currency = Column(String(20, 'utf8_unicode_ci'), nullable=False)
    created_date = Column(DateTime, nullable=False)
    last_updated = Column(DateTime, nullable=False)


class SubIndustry(Base):
    __tablename__ = 'sub_industry'

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(20, 'utf8_unicode_ci'), nullable=False, index=True)
    name_vn = Column(String(200, 'utf8_unicode_ci'))
    name_en = Column(String(200, 'utf8_unicode_ci'))
    created_date = Column(DateTime, nullable=False)
    last_updated = Column(DateTime, nullable=False)


class Security(Base):
    __tablename__ = 'security'

    id = Column(INTEGER(11), primary_key=True)
    ticker_id = Column(String(20, 'utf8_unicode_ci'), nullable=False, index=True)
    exchange_id = Column(ForeignKey('stock_exchange.id'), nullable=False, index=True)
    ticker_name_vn = Column(String(200, 'utf8_unicode_ci'))
    ticker_name_en = Column(String(200, 'utf8_unicode_ci'))
    sub_industry_id = Column(ForeignKey('sub_industry.code'), index=True)
    created_date = Column(DateTime, nullable=False)
    last_updated = Column(DateTime, nullable=False)

    exchange = relationship('StockExchange')
    sub_industry = relationship('SubIndustry')


class DailyPrice(Base):
    __tablename__ = 'daily_price'

    id = Column(BIGINT(20), primary_key=True)
    ticker_id = Column(ForeignKey('security.ticker_id'), nullable=False, index=True)
    price_date = Column(Date, nullable=False)
    open_price = Column(Float, nullable=False)
    high_price = Column(Float, nullable=False)
    low_price = Column(Float, nullable=False)
    close_price = Column(Float, nullable=False)
    volume = Column(INTEGER(11), nullable=False)
    created_date = Column(DateTime, nullable=False)
    last_updated = Column(DateTime, nullable=False)

    ticker = relationship('Security')


class FinanceAnalysis(Base):
    __tablename__ = 'finance_analysis'

    id = Column(INTEGER(11), primary_key=True)
    ticker_id = Column(ForeignKey('security.ticker_id'), index=True)
    year = Column(Text(collation='utf8_unicode_ci'))
    quarter = Column(Text(collation='utf8_unicode_ci'))
    klcp_niem_yiet = Column(Float(asdecimal=True))
    klcp_luu_hanh = Column(Float(asdecimal=True))
    von_hoa_thi_truong = Column(Float(asdecimal=True))
    tong_doanh_thu = Column(Float(asdecimal=True))
    doanh_thu_thuan = Column(Float(asdecimal=True))
    gia_von = Column(Float(asdecimal=True))
    loi_nhuan_gop = Column(Float(asdecimal=True))
    loi_nhuan_hdkd = Column(Float(asdecimal=True))
    loi_nhuan_tai_chinh = Column(Float(asdecimal=True))
    loi_nhuan_khac = Column(Float(asdecimal=True))
    tong_chi_phi = Column(Float(asdecimal=True))
    tong_loi_nhuan_truoc_thue = Column(Float(asdecimal=True))
    loi_nhuan_rong = Column(Float(asdecimal=True))
    loi_nhuan_sau_thue = Column(Float(asdecimal=True))
    loi_nhuan_sau_thue_cty_me = Column(Float(asdecimal=True))
    tong_tai_san_ngan_han = Column(Float(asdecimal=True))
    tong_tai_san = Column(Float(asdecimal=True))
    no_ngan_han = Column(Float(asdecimal=True))
    tong_no = Column(Float(asdecimal=True))
    von_chu_so_huu = Column(Float(asdecimal=True))
    tien_cho_vay = Column(Float(asdecimal=True))
    dau_tu_chung_khoan = Column(Float(asdecimal=True))
    gop_von_dau_tu_dai_han = Column(Float(asdecimal=True))
    tien_gui = Column(Float(asdecimal=True))
    von_va_cac_quy = Column(Float(asdecimal=True))
    eps_basic = Column(Float(asdecimal=True))
    eps_deluted = Column(Text(collation='utf8_unicode_ci'))
    book_value = Column(Float(asdecimal=True))
    pe = Column(Float(asdecimal=True))
    roa = Column(Float(asdecimal=True))
    roe = Column(Float(asdecimal=True))
    ros = Column(Float(asdecimal=True))
    gos = Column(Float(asdecimal=True))
    dar = Column(Float(asdecimal=True))
    gia_thi_truong = Column(Float(asdecimal=True))
    created_date = Column(DateTime)
    last_updated = Column(DateTime)

    ticker = relationship('Security')


def create_table():
    Base.metadata.create_all(env.engine)