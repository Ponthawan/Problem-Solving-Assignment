import networkx as nx
import matplotlib.pyplot as plt

import tkinter as tk

G = nx.Graph()

G.add_edges_from([
    ('KMUTNB Prachinburi', '7-11 Noen Hom', {'distance': 1.1}),
    ('7-11 Noen Hom', '7-11 Naresuan', {'distance': 2.4}),
    ('7-11 Naresuan', '7-11 Phrom Yothi', {'distance': 0.6}),
    ('7-11 Naresuan', '7-11 Mai Khet', {'distance': 3.7}),
    ('7-11 Phrom Yothi', '7-11 Mai Khet', {'distance': 4.1}),
    ('7-11 Phrom Yothi', '7-11 Prachantakham', {'distance': 21.2}),
    ('7-11 Phrom Yothi', '7-11 Mueng', {'distance': 7}),
    ('7-11 Mai Khet', '7-11 Mueng', {'distance': 5.8}),
    ('7-11 Mueng', '7-11 Nha Mueng', {'distance': 1.3}),
    ('7-11 Mueng', '7-11 Ban Sang', {'distance': 25.8}),
    ('7-11 Nha Mueng', '7-11 Ban Sang', {'distance': 25.3}),
    ('7-11 Nha Mueng', '7-11 Sri Mahosot', {'distance': 29.2}),
    ('7-11 Nha Mueng', '7-11 Sri Maha Phot', {'distance': 30.4}),
    ('7-11 Ban Sang', '7-11 Sri Mahosot', {'distance': 29.9}),
    ('Ban Sang', '7-11 Ban Sang', {'distance': 8}),
    ('7-11 Sri Mahosot', '7-11 Khok kwang', {'distance': 13.7}),
    ('Sri Mahosot', '7-11 Sri Mahosot', {'distance': 4.5}),
    ('Sri Maha Phot', '7-11 Sri Maha Phot', {'distance': 14}),
    ('Sri Maha Phot', '7-11 Khok kwang', {'distance': 2.5}),
    ('7-11 Sri Maha Phot', '7-11 Khok kwang', {'distance': 2}),
    ('7-11 Sri Maha Phot', '7-11 Nadee', {'distance': 49.2}),
    ('7-11 Khok kwang', '7-11 Nadee', {'distance': 55.3}),
    ('7-11 Khok kwang', '7-11 Nikom 304', {'distance': 8.8}),
    ('Prachantakham','7-11 Prachantakham', {'distance': 0.4}),
    ('7-11 Prachantakham','7-11 Nadee', {'distance': 32.7}),
    ('7-11 Prachantakham','7-11 Sri Maha Phot', {'distance': 12.3}),
    ('Nadee','7-11 Nadee', {'distance': 13.7}),
    ('7-11 Nadee','7-11 Nikom 304', {'distance': 46.7}),
    ('7-11 Nikom 304','7-11 Kabin', {'distance': 45.8}),
    ('Kabin Buri','7-11 Kabin', {'distance': 21.4}) 
    ])


pos = {'KMUTNB Prachinburi':(1.8,10.4),'Kabin Buri':(9.2,0.5),'Nadee':(11.2,8),'Ban Sang':(1.6,1.4),'Prachantakham':(7.5,11.5),'Sri Maha Phot':(8.9,5),'Sri Mahosot':(4.6,2.5)
       ,'7-11 Noen Hom':(2.6,8.7),'7-11 Naresuan':(3.2,7.9),'7-11 Phrom Yothi':(4.6,6.9),'7-11 Mai Khet':(2.5,6.6),'7-11 Mueng':(2.8,4.7),'7-11 Nha Mueng':(5.3,5.9),'7-11 Ban Sang':(2,3.3)
       ,'7-11 Sri Mahosot':(5.2,3.6),'7-11 Sri Maha Phot':(7.2,7),'7-11 Khok kwang':(7,3),'7-11 Nikom 304':(10.2,4),'7-11 Kabin':(9.4,2.9),'7-11 Nadee':(8.6,8), '7-11 Prachantakham':(7.4,8.9)}




def search_nodes():
    global shortest_path
    valid_nodes = ['KMUTNB Prachinburi', 'Kabin Buri', 'Nadee', 'Ban Sang', 'Prachantakham', 'Sri Maha Phot', 'Sri Mahosot',
                   '7-11 Noen Hom','7-11 Naresuan','7-11 Phrom Yothi','7-11 Mai Khet','7-11 Mueng','7-11 Nha Mueng','7-11 Thetsaban Mueang'
                    ,'7-11 Sri Mahosot','7-11 Sri Maha Phot','7-11 Khok kwang','7-11 Nikom 304','7-11 Kabin','7-11 Nadee']
    source = source_entry.get()
    while source not in valid_nodes:
        source = input(f"{source} is not a valid node. Please try again: ")
    destination = destination_entry.get()
    while destination not in valid_nodes:
        destination = input(f"{destination} is not a valid node. Please try again: ")
    shortest_path = nx.shortest_path(G, source=source, target=destination, weight='distance')
    shortest_path_length = nx.shortest_path_length(G, source=source, target=destination, weight='distance')
    shortest_path_length = ("%.2f"%(shortest_path_length))
    path_label.config(text=f"The nearest ways from {source} to {destination}: {shortest_path}\nShortest path length: {shortest_path_length} km.")
    
    node_color_map = []
    for node in G.nodes():
        if node == shortest_path[0]:
            node_color_map.append('orange')
        elif node == shortest_path[-1]:
            node_color_map.append('orange')
        elif node in shortest_path:
            node_color_map.append('yellow')
        else:
            node_color_map.append('purple')

    plt.figure(figsize=(12,8))
    nx.draw_networkx(G, pos, with_labels=True, node_color=node_color_map, node_size=1000)
    edge_labels = nx.get_edge_attributes(G, 'distance')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    edge_list = list(zip(shortest_path, shortest_path[1:]))
    plt.title("Find 7-11 Shortest Location", size=12)
    plt.show()


root = tk.Tk()
root.title("Find 7-11 Shortest Location")

root.config(bg="pink")

canvas = tk.Canvas(root, width=800, height=400)
canvas.pack()

photo = tk.PhotoImage(file="Locationnn.png")
canvas.create_image(400, 200, image=photo)

frame = tk.Frame(root)
frame.pack(side=tk.BOTTOM)

source_label = tk.Label(frame, text="Where do you want to start: ")
source_label.grid(row=0, column=0)

source_entry = tk.Entry(frame)
source_entry.grid(row=0, column=1)

destination_label = tk.Label(frame, text="Where do you want to end: ")
destination_label.grid(row=1, column=0)

destination_entry = tk.Entry(frame)
destination_entry.grid(row=1, column=1)

button = tk.Button(frame, text="Let's go to find!", command=search_nodes)
button.grid(row=2, column=1)
button.configure(bg="pink")

path_label = tk.Label(frame, text="")
path_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
