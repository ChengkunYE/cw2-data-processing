
import pandas as pd
input_file_path='D:/nottingham/research paper/Results_21Mar2022.csv'
output_file_path='data1.csv'
df=pd.read_csv(input_file_path)
pd.set_option('display.max_columns', None)
#Calculation of average values
grouped_data = df.groupby('diet_group').mean().reset_index()


Fish = grouped_data[grouped_data['diet_group'] == 'fish']
Meat = grouped_data[grouped_data['diet_group'] == 'meat']
meat50_data = grouped_data[grouped_data['diet_group'] == 'meat50']
meat100_data = grouped_data[grouped_data['diet_group'] == 'meat100']
vegan = grouped_data[grouped_data['diet_group'] == 'vegan']
veggie = grouped_data[grouped_data['diet_group'] == 'veggie']

# Display of average values
print(Fish[['mean_ghgs', 'mean_land', 'mean_watscar', 'mean_eut', 'mean_bio', 'mean_watuse', 'mean_acid']])
print(Meat[['mean_ghgs', 'mean_land', 'mean_watscar', 'mean_eut', 'mean_bio', 'mean_watuse', 'mean_acid']])
print(meat50_data[['mean_ghgs', 'mean_land', 'mean_watscar', 'mean_eut', 'mean_bio', 'mean_watuse', 'mean_acid']])
print(meat100_data[['mean_ghgs', 'mean_land', 'mean_watscar', 'mean_eut', 'mean_bio', 'mean_watuse', 'mean_acid']])
print(vegan[['mean_ghgs', 'mean_land', 'mean_watscar', 'mean_eut', 'mean_bio', 'mean_watuse', 'mean_acid']])
print(veggie[['mean_ghgs', 'mean_land', 'mean_watscar', 'mean_eut', 'mean_bio', 'mean_watuse', 'mean_acid']])

#column 0->Fish，1->Meat ，2->meat50，3->meat100，4->vegan，5->veggie
#The following data is the result of the above output
data = {
    'mean_ghgs': [5.133366, 7.553983, 5.797222, 11.425865, 2.612561, 4.518411],
    'mean_land': [6.85312, 13.086665, 8.662609, 24.010061, 4.510695, 6.542007],
    'mean_watscar': [18565.613639, 19284.331898, 17817.131705, 22497.223846, 15312.488198, 16470.226046],
    'mean_eut': [21.730615, 30.317774, 24.081761, 42.258796, 11.461199, 17.866328],
    'mean_bio': [257.354033, 318.944165, 272.634156, 422.000804, 124.367816, 252.861965],
    'mean_watuse': [798.555192, 863.87092, 782.299134, 974.222937, 450.019441, 569.308337],
    'mean_acid': [24.101781, 33.999236, 27.172879, 46.779738, 11.598582, 21.664146]
}

df = pd.DataFrame(data)

# Normalizing the data
df_normalized = (df - df.min()) / (df.max() - df.min())
df_normalized_sorted = df_normalized.sort_values(by=list(df_normalized.columns), ascending=False)
df_normalized_sorted.to_csv(output_file_path,index=False)
print(df_normalized)
print(df_normalized_sorted)