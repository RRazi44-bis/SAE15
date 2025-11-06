from matplotlib import pyplot as plt

def generate_pie_chart(data_dict):
    list_used = []
    list_frequency = []
    
    for frequency, used in data_dict.items():
        assert type(used) == int, "The type of the data in the list must me int"
    
    for frequency, used in data_dict.items():
        list_frequency.append(frequency)
        list_used.append(used)
    
    fig = plt.figure(figsize=(10, 7))
    plt.pie(list_used, list_frequency)

