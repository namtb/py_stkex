import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Date, Float
import config.environment as env

BASE = declarative_base()

class FinanceAnalysis(BASE):
    __tablename__ = "finance_analysis"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    ticker_id = Column(String(20), nullable=False)
    year = Column(String(4), nullable=False)
    quarter = Column(String(4), nullable=False)
    klcp_niem_yiet =  Column(Float(), nullable=True)
    klcp_luu_hanh =  Column(Float(), nullable=True)
    von_hoa_thi_truong =  Column(Float(), nullable=True)
    tong_doanh_thu = Column(Float(), nullable=True)
    doanh_thu_thuan =  Column(Float(), nullable=True)
    gia_von =  Column(Float(), nullable=True)
    loi_nhuan_gop =  Column(Float(), nullable=True)
    loi_nhuan_hdkd =  Column(Float(), nullable=True)
    loi_nhuan_tai_chinh =  Column(Float(), nullable=True)
    loi_nhuan_khac =  Column(Float(), nullable=True)
    tong_chi_phi =  Column(Float(), nullable=True)
    tong_loi_nhuan_truoc_thue =  Column(Float(), nullable=True)
    loi_nhuan_rong =  Column(Float(), nullable=True)
    loi_nhuan_sau_thue =  Column(Float(), nullable=True)
    loi_nhuan_sau_thue_cty_me =  Column(Float(), nullable=True)
    tong_tai_san_ngan_han =  Column(Float(), nullable=True)
    tong_tai_san =  Column(Float(), nullable=True)
    no_ngan_han =  Column(Float(), nullable=True)
    tong_no =  Column(Float(), nullable=True)
    von_chu_so_huu =  Column(Float(), nullable=True)
    tien_cho_vay =  Column(Float(), nullable=True)
    dau_tu_chung_khoan =  Column(Float(), nullable=True)
    gop_von_dau_tu_dai_han =  Column(Float(), nullable=True)
    tien_gui =  Column(Float(), nullable=True)
    von_va_cac_quy =  Column(Float(), nullable=True)
    eps_basic = Column(Float(), nullable=True)
    eps_deluted = Column(Float(), nullable=True)
    book_value = Column(Float(), nullable=True)
    pe = Column(Float(), nullable=True)
    roa = Column(Float(), nullable=True)
    roe = Column(Float(), nullable=True)
    ros = Column(Float(), nullable=True)
    gos = Column(Float(), nullable=True)
    dar = Column(Float(), nullable=True)
    created_date = Column(DateTime(50), nullable=False)
    last_updated = Column(DateTime(50), nullable=False)

    def __init__(
            self,id="" ,ticker_id="", year="", quarter="",
            klcp_niem_yiet="", klcp_luu_hanh="", von_hoa_thi_truong="",tong_doanh_thu="",
            doanh_thu_thuan="", gia_von="", loi_nhuan_gop="", loi_nhuan_hdkd="", loi_nhuan_tai_chinh="",
            loi_nhuan_khac="", tong_chi_phi="", tong_loi_nhuan_truoc_thue="", loi_nhuan_rong="",
            loi_nhuan_sau_thue="", loi_nhuan_sau_thue_cty_me="", tong_tai_san_ngan_han="",
            tong_tai_san="", no_ngan_han="",tong_no="", von_chu_so_huu="", tien_cho_vay="",
            dau_tu_chung_khoan="", gop_von_dau_tu_dai_han="", tien_gui="",von_va_cac_quy="",
            eps_basic="", eps_deluted= "", book_value="", pe="", roa="", roe="", ros="", gos="", dar="",
            created_date="", last_updated=""):
        date_format = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        self.id                         = id
        self.ticker_id                  = ticker_id
        self.year                       = year
        self.quarter                    = quarter
        self.klcp_niem_yiet             = klcp_niem_yiet
        self.klcp_luu_hanh              = klcp_luu_hanh
        self.von_hoa_thi_truong         = von_hoa_thi_truong
        self.tong_doanh_thu             = tong_doanh_thu
        self.doanh_thu_thuan            = doanh_thu_thuan
        self.gia_von                    = gia_von
        self.loi_nhuan_gop              = loi_nhuan_gop
        self.loi_nhuan_hdkd             = loi_nhuan_hdkd
        self.loi_nhuan_tai_chinh        = loi_nhuan_tai_chinh
        self.loi_nhuan_khac             = loi_nhuan_khac
        self.tong_chi_phi               = tong_chi_phi
        self.tong_loi_nhuan_truoc_thue  = tong_loi_nhuan_truoc_thue
        self.loi_nhuan_rong             = loi_nhuan_rong
        self.loi_nhuan_sau_thue         = loi_nhuan_sau_thue
        self.loi_nhuan_sau_thue_cty_me  = loi_nhuan_sau_thue_cty_me
        self.tong_tai_san_ngan_han      = tong_tai_san_ngan_han
        self.tong_tai_san               = tong_tai_san
        self.no_ngan_han                = no_ngan_han
        self.tong_no                    = tong_no
        self.von_chu_so_huu             = von_chu_so_huu
        self.tien_cho_vay               = tien_cho_vay
        self.dau_tu_chung_khoan         = dau_tu_chung_khoan
        self.gop_von_dau_tu_dai_han     = gop_von_dau_tu_dai_han
        self.tien_gui                   = tien_gui
        self.von_va_cac_quy             = von_va_cac_quy
        self.eps_basic                  = eps_basic
        self.eps_deluted                = eps_deluted
        self.book_value                 = book_value
        self.pe                         = pe
        self.roa                        = roa
        self.roe                        = roe
        self.ros                        = ros
        self.gos                        = gos
        self.dar                        = dar
        self.created_date               = date_format
        self.last_updated               = date_format
        if created_date != "":
            self.created_date   =  created_date
        if last_updated != "":
            self.last_updated   =  last_updated

    # listOfDicts = {"id": "1", "ticker_id": 10, "exchange_id": "",...},
    @classmethod
    def _alternative_init(self, dict_info):
        result = dict_info
        # sec_class = Security(self)
        date_format = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        if not dict_info: return False
        else:
            # if (dict_info["id"] != None): self.id = dict_info["id"]
            if ("ticker_id" in dict_info): self.ticker_id = dict_info.get("ticker_id")
            else:
                return False
            if ("klcp_niem_yiet" in dict_info): self.klcp_niem_yiet = dict_info.get("klcp_niem_yiet")
            else:
                result["klcp_niem_yiet"] = ""
                self.klcp_niem_yiet = ""
            if ("klcp_luu_hanh" in dict_info): self.klcp_luu_hanh	= dict_info.get("klcp_luu_hanh")
            else:
                result["klcp_luu_hanh"] = ""
                self.klcp_luu_hanh = ""
            if ("von_hoa_thi_truong" not in dict_info): self.von_hoa_thi_truong = dict_info.get("von_hoa_thi_truong")
            else:
                result["von_hoa_thi_truong"] = ""
                self.von_hoa_thi_truong = ""
            if ("tong_doanh_thu" in dict_info): self.tong_doanh_thu = dict_info.get("tong_doanh_thu")
            else:
                result["tong_doanh_thu"] = ""
                self.tong_doanh_thu = ""
            if ("doanh_thu_thuan" in dict_info): self.doanh_thu_thuan	= dict_info.get("doanh_thu_thuan")
            else:
                result["doanh_thu_thuan"] = ""
                self.doanh_thu_thuan = ""
            if ("gia_von" in dict_info): self.gia_von	= dict_info.get("gia_von")
            else:
                result["gia_von"] = ""
                self.gia_von = ""
            if ("loi_nhuan_gop" in dict_info): self.loi_nhuan_gop = dict_info.get("loi_nhuan_gop")
            else:
                result["loi_nhuan_gop"] = ""
                self.loi_nhuan_gop = ""
            if ("loi_nhuan_hdkd" in dict_info): self.loi_nhuan_hdkd = dict_info.get("loi_nhuan_hdkd")
            else:
                result["loi_nhuan_hdkd"] = ""
                self.loi_nhuan_hdkd = ""
            if ("loi_nhuan_tai_chinh" in dict_info): self.loi_nhuan_tai_chinh	= dict_info.get("loi_nhuan_tai_chinh")
            else:
                result["loi_nhuan_tai_chinh"] = ""
                self.loi_nhuan_tai_chinh = ""
            if ("loi_nhuan_khac" in dict_info): self.loi_nhuan_khac = dict_info.get("loi_nhuan_khac")
            else:
                result["loi_nhuan_khac"] = ""
                self.loi_nhuan_khac = ""
            if ("tong_chi_phi" in dict_info): self.tong_chi_phi = dict_info.get("tong_chi_phi")
            else:
                result["tong_chi_phi"] = ""
                self.tong_chi_phi = ""
            if ("tong_loi_nhuan_truoc_thue" in dict_info): self.tong_loi_nhuan_truoc_thue	= dict_info.get("tong_loi_nhuan_truoc_thue")
            else:
                result["tong_loi_nhuan_truoc_thue"] = ""
                self.tong_loi_nhuan_truoc_thue = ""
            if ("loi_nhuan_rong" in dict_info): self.loi_nhuan_rong = dict_info.get("loi_nhuan_rong")
            else:
                result["loi_nhuan_rong"] = ""
                self.loi_nhuan_rong = ""
            if ("loi_nhuan_sau_thue" in dict_info): self.loi_nhuan_sau_thue = dict_info.get("loi_nhuan_sau_thue")
            else:
                result["loi_nhuan_sau_thue"] = ""
                self.loi_nhuan_sau_thue = ""
            if ("loi_nhuan_sau_thue_cty_me" in dict_info): self.loi_nhuan_sau_thue_cty_me	= dict_info.get("loi_nhuan_sau_thue_cty_me")
            else:
                result["loi_nhuan_sau_thue_cty_me"] = ""
                self.loi_nhuan_sau_thue_cty_me = ""
            if ("tong_tai_san_ngan_han" in dict_info): self.tong_tai_san_ngan_han	= dict_info.get("tong_tai_san_ngan_han")
            else:
                result["tong_tai_san_ngan_han"] = ""
                self.tong_tai_san_ngan_han = ""
            if ("tong_tai_san" in dict_info): self.tong_tai_san = dict_info.get("tong_tai_san")
            else:
                result["tong_tai_san"] = ""
                self.tong_tai_san = ""
            if ("no_ngan_han" in dict_info): self.no_ngan_han	= dict_info.get("no_ngan_han")
            else:
                result["no_ngan_han"] = ""
                self.no_ngan_han = ""
            if ("tong_no" in dict_info): self.tong_no	= dict_info.get("tong_no")
            else:
                result["tong_no"] = ""
                self.tong_no = ""
            if ("von_chu_so_huu" in dict_info): self.von_chu_so_huu = dict_info.get("von_chu_so_huu")
            else:
                result["von_chu_so_huu"] = ""
                self.von_chu_so_huu = ""
            if ("tien_cho_vay" in dict_info): self.tien_cho_vay = dict_info.get("tien_cho_vay")
            else:
                result["tien_cho_vay"] = ""
                self.tien_cho_vay = ""
            if ("dau_tu_chung_khoan" in dict_info): self.dau_tu_chung_khoan = dict_info.get("dau_tu_chung_khoan")
            else:
                result["dau_tu_chung_khoan"] = ""
                self.dau_tu_chung_khoan = ""
            if ("gop_von_dau_tu_dai_han" in dict_info): self.gop_von_dau_tu_dai_han = dict_info.get("gop_von_dau_tu_dai_han")
            else:
                result["gop_von_dau_tu_dai_han"] = ""
                self.gop_von_dau_tu_dai_han = ""
            if ("tien_gui" in dict_info): self.tien_gui = dict_info.get("tien_gui")
            else:
                result["tien_gui"] = ""
                self.tien_gui = ""
            if ("von_va_cac_quy" in dict_info): self.von_va_cac_quy = dict_info.get("von_va_cac_quy")
            else:
                result["von_va_cac_quy"] = ""
                self.von_va_cac_quy = ""
            if (dict_info.get("created_date") != ""):
                self.created_date = dict_info.get("created_date")
            else:
                self.created_date = date_format

            if (dict_info.get("last_updated") != ""):
                self.last_updated = dict_info.get("last_updated")
            else:
                self.last_updated = date_format

        return self

    # Get all attributes of class
    def _props(self):
        return [i for i in self.__dict__.keys() if i[:1] != '_']

    # Get all attributes of class
    def _dictionary_values_in_class(object):
        result = {}
        for i in object.__dict__.keys():
            if i[:1] != '_':
                result[i] = object.__dict__[i]
        return result

def create_table():
    BASE.metadata.create_all(env.engine)
    print("Finance analysis table was created successfullly.")
