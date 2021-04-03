import pandas as pd

data = pd.read_csv('world_population.tsv', sep='\t')
papers = pd.read_csv('papers_per_countries.csv', sep=',')
merged_data = papers.merge(data, left_on=['Country'], right_on=['name'], how='outer')
merged_data['Number_of_papers'] = merged_data['Number_of_papers'].fillna(0)
data_1 = merged_data[['id', 'Number_of_papers']]
data_1.to_csv('world_paper.tsv', sep='\t', index=False)
# print(data_1)
x = 0
# print(data['name'])
# print(papers['Country'])
for paper in list(papers['Country']):
    if paper not in list(data['name']):
        print(paper)
        x += 1
# print(x)