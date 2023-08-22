import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from data import sales_data,inventory_data,product_data,sales_year_data,inventory_month_data

plt.rcParams['axes.prop_cycle'] = plt.cycler(
    color=["#4C2A85", "#BE96FF", "#957DAD", "#5E366E", "#A98CCC"])

fig1, ax1 = plt.subplots()
ax1.bar(sales_data.keys(),sales_data.values())
ax1.set_title("Sales by Product")
ax1.set_xlabel("Product")
ax1.set_ylabel("Sales")
#plt.show()

fig2,ax2 = plt.subplots()
ax2.barh(list(inventory_data.keys()),inventory_data.values())
ax2.set_title("Inventory by Product")
ax2.set_xlabel("Inventory")
ax2.set_ylabel("Product")
#plt.show()

fig3,ax3 = plt.subplots()
ax3.pie(product_data.values(),labels=product_data.keys())
ax3.set_title("Product Breakdown")
#plt.show()

fig4,ax4 = plt.subplots()
ax4.plot(list(sales_year_data.keys()),list(sales_year_data.values()))
ax4.set_title("Sales by Year")
ax4.set_xlabel("Year")
ax4.set_ylabel("Sales")
#plt.show()

fig5,ax5 = plt.subplots()
ax5.fill_between(inventory_month_data.keys(),inventory_month_data.values())
ax5.set_title("Inventory by Month")
ax5.set_xlabel("Month")
ax5.set_ylabel("Inventory")
#plt.show()

root = tk.Tk()
root.title("Dashboard")
root.state("zoomed")

upper_frame = tk.Frame(root)
upper_frame.pack(fill='both',expand=True)

canvas1 = FigureCanvasTkAgg(fig1,upper_frame)
canvas1.draw()
canvas1.get_tk_widget().pack(side='left',fill='both',expand=True)

canvas2 = FigureCanvasTkAgg(fig2,upper_frame)
canvas2.draw()
canvas2.get_tk_widget().pack(side='left',fill='both',expand=True)

canvas3 = FigureCanvasTkAgg(fig3,upper_frame)
canvas3.draw()
canvas3.get_tk_widget().pack(side='left',fill='both',expand=True)

lower_frame = tk.Frame(root)
lower_frame.pack(fill='both',expand=True)

canvas4 = FigureCanvasTkAgg(fig4,lower_frame)
canvas4.draw()
canvas4.get_tk_widget().pack(side='left',fill='both',expand=True)

canvas5 = FigureCanvasTkAgg(fig5,lower_frame)
canvas5.draw()
canvas5.get_tk_widget().pack(side='left',fill='both',expand=True)


root.mainloop()