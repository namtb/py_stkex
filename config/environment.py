import config.connectDB as connectDB
from sqlalchemy.orm import sessionmaker

engine = connectDB.connect_db_sqlalchemy()
Session = sessionmaker(bind=engine)
session = Session()

default_url = "https://iboard.ssi.com.vn/bang-gia/vn30"

finance_info_list_urls = {
    # "gvr": "https://s.cafef.vn/hose/GVR-tap-doan-cong-nghiep-cao-su-viet-nam.chn",
    # "pow": "https://s.cafef.vn/hose/pow-tong-cong-ty-dien-luc-dau-khi-viet-nam-ctcp.chn",
    "bvh": "https://s.cafef.vn/hose/BVH-tap-doan-bao-viet.chn",
    # "ctg": "https://s.cafef.vn/hose/CTG-ngan-hang-thuong-mai-co-phan-cong-thuong-viet-nam.chn",
    # "bid": "https://s.cafef.vn/hose/BID-ngan-hang-thuong-mai-co-phan-dau-tu-va-phat-trien-viet-nam.chn",
    # "vcb": "https://s.cafef.vn/hose/VCB-ngan-hang-thuong-mai-co-phan-ngoai-thuong-viet-nam.chn",
    # "tcb": "https://s.cafef.vn/hose/TCB-ngan-hang-tmcp-ky-thuong-viet-nam-techcombank.chn",
    # "vpb": "https://s.cafef.vn/hose/VPB-ngan-hang-thuong-mai-co-phan-viet-nam-thinh-vuong.chn",
    # "mbb": "https://s.cafef.vn/hose/MBB-ngan-hang-thuong-mai-co-phan-quan-doi.chn",
    # "vib": "https://s.cafef.vn/hose/VIB-ngan-hang-thuong-mai-co-phan-quoc-te-viet-nam.chn",
    # "tpb": "https://s.cafef.vn/hose/TPB-ngan-hang-thuong-mai-co-phan-tien-phong.chn",
    # "msb": "https://s.cafef.vn/hose/MSB-ngan-hang-thuong-mai-co-phan-hang-hai-viet-nam.chn",
    # "acb": "https://s.cafef.vn/hose/ACB-ngan-hang-thuong-mai-co-phan-a-chau.chn",
    # "eib": "https://s.cafef.vn/hose/EIB-ngan-hang-thuong-mai-co-phan-xuat-nhap-khau-viet-nam.chn",
    # "stb": "https://s.cafef.vn/hose/STB-ngan-hang-thuong-mai-co-phan-sai-gon-thuong-tin.chn",
    # "hdb": "https://s.cafef.vn/hose/HDB-ngan-hang-tmcp-phat-trien-tp-ho-chi-minh.chn",
    # "fpt": "https://s.cafef.vn/hose/FPT-cong-ty-co-phan-fpt.chn",
    # "gas": "https://s.cafef.vn/hose/GAS-tong-cong-ty-khi-viet-namctcp.chn",
    # "hpg": "https://s.cafef.vn/hose/HPG-cong-ty-co-phan-tap-doan-hoa-phat.chn",
    # "kdh": "https://s.cafef.vn/hose/KDH-cong-ty-co-phan-dau-tu-kinh-doanh-nha-khang-dien.chn",
    # "msn": "https://s.cafef.vn/hose/MSN-cong-ty-co-phan-tap-doan-masan.chn",
    # "mwg": "https://s.cafef.vn/hose/MWG-cong-ty-co-phan-dau-tu-the-gioi-di-dong.chn",
    # "nvl": "https://s.cafef.vn/hose/NVL-cong-ty-co-phan-tap-doan-dau-tu-dia-oc-no-va.chn",
    # "pdr": "https://s.cafef.vn/hose/PDR-cong-ty-co-phan-phat-trien-bat-dong-san-phat-dat.chn",
    # "plx": "https://s.cafef.vn/hose/PLX-tap-doan-xang-dau-viet-nam.chn",
    # "ree": "https://s.cafef.vn/hose/REE-cong-ty-co-phan-co-dien-lanh.chn",
    # "sbt": "https://s.cafef.vn/hose/SBT-cong-ty-co-phan-thanh-thanh-cong-bien-hoa.chn",
    # "ssi": "https://s.cafef.vn/hose/SSI-cong-ty-co-phan-chung-khoan-ssi.chn",
    # "tch": "https://s.cafef.vn/hose/TCH-cong-ty-co-phan-dau-tu-dich-vu-tai-chinh-hoang-huy.chn",
    # "vhm": "https://s.cafef.vn/hose/VHM-cong-ty-co-phan-vinhomes.chn",
    # "vic": "https://s.cafef.vn/hose/VIC-tap-doan-vingroup-cong-ty-co-phan.chn",
    # "vjc": "https://s.cafef.vn/hose/VJC-cong-ty-co-phan-hang-khong-vietet.chn",
    # "vre": "https://s.cafef.vn/hose/VRE-cong-ty-co-phan-vincom-retail.chn"
}

