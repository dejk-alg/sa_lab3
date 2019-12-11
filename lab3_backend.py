import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=5)


def solve(A, y, mult=False):
    
    if mult:
        max_log = 3
        y = np.log(1 + (max_log - 1) * y)
        A = np.log((1 + max_log) / 2 + (max_log - 1) * A / 2)
        
    return np.linalg.lstsq(A, y)[0]


def forward(A, coeff, mult=False):
    
    if mult:
        max_log = 3
        A_log = np.log((1 + max_log) / 2 + (max_log - 1) * A / 2)
        y_log = A_log @ coeff.T
        y = (np.exp(y_log) - 1) / (max_log - 1)
        return y
        
    else:
        return A @ coeff.T

def get_subscript(symbol):
    if symbol == 'i': return u'\u1d62'
    return chr(ord(u'\u2080') + symbol)


def read_input_from_file(features_filename, labels_filename, rows_limit=50):
    
    x = np.loadtxt(features_filename)
    y = np.squeeze(np.loadtxt(labels_filename))
        
    if y.ndim == 1:
        y = y.reshape((-1, 1))
    
    if x.shape[0] > rows_limit:
        x = x[:rows_limit]
        y = y[:rows_limit]
        
    return x, y 


def default_input():
    x = np.array(
        [[2.050,22.015,1.050,4.015,5.000,1.000,8.100],
        [5.150,16.100,1.150,9.109,15.800,2.100,4.200],
        [8.200,10.125,1.192,14.125,22.500,2.500,3.500],
        [11.250,4.175,1.250,19.175,28.700,3.510,2.720],
        [14.325,1.200,4.325,24.198,34.500,4.200,2.530],
        [17.350,0.250,8.350,29.251,39.000,5.020,2.100],
        [20.490,5.400,12.411,34.495,46.700,8.200,1.150],
        [23.698,10.500,16.505,28.498,53.800,10.100,0.720],
        [26.900,15.700,20.610,22.598,65.000,12.800,0.540],
        [29.450,20.700,24.695,16.699,82.000,14.400,0.150],
        [32.750,25.750,21.750,9.748,95.400,16.700,0.550],
        [28.800,30.775,18.804,4.775,102.800,18.500,1.760],
        [24.950,35.800,15.850,2.798,117.000,21.300,2.230],
        [20.840,40.850,12.050,7.850,129.780,25.700,4.610],
        [16.910,34.855,9.910,13.855,99.000,29.900,6.160],
        [10.925,22.865,5.925,19.865,85.500,32.500,8.250],
        [4.929,16.885,1.011,25.875,71.900,28.700,12.370],
        [2.933,4.915,5.933,31.899,57.500,24.200,14.260],
        [1.935,8.950,10.935,37.951,43.580,19.100,16.510],
        [3.950,16.975,16.950,42.975,29.400,19.700,19.740],
        [9.810,20.995,22.950,35.015,15.500,21.000,15.140],
        [12.750,24.975,28.108,27.975,12.500,23.560,13.350],
        [15.150,28.950,34.251,19.950,9.800,25.300,8.580],
        [18.200,32.900,38.204,12.915,6.500,28.700,6.740],
        [21.450,36.875,34.248,6.875,4.400,31.560,4.850],
        [24.325,40.865,28.325,1.865,2.500,37.100,6.210],
        [27.350,46.855,23.351,5.855,1.300,34.700,9.520],
        [30.400,52.850,18.408,9.850,4.700,26.200,10.750],
        [34.500,47.775,13.495,14.775,11.200,23.700,12.950],
        [29.600,42.750,8.607,19.750,14.700,20.360,8.100],
        [24.700,37.710,3.697,25.697,17.800,17.700,4.150],
        [19.750,32.603,1.750,31.605,20.100,13.340,2.360],
        [14.800,27.495,2.798,37.495,40.520,11.720,1.350],
        [9.850,22.394,5.850,44.415,65.200,9.900,2.130],
        [4.907,17.245,8.913,36.255,80.760,7.740,4.570],
        [1.910,12.192,12.910,28.205,91.100,6.360,6.750],
        [6.925,7.175,17.925,19.175,109.500,5.700,9.260],
        [12.929,2.125,22.929,9.125,122.900,4.750,11.790],
        [18.010,1.105,27.933,3.091,128.300,3.650,13.120],
        [24.935,3.010,21.935,1.985,94.500,3.520,15.360],
        [19.950,13.110,15.950,4.115,57.600,2.720,12.850],
        [14.020,18.115,3.995,9.115,35.800,2.340,10.340],
        [9.050,12.128,9.950,15.120,15.260,2.160,12.680],
        [4.935,6.131,17.935,22.130,9.520,1.760,14.320],
        [1.925,2.135,25.925,29.135,4.800,1.480,16.160]])

    y = np.array(
        [[154.621,158.145,219.406,227.683],
        [398.163,173.368,192.651,190.123],
        [587.411,271.084,187.691,183.576],
        [767.197,383.567,78.793,174.789],
        [966.547,493.813,79.497,154.316],
        [1153.789,601.378,177.082,132.817],
        [1210.926,855.579,267.758,257.425],
        [1851.381,960.432,371.956,289.519],
        [1987.364,1176.283,491.123,321.374],
        [2536.123,1293.657,512.859,549.173],
        [2292.341,1578.624,653.717,784.136],
        [1988.324,2354.324,717.965,879.152],
        [1326.939,3478.926,955.912,901.239],
        [857.128,4588.675,1169.359,1225.482],
        [605.327,5499.367,1292.924,1340.976],
        [458.386,6468.567,1318.549,1875.846],
        [218.859,7353.932,1257.354,1916.124],
        [195.737,9335.124,984.167,863.928],
        [106.168,11261.946,716.375,703.153],
        [185.761,12151.387,541.326,631.195],
        [790.639,13910.519,475.651,571.588],
        [1323.784,15485.142,244.856,436.847],
        [1831.438,17688.125,448.314,341.842],
        [2321.321,19883.435,644.716,239.425],
        [2891.845,14972.834,829.942,122.147],
        [3308.614,9080.562,949.316,95.954],
        [3529.956,7887.987,1148.231,150.492],
        [4730.129,5688.951,1347.987,254.897],
        [5917.152,3455.494,1542.967,458.289],
        [8678.654,1211.209,1732.856,672.164],
        [9212.145,996.197,1915.632,853.356],
        [12886.243,677.325,1493.135,427.168],
        [12362.345,364.615,1177.824,206.123],
        [10632.879,152.534,963.453,182.659],
        [9267.156,45.178,779.167,93.834],
        [7070.531,36.176,580.836,71.345],
        [4984.243,20.364,287.192,66.841],
        [2881.956,10.428,185.834,93.952],
        [1616.829,8.475,301.985,109.463],
        [973.329,16.924,528.591,233.415],
        [449.421,54.183,602.861,308.613],
        [225.356,96.324,705.817,407.319],
        [176.578,176.457,978.473,282.263],
        [170.948,195.814,1081.417,184.132],
        [168.334,204.549,1178.653,61.953]])
    return x, y


