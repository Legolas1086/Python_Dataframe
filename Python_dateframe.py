import pandas as pd 

list_data=[['Pele',1000,650,350],
          ['Ronaldo',750,650,100],
          ['Messi',700,630,70],['Ibrahimovic',600,550,50]]

def to_data_frame(list_data):
    Player=[i[0] for i in list_data]
    Career_Goals=[i[1] for i in list_data]
    Club_Goals=[i[2] for i in list_data]
    International_Goals=[i[3] for i in list_data]
    return zip(Player,Career_Goals,Club_Goals,International_Goals)

data_frame=pd.DataFrame(to_data_frame(list_data),columns=['Player','Career_Goals','Club_Goals','International_Goals'])
print(data_frame)