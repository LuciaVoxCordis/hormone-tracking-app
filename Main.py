from functs_vars import *

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~tk init
window = tk.Tk()
window.geometry('800x600')
window.title('Hormone Tracking')

from tk_functs_vars import *

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~tabs
tabs = ttk.Notebook(window)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~Results Tab~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
tab_results = ttk.Frame(tabs)
ttk.Label(tab_results, text = 'Results').pack()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~Results Table
table_results = ttk.Treeview(tab_results, columns = ('Date', 'Estrogen Level', 'Testosterone Level'), show = 'headings')
table_results.heading('Date', text = 'Date')
table_results.heading('Estrogen Level', text = 'Estrogen Level')
table_results.heading('Testosterone Level', text = 'Testosterone Level')
table_results.pack(fill = 'both', expand = True)

frame_table_buttons = ttk.Frame(tab_results)
ttk.Button(frame_table_buttons, text = 'Delete selected item(s)', command = lambda: delete_items("results", table_results)).pack(side = 'left', padx = 5)
ttk.Button(frame_table_buttons, text = 'View results as graph', command = view_graph).pack(side = 'right', padx = 5)
frame_table_buttons.pack()

#~~~~~~~~~~~~~~~~~~~~~~~~~~Add Results Frame
frame_add_results = ttk.Frame(tab_results)
ttk.Label(frame_add_results, text = 'Add a new Result').pack()

frame_labels = ttk.Frame(frame_add_results)
ttk.Label(frame_labels, text = 'Date: (DD-MM-YYYY)').pack(side = 'left', padx = 5)
ttk.Label(frame_labels, text = 'Estrogen Level (pmol/L)').pack(side = 'left', padx = 5)
ttk.Label(frame_labels, text = 'Testosteron Level (nmol/L)').pack(side = 'left', padx = 5)
frame_labels.pack()

frame_results_entries = ttk.Frame(frame_add_results)
entry_date = ttk.Entry(frame_results_entries, textvariable = date_var)
entry_date.bind('<FocusIn>', lambda event: date_var.set(''))
entry_date.pack(side = 'left')
entry_estrogen = ttk.Entry(frame_results_entries, textvariable = estrogen_var)
entry_estrogen.bind('<FocusIn>', lambda event: estrogen_var.set(''))
entry_estrogen.pack(side = 'left')
entry_testosterone = ttk.Entry(frame_results_entries, textvariable = testosterone_var)
entry_testosterone.bind('<FocusIn>', lambda event: testosterone_var.set(''))
entry_testosterone.pack(side = 'left')
frame_results_entries.pack()

ttk.Button(frame_add_results, text = 'Add Result', command = lambda: handle_button_add_result(table_results)).pack()
frame_add_results.pack()

tab_results.pack()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Notes Tab~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
tab_notes = ttk.Frame(tabs)
ttk.Label(tab_notes, text = 'Notes').pack()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~Notes Table
table_notes = ttk.Treeview(tab_notes, columns = ('Date', 'Note'), show = 'headings')
table_notes.heading('Date', text = 'Date')
table_notes.heading('Note', text = 'Note')
table_notes.pack(fill = 'both', expand = True)

frame_table_buttons_notes = ttk.Frame(tab_notes)       
ttk.Button(frame_table_buttons_notes, text = 'Delete selected item(s)', command = lambda: delete_items("notes", table_notes)).pack(side = 'left', padx = 5)
frame_table_buttons_notes.pack()

#~~~~~~~~~~~~~~~~~~~~~~~~~~Add Notes Frame
frame_add_notes = ttk.Frame(tab_notes)
ttk.Label(frame_add_notes, text = 'Add a new Note').pack()

frame_notes_labels = ttk.Frame(frame_add_notes)
ttk.Label(frame_notes_labels, text = 'Date: (DD-MM-YYYY)').pack(side = 'left', padx = 5)
ttk.Label(frame_notes_labels, text = 'Note:').pack(side = 'left', padx = 5)
frame_notes_labels.pack()

