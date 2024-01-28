# # import matplotlib.pyplot as plt
#
# # C_values = [0.22, 0.21, 0.19, 0.24, 0.27, 0.30, 0.44]
# # S_values = [150, 140, 130, 160, 180, 200, 300]
#
# # plt.plot(S_values, C_values, marker='o', linestyle='-')
# # plt.xlabel("Площа пластин (S, мм^2)")
# # plt.ylabel("Електрична ємність (C, пФ)")
# # plt.title("Залежність електричної ємності від площі пластин")
# # plt.grid(True)
# # plt.show()
#
# # C_values = [1.33, 1.02, 0.83, 0.7, 0.6, 0.53, 0.47]
# # d_values = [2, 2.6, 3.2, 3.8, 4.4, 5, 5.6]
#
# # plt.plot(d_values, C_values, marker='o', linestyle='-')
# # plt.xlabel("Відстань між пластинами (d, мм)")
# # plt.ylabel("Електрична ємність (C, пФ)")
# # plt.title("Залежність електричної ємністі від відстані між пластинами")
# # plt.grid(True)
# # plt.show()
#
# # C_values = [0.47, 0.47, 0.47, 0.47, 0.47, 0.47, 0.47]
# # U_values = [1.5, 1.2, 1.05, 0.7, 0.4, 0, -0.4]
#
# # plt.plot(U_values, C_values, marker='o', linestyle='-')
# # plt.xlabel("Напруга на пластинах (U, В)")
# # plt.ylabel("Електрична ємність (C, пФ)")
# # plt.title("Залежність електричної ємності від напруги на пластинах")
# # plt.grid(True)
# # plt.show()
#
# # import matplotlib.pyplot as plt
#
# #T1 = 0
# #T2 = 537
# #R1 = 0.002
# #R2 = 0.006
#
# #temperatures = [T1, T2]
# #resistances = [R1, R2]
#
# #plt.plot(temperatures, resistances, marker='o', linestyle='-')
# #plt.title('Залежність опору від температури')
# #plt.xlabel('Температура (°C)')
# #plt.ylabel('Опір (R)')
# #plt.grid(True)
#
# #plt.show()
# import matplotlib.pyplot as plt
#
# # Дані з вашої таблиці
# R = [0, 5, 7.5, 10, 25]
# Ur = [34.85, 23.65, 20, 17.5, None]  # None для невідомого значення
# U = [0, 11.65, 15, 17.50, None]     # None для невідомого значення
# KKD = [0, 33, 42.86, 50, None]     # None для невідомого значення
#
# # Побудова графіка втрат напруги в джерелі (Ur) від опору зовнішнього кола (R)
# plt.figure(figsize=(10, 4))
# plt.subplot(1, 3, 1)
# plt.plot(R, Ur, marker='o')
# plt.title('Втрати напруги в джерелі (Ur)')
# plt.xlabel('Опір зовнішнього кола (R), Ом')
# plt.ylabel('Ur, В')
#
# # Побудова графіка напруги на клемах джерела (U) від опору зовнішнього кола (R)
# plt.subplot(1, 3, 2)
# plt.plot(R, U, marker='o')
# plt.title('Напруга на клемах джерела (U)')
# plt.xlabel('Опір зовнішнього кола (R), Ом')
# plt.ylabel('U, В')
#
# # Побудова графіка KKD джерела живлення (%) від опору зовнішнього кола (R)
# plt.subplot(1, 3, 3)
# plt.plot(R, KKD, marker='o')
# plt.title('KKD джерела живлення (%)')
# plt.xlabel('Опір зовнішнього кола (R), Ом')
# plt.ylabel('KKD, %')
#
# plt.tight_layout()
# plt.show()
# import networkx as nx
# import matplotlib.pyplot as plt
# import numpy as np
# adjacency_matrix = np.array([
#     [0, 1, 1, 0],
#     [1, 0, 1, 1],
#     [1, 1, 0, 1],
#     [0, 1, 1, 0]
# ])
# G = nx.from_numpy_array(adjacency_matrix)
# pos = nx.spring_layout(G, seed=42)
# nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=10, edge_color='gray', linewidths=1, alpha=0.7)
# plt.show()

