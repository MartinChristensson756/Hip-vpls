import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('iperf_results.csv')

df.columns = df.columns.str.strip()


fig, ax = plt.subplots(figsize=(12, 9)) 

ax.set_facecolor('whitesmoke')  
buffer_lengths = df['BufferLength'].unique()

colors = plt.cm.viridis(np.linspace(0, 1, len(buffer_lengths)))

tcp_window_sizes = sorted(df['TCPWindowSize'].unique())
tcp_window_size_labels = [str(size) for size in tcp_window_sizes] 

for i, buffer_length in enumerate(sorted(buffer_lengths)):
    subset = df[df['BufferLength'] == buffer_length].sort_values(by='TCPWindowSize')
    
    x = [str(item) for item in subset['TCPWindowSize']] 
    color = colors[i]
    
    ax.plot(x, y, label=f'BufferLength:{buffer_length} bytes', linestyle='-', marker='o', color=color)
ax.set_xlabel('TCP Window Size (bytes)', labelpad=20, fontsize=12)
ax.set_ylabel('Throughput (Mbits/sec)', labelpad=20, fontsize=12)
ax.set_title('Throughput vs. TCP Window Size by Buffer Length', pad=20, fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=10)

ax.legend(loc='upper left', fontsize='10', framealpha=0.7, bbox_to_anchor=(1.02, 1))

ax.set_xticks(range(len(tcp_window_size_labels))) 
ax.set_xticklabels(tcp_window_size_labels, rotation=45, ha='right') 
plt.tight_layout(pad=1.0) 

plt.show()