def normalize_data(x, min_max_data=False):
    min_values = np.min(x, axis=0)
    max_values = np.max(x, axis=0)
    
    divide = np.array(max_values - min_values)
    divide[divide < 1e-5] = 1
    
    x = (x - min_values) / divide
    if min_max_data:
        return x, (min_values, max_values)
    return x


def transform_data(x, min_values, max_values):
    divide = np.array(max_values - min_values)
    divide[divide < 1e-5] = 1
    
    x = (x - min_values) / divide
    return x


def denormalize_data(x, norm_values):
    min_values, max_values = norm_values
    x = x * (max_values - min_values) + min_values
    return x


def polynomial(polynomial_type):
    
    def сhebyshev_first(n, x): 
        return np.cos(n * np.arccos(x))
    
    def chebyshev_second(n, x):
        
        if x == 1:
            if n == 0: return 1
            if n == 1: return 2
            if n == 2: return 3
        
        acos = np.arccos(x)
        return np.sin((n + 1) * acos) / acos
    
    def legendre(n, x):
        
        if n == 0:
            return 0.5
        if n == 1:
            return x
        
        return (2 * n + 1) / (n + 1) * x * legendre(n - 1, x) - n / (n + 1) * legendre(n - 2, x)
        
    def hermite(n, x):
        
        if n == 0:
            return 1
        if n == 1:
            return x
            
        return x * hermite(n - 1, x) -(n - 1) * hermite(n - 2, x)
    
    def laguerre(n, x):
        
        if n == 0:
            return 0.5
        if n == 1:
            return - x + 1
    
        return ((2 * n - x - 1) * laguerre(n - 1, x) - (n - 1) * laguerre(n - 2, x)) / n
    
    # return function with name corresponding to polynome_type variable, 
    # second parameter is a default value
    return locals().get(polynomial_type, сhebyshev_first)


