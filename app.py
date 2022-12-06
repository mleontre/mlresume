from pathlib import Path
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV_ML.pdf"
profile_pic = current_dir / "assets" / "profile_pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Цифровое Резюме| Мария Лукьянова "
PAGE_ICON = ":wave:"
NAME = "Мария Лукьянова "
DESCRIPTION = """
Администратор/управляющая"""
EMAIL = "Тел: 8(025)7013480"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Скачать Резюме",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
# st.write('\n')
# cols = st.columns(len(SOCIAL_MEDIA))
# for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
#     cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Навыки & квалификация")
st.write(
    """
- ✔️ Полное документальное сопровождение закупок (регистрация контрагентов, внесение изменений и дополнений в договора, их согласование и подписание, контроль исполнения обязательств по оплате и доставке, и т.д.);
- ✔️ Знание принципов управления товарными запасами
- ✔️ Поддержание необходимого товарного запаса на складах
- ✔️ Контроль цен от поставщика
- ✔️ Введение базы поставщиков, пополнение новыми
- ✔️ Участие в переговорах с функциональными подразделениями с целью достижения наиболее лучших цен и снижения стоимости во время закупок и поставок
- ✔️ Знание кассового аппарата, терминал, расчет и обслуживание покупателя, приготовление холодных и горячих алкогольных напитков, 
- ✔️ Стажировка и инструктаж персонала (приготовление еды и напитков, сбор заказов)
- ✔️ Организация жизнедеятельности точки (заказ продукции, взаимодействие с поставщиками)


"""
)


# # --- SKILLS ---
# st.write('\n')
# st.subheader("Hard Skills")
# st.write(
#     """
# - 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
# - 📊 Data Visulization: PowerBi, MS Excel, Plotly
# - 📚 Modeling: Logistic regression, linear regression, decition trees
# - 🗄️ Databases: Postgres, MongoDB, MySQL
# """
# )


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Опыт работы")
st.write("---")

# --- JOB 1
st.write("🚧", "**Старший администратор/управляющий | ООО «Веселый повар»**")
st.write("2021-2022")
st.write(
    """
- ► обеспечение жизнедеятельности точки продукцией,
- ► формирование заявок,
- ► контроль расчетов с поставщиками,
- ► ведение кассовой дисциплины,
- ► подбор и стажировка персонала
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Старший администратор/управляющий  | ООО «Бровни» **")
st.write("2019-2021")
st.write(
    """
- ► обеспечение жизнедеятельности точки продукцией,
- ► формирование заявок,
- ► контроль расчетов с поставщиками,
- ► ведение кассовой дисциплины,
- ► подбор и стажировка персонала
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Продавец(опт и розница)   | Продукты для животных  **")
st.write("2017- 2019 ")
st.write(
    """
- ► розничная торговля, 
- ► консультация по ассортименту,
- ► формирование заявок на пополнение склада, 
- ► сбор заявок для интернет-магазина,
- ► обслуживание и расчет покупателей
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Образование")
st.write("---")
# for project, link in PROJECTS.items():
#     st.write(f"[{project}]({link})")
st.write(
    """
- ► Аграрно-технический лицей (продавец-кассир) 
- ► Машиностроительный техникум, специализация - бухгалтерский учет, анализ и контроль
"""
)


st.write('\n')
st.subheader("Личные качества")
st.write("---")
# for project, link in PROJECTS.items():
#     st.write(f"[{project}]({link})")
st.write(
    """
- ► организаторские способности, коммуникабельность, ориентация на результат;  
- ► предприимчивость, творческий подход, оптимизм; 
- ► готовность брать ответственность за результаты, грамотная речь, настойчивость, организованность.
"""
)
