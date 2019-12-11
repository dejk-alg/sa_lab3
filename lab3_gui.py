from lab3_backend import *

import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk

class LabGUI(tk.Frame):
    
    def __init__(self, parent):
        
        tk.Frame.__init__(self, parent)
        self.parent = parent
        
        parent.geometry('1450x700+50+50')
        parent.title('approximation')
                        
        self.init_input_filename()
        self.init_label_filename()
        
        self.init_x_leng()
        
        self.init_choose_polynomial()
        self.init_create_pads()
        
        self.init_polynomial_degrees()
        self.init_function_weight()
        
        self.init_y_coord()
        
        self.init_run_button()
        self.init_default_checkbutton()
        self.init_y_checkbutton()
        
        self.init_mult()

        self.init_all_labels()
        self.init_output_label()
        self.init_graph_canvas()
        
        self.first_run = True
        
    def init_label(self, text, column, row, columnspan=1, rowspan=1, height=1):
        
        label = tk.Label(self.parent, text=text, height=height)
        label.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan)
        
        
    def init_variable_label(self, variable, column, row, columnspan=1, rowspan=1):
        
        label = tk.Label(self.parent, textvariable=variable)
        label.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan)
        
        
    def init_entry(self, variable, text, column, row, columnspan=1, rowspan=1, width=4):
        
        entry = tk.Entry(
            self.parent, text=text,
            textvariable=variable, width=width)    
        
        entry.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=tk.W)
    
    
    def init_label_with_entry(self, text, column, row, variable, columnspan=1, rowspan=1, entry_width=4):
        
        self.init_label(text=text, column=column, row=row)       
        self.init_entry(text=text, column=column+1, row=row, variable=variable, width=entry_width)
 

    def init_radiobutton(self, text, column, row, variable, value, columnspan=1):
        
        rdbutton = tk.Radiobutton(self.parent, text=text, value=value, variable=variable)
        rdbutton.grid(row=row, column=column, columnspan=columnspan, sticky=tk.W)
        
        
    def init_pads(self, row=1, column=1, width=0, height=0):
        
        label = tk.Frame(self.parent, width=width, height=height)
        label.grid(column=column, row=row)
    
    
    def init_button(self, text, column, row, width, height, columnspan=1, rowspan=1, command=None):
        butt = tk.Button(self.parent, text=text, width=width, height=height, command=command)
        butt.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan)
        
        
    def init_checkbutton(self, text, column, row, columnspan=1, rowspan=1, variable=None):
        butt = tk.Checkbutton(self.parent, text=text, variable=variable)
        butt.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan)
    
    #Buttons
    
    def init_run_button(self):
        self.init_button(
            text = 'Розрахувати', width=10, height=1, 
            column=11, row=6, rowspan=2, columnspan=2,
            command=self.run
        )
    
    
    def init_default_checkbutton(self):
        self.default_data = tk.BooleanVar(value=True)
        
        self.init_checkbutton(
            text = 'Стандартні значення', 
            column=1, row=4,
            variable=self.default_data
        )
        
    def init_y_checkbutton(self):
        
        self.normalize_y = tk.BooleanVar(value=True)
        
        self.init_checkbutton(
            text = 'Нормалізувати y на графіку', 
            column=11, row=5,
            variable=self.normalize_y
        )
    
    # Labels
    
    def init_create_pads(self):
        
        self.init_pads(column=2, width=35)
        self.init_pads(column=5, width=35)
        self.init_pads(column=7, width=20)
        self.init_pads(column=10, width=35)
        self.init_pads(row=7, height=30)
        self.init_pads(row=9, height=8)
    
    def init_all_labels(self):
        
        self.init_label(text = 'Ваги цільових функцій', column=11, row=0, columnspan=1, rowspan=2)
        
        self.init_label(text = 'Вибірка', column=0, row=0,columnspan=2, rowspan=2)
        self.init_label(text = 'Вектори', column=3, row = 0, columnspan=2, rowspan=2)
        self.init_label(text = 'Поліноми', column=6, row=0, columnspan=4, height=2)
        self.init_label(text = 'Вид', column=6, row=1)
        self.init_label(text = 'Степінь', column=8, row=1)
        
        self.init_label(text = 'Результат', column=0, row=8, columnspan=6)
        self.init_label(text = 'Графік', column=7, row=8, columnspan=6)  
        
        self.err_output = tk.StringVar(value='Значення похибки')
        self.init_variable_label(variable=self.err_output, column=8, row=11, columnspan=6)
        
    
    def init_output_label(self):
        
        self.scrolled_text = ScrolledText(
            master=self.parent, wrap='word', width=80, height=24, font=('TkDefaultFont', 11))
        
        self.scrolled_text.grid(column=0, row=10, columnspan=7)
        self.set_output_text('Натисніть на кнопку "Розрахувати"')
        self.scrolled_text.config(state=tk.DISABLED)
    
    
    def init_graph_canvas(self):
        self.canvas_size = (700, 420)
        self.graph_canvas = tk.Canvas(self.parent, bg="#fff", height=self.canvas_size[1], width=self.canvas_size[0])
        self.graph_canvas.grid(column=8, row=10, columnspan=6, sticky=tk.NW)
    
    # RadioButtons   
    
    def init_choose_polynomial(self):
        self.polynomial_type = tk.StringVar(value='chebyshev_first')
        self.init_radiobutton(text = 'Чебишева 1-го порядку', row=2, column=6, value='chebyshev_first', variable=self.polynomial_type)
        self.init_radiobutton(text = 'Чебишева 2-го порядку', row=3, column=6, value='chebyshev_second', variable=self.polynomial_type)
        self.init_radiobutton(text = 'Лежандра', row=4, column=6, value='legendre', variable=self.polynomial_type)
        self.init_radiobutton(text = 'Лагерра', row=5, column=6, value='laguerre', variable=self.polynomial_type)
        self.init_radiobutton(text = 'Ерміта', row=6, column=6, value='hermite', variable=self.polynomial_type)
         
    def init_function_weight(self):
        self.weight_average = tk.BooleanVar()
        
        self.init_radiobutton(
            text = 'Через максимум  і мінімум', row=2, column=11, columnspan=2, 
            value=False, variable=self.weight_average)
        
        self.init_radiobutton(
            text = 'Середнє арифметичне', row=3, column=11, columnspan=2,
            value=True, variable=self.weight_average)        
        
    # Labels with entries
    
    def init_samples_length(self):
        
        self.samples_length = tk.IntVar()
        self.init_label_with_entry(
            text='Розмір вибірки', column=0, row=2,
            variable=self.samples_length)
        
    def init_input_filename(self):
        self.input_filename = tk.StringVar(value='features.txt')
        self.init_label_with_entry(
            text='Файл зі значеннями x', column=0, row=2,
            variable=self.input_filename, entry_width=15)
        
    def init_label_filename(self):
        self.label_filename = tk.StringVar(value='labels.txt')
        self.init_label_with_entry(
            text='Файл зі значеннями y', column=0, row=3,
            variable=self.label_filename, entry_width=15) 
    
    def init_x_leng(self):
        self.x_leng_var = [tk.IntVar(value=def_value) for def_value in (3, 2, 2)]
        
        for ind, var in enumerate(self.x_leng_var):  
            self.init_label_with_entry(
                text='Розмірність x' + str(ind+1), column=3, row=ind+2,
                variable=var)
    
    def init_polynomial_degrees(self):
        self.polynomial_degrees = [tk.IntVar(value=3) for _ in range(3)]
        
        for ind, var in enumerate(self.polynomial_degrees):  
            self.init_label_with_entry(
                text='Степінь x' + str(ind+1), column=8, row=ind+2,
                variable=var)
    
    def init_y_coord(self):
        self.y_coord = tk.IntVar(value=1)
        self.init_label_with_entry(
            text='Координата y', column=11, row=4,
            variable=self.y_coord)
        
    def init_mult(self):
        self.init_label(text = 'Модель', column=1, row=5, columnspan=3)
        
        self.mult = tk.BooleanVar(value=True)
        
        self.init_radiobutton(
            text = 'Адитивна', row=6, column=1, columnspan=2, 
            value=False, variable=self.mult)
        
        self.init_radiobutton(
            text = 'Мультиплікативна', row=6, column=2, columnspan=2,
            value=True, variable=self.mult) 
        
        self.both_graphs = tk.BooleanVar(value=True)
        
        self.init_checkbutton(
            text = 'Відобразити обидва графіки', 
            column=1, row=7, columnspan=4,
            variable=self.both_graphs
        )
    
    
    def set_output_text(self, output):
        
        self.scrolled_text.config(state=tk.NORMAL)
        self.scrolled_text.delete(1.0, tk.END)
        self.scrolled_text.insert(1.0, output)
        self.scrolled_text.config(state=tk.DISABLED)
    
    
    def update_graph(self):
        
        self.graph_image = ImageTk.PhotoImage(
            Image.open('graph.png').resize(self.canvas_size, Image.ANTIALIAS))
        
        if self.first_run:
            self.canvas_image = self.graph_canvas.create_image(
                0, 0, image=self.graph_image,  anchor='nw')
        else:
            self.graph_canvas.itemconfigure(self.canvas_image, image=self.graph_image)
    
    
    def add_output(self, inp='', new_line=True):
        self.output += str(inp)
        if new_line: self.output += '\n'
                                           
    
    def run(self):
        
        self.output = ''
        
        self.polynomial_var = {
            'chebyshev_first': 'T',
            'chebyshev_second': 'U',
            'legendre': 'P',
            'hermite': 'H',
            'laguerre': 'L'
        }.get(self.polynomial_type.get())
        
        feature_lengths = ()
        
        if self.default_data.get(): 
            data = default_input()
            feature_lengths = (3, 2, 2)
        else: 
            data = read_input_from_file(self.input_filename.get(), self.label_filename.get())
            feature_lengths = [length.get() for length in self.x_leng_var]
        
        feature_ranges = get_ranges(feature_lengths)
        feature_amount = len(feature_lengths)
        
        polynomial_degree_values = np.array([polynomial_degree.get() for polynomial_degree in self.polynomial_degrees])
        
        mult = self.mult.get()
        both_graphs = self.both_graphs.get()
        polynomial_type = self.polynomial_type.get()
                
        x, y = data
                
        y_variable = y[:, self.y_coord.get() - 1]
        
        x = normalize_data(x)

        y_variable, norm_values = normalize_data(y_variable, min_max_data = True)
                
        b = None
        
        if self.weight_average: b = y.mean(axis=1)
        else: b = (y.min(axis=1) + y.max(axis=1)) / 2
            
        b = normalize_data(b)
        
        A_full = create_equation_matrix_simult(
            x, polynomial_type=polynomial_type, 
            polynomial_degrees=polynomial_degree_values,
            feature_lengths=feature_lengths)
        
        A_full = normalize_data(A_full)
        lambda_matrix_full = solve(A_full, b, mult=mult)
            
        err = np.max(np.abs(forward(A_full, lambda_matrix_full, mult=mult) - b))
        
        while err > 0.1:
            
            change = False
            
            for i in range(3):
                
                new_polynomial_degree_values = polynomial_degree_values.copy()
                new_polynomial_degree_values[i] += 1
                
                A_full = create_equation_matrix_simult(
                    x, polynomial_type=polynomial_type, 
                    polynomial_degrees=new_polynomial_degree_values,
                    feature_lengths=feature_lengths)

                A_full = normalize_data(A_full)
                lambda_matrix_full = solve(A_full, b, mult=mult)

                err_new = np.max(np.abs(forward(A_full, lambda_matrix_full, mult=mult) - b))
                
                if (err - err_new) / err > 0.05:
                    polynomial_degree_values = new_polynomial_degree_values
                    err = err_new
                    change = True
                    
            if not change: break
            
            
        for polynomial_degree, value in zip(self.polynomial_degrees, polynomial_degree_values):
            polynomial_degree.set(value)
                                        
                
        A_full = create_equation_matrix_simult(
            x, polynomial_type=polynomial_type, 
            polynomial_degrees=polynomial_degree_values,
            feature_lengths=feature_lengths)
        
        A_full = normalize_data(A_full)
        lambda_matrix_full = solve(A_full, b, mult=mult)
        
        new_output = print_equation_3(
            coeff_matrix=lambda_matrix_full, lengths=feature_lengths, degrees=polynomial_degree_values, 
            coeff_name='λ', function_name='ψ', var_name=self.polynomial_var, mult=mult)
        
        self.add_output(new_output)

        phi_values_full = []
        row_ind = 0
        
        for feature_ind, (feature_length, polynomial_degree) in enumerate(zip(feature_lengths, polynomial_degree_values)):
            phi_values = []
            
            for variable_ind in range(feature_length):
                A_part = A_full[:, row_ind: row_ind + polynomial_degree]
                lambda_part = lambda_matrix_full[row_ind: row_ind + polynomial_degree]
                row_ind = row_ind + polynomial_degree
                phi_values.append(forward(A_part, lambda_part, mult=mult))
                
            phi_values = normalize_data(np.array(phi_values).T)
            phi_values_full.append(phi_values)
        
        a_matrixes = [solve(phi_values, y_variable, mult=mult) for phi_values in phi_values_full]
            
        new_output = print_equation_2(coeff_matrixes=a_matrixes, target_ind=self.y_coord.get(), mult=mult)
        self.add_output(new_output)
        
        new_output = output_diff(A=phi_values_full, b=y_variable, coeff=a_matrixes, mult=mult, on_array=True)
        self.add_output(new_output)
        
        F_values = np.array([forward(a_matrix, phi_values, mult=mult) for phi_values, a_matrix in zip(phi_values_full, a_matrixes)]).T
        F_values = normalize_data(F_values)
        c_matrix = solve(F_values, y_variable, mult=mult)
        
        new_output = print_equation_1(coeff_matrix=c_matrix, target_ind=self.y_coord.get(), mult=mult)
        self.add_output(new_output)
        
        new_output = output_diff(A=F_values, b=y_variable, coeff=c_matrix, mult=mult)
        self.add_output(new_output)
        
        #approx_values = F_values @ c_matrix.T
        
        lambda_matrix_y = solve(A_full, y_variable, mult=mult)
        approx_values = forward(A_full, lambda_matrix_y, mult=mult)
                
        if both_graphs:
                        
            lambda_matrix_y_mult = solve(A_full, y_variable, mult=not mult)
            approx_values_mult = forward(A_full, lambda_matrix_y_mult, mult=not mult)
            
            if not self.normalize_y.get():
                y_variable = denormalize_data(y_variable, norm_values)
                approx_values = denormalize_data(approx_values, norm_values)
                approx_values_mult = denormalize_data(approx_values_mult, norm_values)
      
            if mult:
                save_graph_mult(y_variable, approx_values_mult, approx_values) 
            else:
                save_graph_mult(y_variable, approx_values, approx_values_mult) 
        
        else:       
            if not self.normalize_y.get():
                y_variable = denormalize_data(y_variable, norm_values)
                approx_values = denormalize_data(approx_values, norm_values)
            save_graph(y_variable, approx_values) 
        
        self.update_graph()
        
        err_value = np.max(np.abs(y_variable - approx_values))
        self.err_output.set('Значення похибки: {0:.5}'.format(err_value))
                
        self.set_output_text(self.output)
        
        if self.first_run: self.first_run = False