def get_ranges(lengths):
    
    ranges = []
    ind = 0
    for length in lengths:
        ranges.append((ind, ind + length))
        ind += length
        
    return ranges


def create_equation_matrix_simult(x, polynomial_type='сhebyshev_first', polynomial_degrees=(2, 2, 2), feature_lengths = (2, 2, 3)):
    
    feature_ranges = get_ranges(feature_lengths)
    
    polynomial_fuction = polynomial(polynomial_type)
    
    variables_amount = sum(length * degree for length, degree in zip(feature_lengths, polynomial_degrees))
    A = np.empty((x.shape[0], variables_amount), dtype=np.float32)
    
    for row_ind in range(x.shape[0]):
        
        row = []
        
        for feature_range, feature_degree in zip(feature_ranges, polynomial_degrees):
            for feature_ind in range(feature_range[0], feature_range[1]):
                for degree_ind in range(feature_degree):
                    degree_ind += 1
                    row.append(polynomial_fuction(degree_ind, 2 * x[row_ind, feature_ind] - 1))
        
        A[row_ind] = row
        
    return A


def create_equation_matrix(x, polynomial_type='сhebyshev_first', polynomial_degree=2):
    
    polynomial_function = polynomial(polynomial_type)
    
    variables_amount = x.shape[1] * polynomial_degree
    
    A = np.empty((x.shape[0], variables_amount), dtype=np.float32)
    
    for row_ind in range(x.shape[0]):
                
        for variable_ind in range(x.shape[1]):
            variable_value = 2 * x[row_ind, variable_ind] - 1
            for degree_ind in range(polynomial_degree):
                degree_ind += 1
                A[row_ind, polynomial_degree * variable_ind + degree_ind] = polynomial_function(degree_ind, variable_value)
                
    return A

def save_graph(y, approx, filename='graph.png'):
    
    plt.figure(figsize=(20,10))
    n = np.arange(len(y))
    plt.plot(n, approx, 'r', n, y, 'b')
    plt.legend(['наближення', 'цільова функція'])
    plt.savefig('graph.png', bbox_inches = 'tight')

    
def save_graph_mult(y, approx, approx_mult, filename='graph.png'):
    
    plt.figure(figsize=(20,10))
    n = np.arange(len(y))
    plt.plot(n, approx, 'r', n, approx_mult, 'g', n, y, 'b')
    plt.legend(['адитивне наближення', 'мультиплікативне наближення', 'цільова функція'])
    plt.savefig('graph.png', bbox_inches = 'tight')
    
    