# import networkx as nx
# import matplotlib.pyplot as plt
# edges = {0: [2, 3], 1: [0, 2, 4, 5, 7], 2: [3, 4, 7, 8], 3: [0, 2], 4: [1, 2, 6], 5: [1, 6, 7], 6: [4, 5, 7], 7: [1, 2, 5, 6], 8: [2]}
# G = nx.Graph(edges)
# pos = nx.spring_layout(G, seed=42)
# nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=10, edge_color='gray', linewidths=1, alpha=0.7)
# plt.savefig('graph.png')
# plt.show()


# import networkx as nx
# import matplotlib.pyplot as plt
#
# edges = {
#     1: [(2, 5), (3, 8), (6, 2)],
#     2: [(1, 5), (3, 5), (5, 3)],
#     3: [(1, 8), (2, 5), (4, 2)],
#     4: [(3, 2), (5, 3)],
#     5: [(2, 3), (4, 3), (6, 4)],
#     6: [(1, 2), (5, 4)]
# }
#
# G = nx.Graph()
#
# for node, edge_list in edges.items():
#     G.add_node(node)
#     for edge in edge_list:
#         neighbor, weight = edge
#         G.add_edge(node, neighbor, weight=weight)
#
# pos = nx.spring_layout(G, seed=42)
#
# nx.draw(
#     G,
#     pos,
#     with_labels=True,
#     font_weight='bold',
#     node_size=700,
#     node_color='skyblue',
#     font_color='black',
#     font_size=10,
#     edge_color='gray',
#     width=[d['weight'] for (u, v, d) in G.edges(data=True)],
#     alpha=0.7
# )
#
# plt.savefig('graph.png')
# plt.show()

# import requests
# from datetime import datetime, timedelta
#
# def get_wind_forecast(api_key, city_name):
#     base_url = "http://api.openweathermap.org/data/2.5/forecast"
#     params = {
#         'q': city_name,
#         'appid': api_key,
#     }
#
#     response = requests.get(base_url, params=params)
#     data = response.json()
#
#     if response.status_code == 200:
#         forecasts = data.get('list', [])
#         for forecast in forecasts:
#             timestamp = forecast.get('dt', 0)
#             wind_info = forecast.get('wind', {})
#             wind_speed = wind_info.get('speed', 0)
#             wind_deg = wind_info.get('deg', 0)
#
#             date = datetime.utcfromtimestamp(timestamp)
#             print(f"{date}: Wind Speed - {wind_speed}, Wind Direction - {wind_deg} degrees")
#     else:
#         print(f"Error: {data.get('message', 'Unknown error')}")
#
# if __name__ == "__main__":
#     # Вам потрібно замінити 'YOUR_API_KEY' на реальний ключ API OpenWeatherMap
#     api_key = '32e5b9ce34293b090423b772d5bb283f'
#     city_name = 'Krivoy Rog'
#
#     get_wind_forecast(api_key, city_name)



#Рооооооооооооооооооооооооооооооза віііііііііііііііііііііііііііііііііітрів

import matplotlib.pyplot as plt
import numpy as np
wind_directions = ["Пн", "Пн.-Сх", "Сх", "Пд.-Сх", "Пд", "Пд.-Зх", "Зх", "Пн.-Зх"]
wind_days = [3, 7, 3, 4, 6, 3, 2, 3]
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
theta = np.linspace(0, 2*np.pi, len(wind_directions), endpoint=False)
bars = ax.bar(theta, wind_days, align="center", alpha=0.7)
for bar, color in zip(bars, plt.cm.viridis(np.linspace(0, 1, len(wind_directions)))):
    bar.set_facecolor(color)
    bar.set_edgecolor('gray')
ax.set_thetagrids(np.degrees(theta), wind_directions)
plt.title("Роза вітрів", va='bottom')
plt.show()

