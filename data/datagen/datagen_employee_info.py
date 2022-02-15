import pandas as pd
from random import randint
import random
import numpy as np

def gen_employee_data(num_employess):
    employee_ids = [ii for ii in range(100,100 +num_employess)]
    df = pd.DataFrame(employee_ids, columns=["employee_id"])
    df['age'] = [randint(18, 55) for _ in range(0, num_employess)]
    df['pay'] = [randint(45000, 120000) for _ in range(0, num_employess)]
    df['height'] = [round(random.uniform(1,2), 2) for _ in range(0, num_employess)]
    male_or_female = [random.randint(0, 1) for _ in range(0, num_employess)]
    gender = []
    for mm in male_or_female:
        if mm==0:
            gender.append('Male')
        else:
            gender.append('Female')
    df['gender'] = gender

    return df

df = gen_employee_data(20)
print(df)

df.to_csv("../employee_data_20.csv", sep=',', encoding='utf-8', index=False)