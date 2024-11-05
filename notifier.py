from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

login_url = "https://prod.ps.stonybrook.edu/psp/csprods/?cmd=login"
class_url = "https://prod.ps.stonybrook.edu/psp/csprods/EMPLOYEE/CAMP/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL?PORTALPARAM_PTCNAV=HC_SSR_SSENRL_CART_GBL&EOPP.SCNode=CAMP&EOPP.SCPortal=EMPLOYEE&EOPP.SCName=ADMN_SOLAR_SYSTEM&EOPP.SCLabel=Enrollment&EOPP.SCFName=HCCC_ENROLLMENT&EOPP.SCSecondary=true&EOPP.SCPTcname=PT_PTPP_SCFNAV_BASEPAGE_SCR&FolderPath=PORTAL_ROOT_OBJECT.CO_EMPLOYEE_SELF_SERVICE.SU_STUDENT_FOLDER.HCCC_ENROLLMENT.HC_SSR_SSENRL_CART_GBL&IsFolder=false"