def print_equation_3(coeff_matrix, lengths, degrees, coeff_name='λ', function_name='ψ', var_name='T', mult=False):
    
    if mult:
        return print_equation_3_mult(
            coeff_matrix=coeff_matrix, lengths=lengths, degrees=degrees, 
            coeff_name=coeff_name, function_name=function_name, var_name=var_name)
    
    output = ''
        
    output += 'Третій ієрархічний рівень\n'
    output += 'Формування функцій ψ\n'
        
    ind = 0
                
    for eq_ind, (length, degree_range) in enumerate(zip(lengths, degrees)):
            
        output += '\nМатриця коефіціентів {0}{1}\n'.format(coeff_name, get_subscript(eq_ind + 1))
            
        coeff_matrix_part = coeff_matrix[ind: ind + length * degree_range].reshape(length, degree_range)
        output += str(coeff_matrix_part)
        output += '\n'
        ind += length * degree_range
        
    ind = 0
    for eq_ind, (length, degree_range) in enumerate(zip(lengths, degrees)):
                        
        for var_ind in range(length):
            output += '\n{0}{1}{2}(x{1}{2}) = '.format(
                function_name, 
                get_subscript(eq_ind + 1), 
                get_subscript(var_ind + 1))
                                
            for degree in range(degree_range):
                    
                if degree != 0:
                    if coeff_matrix[ind] >= 0:
                        output += ' + '
                    else:
                        output += ' - '
                        
                output += '{0:.5} {1}{2}(x{3}{4})'.format(
                    np.abs(coeff_matrix[ind]), var_name, get_subscript(degree),
                    get_subscript(eq_ind + 1), get_subscript(var_ind + 1))
                    
                ind += 1
                    
    return output


def print_equation_2(coeff_matrixes, target_ind=1, coeff_name='a', function_name='F', var_name='ψ', mult=False):
    
    if mult:
        return print_equation_2_mult(
            coeff_matrixes=coeff_matrixes, target_ind=target_ind, 
            coeff_name=coeff_name, function_name=function_name, var_name=var_name)
    
    output = ''
    output += '\n\nДругий ієрархічний рівень\n'
    output += 'Формування функцій F\n'
        
    for eq_ind, coeff_matrix in enumerate(coeff_matrixes):
        output += '\nВектор коефіціентів {0}{1}{2}'.format(
            coeff_name, get_subscript(target_ind),
            get_subscript(eq_ind + 1))
            
        output += '\n'
        output += str(coeff_matrix)
        output += '\n'
        
    for eq_ind, coeff_matrix in enumerate(coeff_matrixes):
            
        output += '\n{0}{1}{2}(x{2}) = '.format(
            function_name, get_subscript(target_ind),
            get_subscript(eq_ind + 1))
                                
        for var_ind in range(coeff_matrix.shape[0]):
                    
            if var_ind != 0:
                if coeff_matrix[var_ind] >= 0:
                    output += ' + '
                else:
                    output += ' - '
                        
            output += '{0:.5} {1}{2}{3}(x{2}{3})'.format(
                np.abs(coeff_matrix[var_ind]), var_name, get_subscript(eq_ind + 1),
                get_subscript(var_ind + 1))
                
    return output


def print_equation_1(coeff_matrix, target_ind=1, coeff_name='c', function_name='Φ', var_name='F', mult=False):
    
    if mult:
        return print_equation_1_mult(
            coeff_matrix=coeff_matrix, target_ind=target_ind, 
            coeff_name=coeff_name, function_name=function_name, var_name=var_name)
    
    output = ''
        
    output += 'Перший ієрархічний рівень\n'
    output += 'Формування функцій Φ\n'
        
    output += '\nВектор коефіціентів {0}\n{1}\n'.format(coeff_name, coeff_matrix)
    output += '{0}{1}(x) = '.format(function_name, get_subscript(target_ind))
                                
    for var_ind in range(coeff_matrix.shape[0]):
                    
        if var_ind != 0:
            if coeff_matrix[var_ind] >= 0:
                output += ' + '
            else:
                output += ' - '
                        
        output += '{0:.5} {1}{2}{3}(x{2})'.format(
            np.abs(coeff_matrix[var_ind]), var_name, get_subscript(var_ind + 1),
            get_subscript(target_ind))
            
    return output



