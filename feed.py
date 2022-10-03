import bs4
import pandas as pd



choice_mode = input('Выберите режим: \n 1.Поиск ID \n 2.Статистика по цене')

    
def search_and_stats(name_fale):
    if choice_mode == '1':
        name_fale = input('Введите имя файла. Файл должен быть в одной директории со скриптом')
        
        with open(name_fale, 'r') as xmlFile:
            xmlData = xmlFile.read()

        soup = bs4.BeautifulSoup(xmlData, "xml")
        val = int(input('Введите id')) 
        
        for start in soup.find_all('offer'):
            if int(start['id']) == val:
                return f'{val} Найден'
        print('id не найден') 
        
    if choice_mode == '2':
        name_fale = input('Введите имя файла. Файл должен быть в одной директории со скриптом')
        
        with open(name_fale, 'r') as xmlFile:
            xmlData = xmlFile.read()

        soup = bs4.BeautifulSoup(xmlData, "xml")
        list_price = []
        d = soup.find_all('price')
        for i in range(0,len(d)):
            list_price.append((d[i].get_text()))
            
        int_price = [int(i) for i in list_price]
        max_num = max(int_price)   
        num_ = 0
        list_categori_price = []
        
        while num_ < max_num:
            num_ += 1000
            list_categori_price.append(num_)

        out = (pd.Series(list_price).astype(int)
                 .sub(1).floordiv(1000)
                 .add(1).mul(1000)
                 .value_counts()
               )
        dd = out.to_frame(name='Число предложений')
        dd.sort_values(by='Число предложений', ascending=False)
        print(dd)

search_and_stats(choice_mode)

