from functs_vars import *
from csv_class import CSV
from json_class import JSON
from plotting import plot_results

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~Tk Variables~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
date_var = tk.StringVar(value = 'DD-MM-YYYY')
estrogen_var = tk.IntVar(value = 0)
testosterone_var = tk.DoubleVar(value = 0)

notes_date_var = tk.StringVar(value = 'DD-MM-YYYY')
notes_var = tk.StringVar(value = 'Note')

e_lower = tk.DoubleVar()
e_upper = tk.DoubleVar()
t_lower = tk.DoubleVar()
t_upper = tk.DoubleVar()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~Tk Functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def draw_table(mode, table):
    for i in table.get_children():
        table.delete(i) 
    if mode == "results":
        df = CSV.view_all("results")
        for i, v in df.iterrows():
            date = v['Date'].strftime(date_format)
            e_levels = v['Oestradiol']
            t_levels = v['Testosterone']
            data = (date, e_levels, t_levels)
            table.insert(parent = '', index = 0, values = data)
    elif mode == "notes":
        df = CSV.view_all("notes")
        for i, v in df.iterrows():
            date = v['Date'].strftime(date_format)
            note = v['Note']
            data = (date, note)
            table.insert(parent = '', index = 0, values = data)

def delete_items(mode, table):
    for i in table.selection():
        CSV.remove_entry(mode, table.item(i)['values'][0])
        draw_table(mode, table)
        
def view_graph():
    df = CSV.view_all("results")
    plot_results(df)
    
def handle_button_add_result(table):
    try:
        date = get_date(str(date_var.get()))
        estrogen = float(estrogen_var.get())
        testosterone = float(testosterone_var.get())
        if date == ValueError:
            print('date error!')
        else:
            CSV.add_entry("results", date, estrogen, testosterone)
            draw_table("results", table)
            date_var.set("DD-MM-YYYY")
            estrogen_var.set(0)
            testosterone_var.set(0)
    except TclError:
        print('float error!')
        
def handle_button_add_note(table):
    try:
        date = get_date(str(notes_date_var.get()))
        note = str(notes_var.get())
        if date == ValueError:
            print('date error!')
        else:
            CSV.add_entry("notes", date, note)
            draw_table("notes", table)
            notes_date_var.set("DD-MM-YYYY")
            notes_var.set("note")
    except TclError:
        print('error!')
        
def handle_button_update_levels():
    JSON.change_settings(e_lower.get(), e_upper.get(), t_lower.get(), t_upper.get())
    update_settings()
        
def update_settings():
    df = pd.read_json(path.join(wdir, JSON.file_name), typ = 'series', precise_float = True)
    e_lower.set(df['e_lower'])
    e_upper.set(df['e_upper'])
    t_lower.set(df['t_lower'])
    t_upper.set(df['t_upper'])