frame_notes_entries = ttk.Frame(frame_add_notes)
entry_notes_date = ttk.Entry(frame_notes_entries, textvariable = notes_date_var)
entry_notes_date.bind('<FocusIn>', lambda event: notes_date_var.set(''))
entry_notes_date.pack(side = 'left')
entry_notes = ttk.Entry(frame_notes_entries, textvariable = notes_var)
entry_notes.bind('<FocusIn>', lambda event: notes_var.set(''))
entry_notes.pack(side = 'left')
frame_notes_entries.pack()

ttk.Button(frame_add_notes, text = 'Add Note', command = lambda: handle_button_add_note(table_notes)).pack()
frame_add_notes.pack()

tab_notes.pack()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~Settings Tab~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
tab_settings = ttk.Frame(tabs)
tk.Label(tab_settings, text = 'Settings').pack()

#~~~~~~~~~~~~~~~~~~~~~~~~~~E-levels Frame
frame_e_levels = ttk.Frame(tab_settings)
ttk.Label(frame_e_levels, text = 'Target E levels:').pack(side= 'top')

frame_e_lower = ttk.Frame(frame_e_levels)
ttk.Label(frame_e_lower, text = 'lower:').pack(side= 'top')
#ttk.Label(frame_e_lower, text = e_lower, textvariable = e_lower).pack()
spin_e_lower = ttk.Spinbox(frame_e_lower, 
                   from_ = 0, 
                   to = 2000, 
                   increment = 10, 
                   textvariable = e_lower,
                   width = 5)
spin_e_lower.bind('<<Increment>>')
spin_e_lower.bind('<<Decrement>>')
spin_e_lower.pack()
frame_e_lower.pack(side = 'left', padx = 10)

frame_e_upper = ttk.Frame(frame_e_levels)
ttk.Label(frame_e_upper, text = 'upper:').pack(side= 'top')
spin_e_upper = ttk.Spinbox(frame_e_upper, 
                   from_ = 0, 
                   to = 2000, 
                   increment = 10, 
                   textvariable = e_upper,
                   width = 5)
spin_e_upper.bind('<<Increment>>')
spin_e_upper.bind('<<Decrement>>')
spin_e_upper.pack()
frame_e_upper.pack(side = 'right', padx = 10)

frame_e_levels.pack()

#~~~~~~~~~~~~~~~~~~~~~~~~~~T-levels Frame
frame_t_levels = ttk.Frame(tab_settings)
ttk.Label(frame_t_levels, text = 'Target T levels:').pack(side= 'top')

frame_t_lower = ttk.Frame(frame_t_levels)
ttk.Label(frame_t_lower, text = 'lower:').pack(side= 'top')
spin_t_lower = ttk.Spinbox(frame_t_lower, 
                   from_ = 0, 
                   to = 100, 
                   increment = 0.1, 
                   textvariable = t_lower,
                   width = 5)
spin_t_lower.bind('<<Increment>>')
spin_t_lower.bind('<<Decrement>>')
spin_t_lower.pack()
frame_t_lower.pack(side = 'left', padx = 10)

frame_t_upper = ttk.Frame(frame_t_levels)
ttk.Label(frame_t_upper, text = 'upper:').pack(side= 'top')
spin_t_upper = ttk.Spinbox(frame_t_upper, 
                   from_ = 0, 
                   to = 100, 
                   increment = 0.1, 
                   textvariable = t_upper,
                   width = 5)
spin_t_upper.bind('<<Increment>>')
spin_t_upper.bind('<<Decrement>>')
spin_t_upper.pack()
frame_t_upper.pack(side = 'right', padx = 10)

frame_t_levels.pack()

ttk.Button(tab_settings, text = 'Save levels', command = handle_button_update_levels).pack()

tab_settings.pack()
#~~~~~~~~~~~~~~~~~~~~~~~~Adding/packing Tabs~~~~~~~~~~~~~~~~~~~~~~~~#
tabs.add(tab_results, text = 'Results')
tabs.add(tab_notes, text = 'Notes')
tabs.add(tab_settings, text = 'Settings')
tabs.pack()
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Run~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
if __name__ == "__main__":
    initialize_data_folder()
    CSV.initialize_files()
    JSON.initialize_json()
    draw_table("results", table_results)
    draw_table("notes", table_notes)
    update_settings()
    window.mainloop()