import configparser
import pandas as pd
import matplotlib.pyplot as plt
import re

# data cleaning function
def data_cleaning(df):

    df_cleaned = df.fillna(
        {
            'YEAR' : 0,
            'GENRE' : 'UNKNOWN',
            'RATING' : 0,
            'ONE-LINE' : 'UNKNOWN',
            'STARS' : 'UNKNOWN',
            'VOTES' : 0,
            'RunTime' : 0,
            'Gross' : 0
        }
    )
    return df_cleaned


def data_transformation(df, column="col"):
    
    # Transform the Year

    regex_pattern = r"(\(\d{4}-?\d{4}?\)|-\d{4})"
    df['extracted'] = df[column].str.extract(regex_pattern)

    return df



def data_analysis(df):
    
    #Movie with highest rating
    highest_rating_row  = df.loc[df['RATING'].idxmax()]
    movie_with_highest_rating = highest_rating_row['MOVIES']
    highest_rating_year = highest_rating_row['YEAR']
    return movie_with_highest_rating , highest_rating_year



def read_data():
    config = configparser.ConfigParser()
    config.read('access.config')
    movie_data = config.get('paths', 'movie_data_file_path')
    df = pd.read_csv(movie_data)
    return df
    

if __name__ == "__main__":
    df = read_data()
    #print(df.isna().any())
    #print(df.isna().sum())

    #df.isna().sum().plot(kind="bar")
    #plt.show()

    df_cleaned = data_cleaning(df)
    #print(df_cleaned.head(10))

    df_cleaned = data_transformation(df, "YEAR")

    movie_with_highest_rating,year = data_analysis(df_cleaned)
    print(movie_with_highest_rating,year)





