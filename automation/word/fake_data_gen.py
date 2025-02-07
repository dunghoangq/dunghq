from faker import Faker
import pandas as pd

fake = Faker()

profiles = [fake.profile() for i in range(10)]

df_profile = pd.DataFrame(profiles)

df_numbers = [fake.phone_number() for i in range(10)]

df_profile['phone_number'] = df_numbers

def main():
    print(df_profile.columns)

if __name__ == '__main__':
    main()