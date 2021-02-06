import pandas as pd
from sklearn.preprocessing import scale

def preprocess(employee_data):
     # Filling NA values in 'rating_tahun_lalu' column with median
    employee_data['rating_tahun_lalu'] = employee_data['rating_tahun_lalu'].fillna(employee_data['rating_tahun_lalu'].median(skipna=True))

    # Filling NA values in 'pendidikan' column with most frequent data
    employee_data['pendidikan'] = employee_data['pendidikan'].fillna("Bachelor's")

    # Feature scaling
    employee_data['jumlah_training'] = scale(employee_data['jumlah_training'])
    employee_data['umur'] = scale(employee_data['umur'])
    employee_data['rating_tahun_lalu'] = scale(employee_data['rating_tahun_lalu'])
    employee_data['masa_kerja'] = scale(employee_data['masa_kerja'])
    employee_data['KPI_>80%'] = scale(employee_data['KPI_>80%'])
    employee_data['penghargaan'] = scale(employee_data['penghargaan'])
    employee_data['rata_rata_skor_training'] = scale(employee_data['rata_rata_skor_training'])
        # Encoding categorical variable
    departemen = pd.get_dummies(employee_data['departemen'],drop_first=True)
    wilayah = pd.get_dummies(employee_data['wilayah'],drop_first=True)
    pendidikan = pd.get_dummies(employee_data['pendidikan'],drop_first=True)
    jenis_kelamin = pd.get_dummies(employee_data['jenis_kelamin'],drop_first=True)
    rekrutmen = pd.get_dummies(employee_data['rekrutmen'],drop_first=True)
    print(employee_data.shape)
    employee_data.drop(['departemen','wilayah','pendidikan','jenis_kelamin','rekrutmen'], axis=1, inplace=True)
    employee_data = pd.concat([employee_data,departemen,wilayah,pendidikan,jenis_kelamin,rekrutmen],axis=1)
    print(employee_data.shape)
    return employee_data