def print_equation_3_mult(coeff_matrix, lengths, degrees, coeff_name='λ', function_name='ψ', var_name='T'):
        
    output = ''
        
    output += 'Третій ієрархічний рівень\n'
    output += 'Формування функцій ψ\n'
        
    ind = 0
                
    for eq_ind, (length, degree_range) in enumerate(zip(lengths, degrees)):
            
        output += '\nМатриця коефіціентів {0}{1}\n'.format(coeff_name, get_subscript(eq_ind + 1))
            
        coeff_matrix_part = coeff_matrix[ind: ind + length * degree_range].reshape(length, degree_range)
        output += str(coeff_matrix_part)
        output += '\n'
        ind += length * degree_range
        
    ind = 0
    for eq_ind, (length, degree_range) in enumerate(zip(lengths, degrees)):
                        
        for var_ind in range(length):
            output += '\n{0}{1}{2}(x{1}{2}) = '.format(
                function_name, 
                get_subscript(eq_ind + 1), 
                get_subscript(var_ind + 1))
                                
            for degree in range(degree_range):
                    
                if degree != 0:
                    output += ' * '
                        
                degree += 1
                        
                output += '(1 + {1}{2}(x{3}{4})) ^ {0:.5}'.format(
                    np.abs(coeff_matrix[ind]), var_name, get_subscript(degree),
                    get_subscript(eq_ind + 1), get_subscript(var_ind + 1))
                    
                ind += 1
                    
    return output


def print_equation_2_mult(coeff_matrixes, target_ind=1, coeff_name='a', function_name='F', var_name='ψ'):
        
    output = ''
    output += '\n\nДругий ієрархічний рівень\n'
    output += 'Формування функцій F\n'
        
    for eq_ind, coeff_matrix in enumerate(coeff_matrixes):
        output += '\nВектор коефіціентів {0}{1}{2}'.format(
            coeff_name, get_subscript(target_ind),
            get_subscript(eq_ind + 1))
            
        output += '\n'
        output += str(coeff_matrix)
        output += '\n'
        
    for eq_ind, coeff_matrix in enumerate(coeff_matrixes):
            
        output += '\n{0}{1}{2}(x{2}) = '.format(
            function_name, get_subscript(target_ind),
            get_subscript(eq_ind + 1))
                                
        for var_ind in range(coeff_matrix.shape[0]):
                    
            if var_ind != 0:
                output += ' * '
                        
            output += '(1 + {1}{2}{3}(x{2}{3})) ^ {0:.5}'.format(
                np.abs(coeff_matrix[var_ind]), var_name, get_subscript(eq_ind + 1),
                get_subscript(var_ind + 1))
                
    return output


def print_equation_1_mult(coeff_matrix, target_ind=1, coeff_name='c', function_name='Φ', var_name='F'):
        
    output = ''
        
    output += 'Перший ієрархічний рівень\n'
    output += 'Формування функцій Φ\n'
        
    output += '\nВектор коефіціентів {0}\n{1}\n'.format(coeff_name, coeff_matrix)
    output += '{0}{1}(x) = '.format(function_name, get_subscript(target_ind))
                                
    for var_ind in range(coeff_matrix.shape[0]):
                    
        if var_ind != 0:
            output += ' * '
                        
        output += '(1 + {1}{2}{3}(x{2})) ^ {0:.5}'.format(
            np.abs(coeff_matrix[var_ind]), var_name, get_subscript(var_ind + 1),
            get_subscript(target_ind))
            
    return output


def output_diff(A, b, coeff, mult, on_array=False):
    
    output = ''
    output += "\nНев'язка\n"

    if on_array: 
        diff = np.array([np.max(forward(A_inst, coeff_inst, mult) - b) for A_inst, coeff_inst in zip(A, coeff)])
        output += str(diff)
        output += '\n'
    else: 
        diff = np.max(forward(A, coeff, mult) - b)
        output += '{0:.5}\n'.format(diff)
            
    output += '\n'
    
    return output