# define colum for ticket information type 1
list_ticket_type_1 = ["pow", "gvr","fpt","gas","hpg","kdh","msn","mwg","nvl","pdr","plx","ree","sbt","ssi","tch","vhm","vic","vjc","vre"]
list_colums_information_type_1 = {
    "doanh_thu_thuan": "rptNhomChiTieu_ctl00_rptData_ctl00_TrData",
    "gia_von": "rptNhomChiTieu_ctl00_rptData_ctl01_TrData",
    "loi_nhuan_gop": "rptNhomChiTieu_ctl00_rptData_ctl02_TrData",
    "loi_nhuan_tai_chinh": "rptNhomChiTieu_ctl00_rptData_ctl03_TrData",
    "loi_nhuan_khac": "rptNhomChiTieu_ctl00_rptData_ctl04_TrData",
    "tong_loi_nhuan_truoc_thue": "rptNhomChiTieu_ctl00_rptData_ctl05_TrData",
    "loi_nhuan_sau_thue": "rptNhomChiTieu_ctl00_rptData_ctl06_TrData",
    "loi_nhuan_sau_thue_cty_me": "rptNhomChiTieu_ctl00_rptData_ctl08_TrData",
    "tong_tai_san_ngan_han": "rptNhomChiTieu_ctl01_rptData_ctl00_TrData",
    "tong_tai_san": "rptNhomChiTieu_ctl01_rptData_ctl01_TrData",
    "no_ngan_han": "rptNhomChiTieu_ctl01_rptData_ctl02_TrData",
    "tong_no": "rptNhomChiTieu_ctl01_rptData_ctl03_TrData",
    "von_chu_so_huu": "rptNhomChiTieu_ctl01_rptData_ctl04_TrData"
}
# define colum for ticket information type 2
list_ticket_type_2 = ["bvh"]
list_colums_information_type_2 = {
    "tong_doanh_thu": "rptNhomChiTieu_ctl00_rptData_ctl00_TrData",
    "doanh_thu_thuan": "rptNhomChiTieu_ctl00_rptData_ctl01_TrData",
    "loi_nhuan_hdkd": "rptNhomChiTieu_ctl00_rptData_ctl02_TrData",
    "loi_nhuan_tai_chinh": "rptNhomChiTieu_ctl00_rptData_ctl03_TrData",
    "tong_loi_nhuan_truoc_thue": "rptNhomChiTieu_ctl00_rptData_ctl04_TrData",
    "loi_nhuan_sau_thue": "rptNhomChiTieu_ctl00_rptData_ctl05_TrData",
    "tong_tai_san_ngan_han": "rptNhomChiTieu_ctl01_rptData_ctl00_TrData",
    "tong_tai_san": "rptNhomChiTieu_ctl01_rptData_ctl01_TrData",
    "no_ngan_han": "rptNhomChiTieu_ctl01_rptData_ctl02_TrData",
    "tong_no": "rptNhomChiTieu_ctl01_rptData_ctl03_TrData",
    "von_chu_so_huu": "rptNhomChiTieu_ctl01_rptData_ctl04_TrData"
}

# define colum for ticket information type 3
list_ticket_type_3 = ["ctg","bid","vcb","tcb","vpb","mbb","vib","tpb","msb","acb","eib","stb","hdb"]
list_colums_information_type_3 = {
    "tong_doanh_thu": "rptNhomChiTieu_ctl00_rptData_ctl00_TrData",
    "tong_loi_nhuan_truoc_thue": "rptNhomChiTieu_ctl00_rptData_ctl01_TrData",
    "tong_chi_phi": "rptNhomChiTieu_ctl00_rptData_ctl02_TrData",
    "loi_nhuan_rong": "rptNhomChiTieu_ctl00_rptData_ctl03_TrData",
    "tong_tai_san": "rptNhomChiTieu_ctl01_rptData_ctl00_TrData",
    "tien_cho_vay": "rptNhomChiTieu_ctl01_rptData_ctl01_TrData",
    "dau_tu_chung_khoan": "rptNhomChiTieu_ctl01_rptData_ctl02_TrData",
    "gop_von_dau_tu_dai_han": "rptNhomChiTieu_ctl01_rptData_ctl03_TrData",
    "tien_gui": "rptNhomChiTieu_ctl01_rptData_ctl04_TrData",
    "von_va_cac_quy": "rptNhomChiTieu_ctl01_rptData_ctl05_TrData"
}

price_date_quarter = {
    "12021": "2021-03-31", "42020": "2020-12-31", "32020": "2020-09-30", "22020": "2020-06-30", "12020": "2020-03-31",
    "42019": "2019-12-31", "32019": "2019-09-30", "22019": "2019-06-28", "12019": "2019-03-29",
    "42018": "2018-12-28", "32018": "2018-09-28", "22018": "2018-06-29", "12018": "2018-03-30",
    "42017": "2017-12-29", "32017": "2017-09-29", "22017": "2017-06-30"
}