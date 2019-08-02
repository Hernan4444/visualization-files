from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime, timedelta
import os
import pandas as pd
from dotenv import load_dotenv
from pathlib import Path  # python3 only
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


def get_text(element):
    text = element.text.strip()
    if "-" in text:
        return text.split("-")[1].strip()
    return text


def get_dataset():
    if 'GOOGLE_CHROME_BIN' in os.environ:
        GOOGLE_CHROME_BIN = os.environ['GOOGLE_CHROME_BIN']
    else:
        GOOGLE_CHROME_BIN = os.path.join(
            "/", "Applications", "Google Chrome.app", "Contents", "MacOS", "Google Chrome")

    if 'CHROME_DRIVER' in os.environ:

        CHROME_DRIVER = os.environ['CHROME_DRIVER']
    else:
        CHROME_DRIVER = os.path.join('/', 'Library', 'chromedriver')

    options = Options()
    if 'GOOGLE_CHROME_BIN' in os.environ:
        options.add_argument("--headless")
        options.binary_location = GOOGLE_CHROME_BIN

    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    if 'GOOGLE_CHROME_BIN' in os.environ:
        driver = webdriver.Chrome(executable_path=CHROME_DRIVER, options=options)
        time_ = datetime.now() - timedelta(hours=4)
    else:
        driver = webdriver.Safari()
        time_ = datetime.now()

    driver.get("http://buscacursos.uc.cl/?cxml_semestre=2019-2&cxml_sigla=IIC1&cxml_nrc=&cxml_nombre=&cxml_categoria=TODOS&cxml_profesor=&cxml_campus=TODOS&cxml_unidad_academica=TODOS&cxml_horario_tipo_busqueda=si_tenga&cxml_horario_tipo_busqueda_actividad=TODOS#resultados")



    for grade in driver.find_elements_by_class_name("resultadosRowPar"):
        row = grade.find_elements_by_tag_name('td')
        sigle = row[1].text
        section = row[4].text
        teacher = row[8].text
        
        print('"{}-{}": "{}",'.format(sigle.strip(), section, teacher))
    
    for grade in driver.find_elements_by_class_name("resultadosRowImpar"):
        row = grade.find_elements_by_tag_name('td')
        sigle = row[1].text
        section = row[4].text
        teacher = row[8].text
        
        print('"{}-{}": "{}",'.format(sigle.strip(), section, teacher))
    
    driver.get("http://buscacursos.uc.cl/?cxml_semestre=2019-2&cxml_sigla=IIC2&cxml_nrc=&cxml_nombre=&cxml_categoria=TODOS&cxml_profesor=&cxml_campus=TODOS&cxml_unidad_academica=TODOS&cxml_horario_tipo_busqueda=si_tenga&cxml_horario_tipo_busqueda_actividad=TODOS#resultados")

    inputElement = driver.find_elements_by_class_name("resultadosRowPar")

    data = []

    for grade in driver.find_elements_by_class_name("resultadosRowPar"):
        row = grade.find_elements_by_tag_name('td')
        sigle = row[1].text
        section = row[4].text
        teacher = row[8].text
        
        print('"{}-{}": "{}",'.format(sigle.strip(), section, teacher))
    
    for grade in driver.find_elements_by_class_name("resultadosRowImpar"):
        row = grade.find_elements_by_tag_name('td')
        sigle = row[1].text
        section = row[4].text
        teacher = row[8].text
        
        print('"{}-{}": "{}",'.format(sigle.strip(), section, teacher))
    
    
    driver.get("http://buscacursos.uc.cl/?cxml_semestre=2019-2&cxml_sigla=IIC3&cxml_nrc=&cxml_nombre=&cxml_categoria=TODOS&cxml_profesor=&cxml_campus=TODOS&cxml_unidad_academica=TODOS&cxml_horario_tipo_busqueda=si_tenga&cxml_horario_tipo_busqueda_actividad=TODOS#resultados")

    inputElement = driver.find_elements_by_class_name("resultadosRowPar")

    data = []

    for grade in driver.find_elements_by_class_name("resultadosRowPar"):
        row = grade.find_elements_by_tag_name('td')
        sigle = row[1].text
        section = row[4].text
        teacher = row[8].text
        
        print('"{}-{}": "{}",'.format(sigle.strip(), section, teacher))
    
    for grade in driver.find_elements_by_class_name("resultadosRowImpar"):
        row = grade.find_elements_by_tag_name('td')
        sigle = row[1].text
        section = row[4].text
        teacher = row[8].text
        
        print('"{}-{}": "{}",'.format(sigle.strip(), section, teacher))
    
    driver.close()


if __name__ == "__main__":
    get_dataset()
