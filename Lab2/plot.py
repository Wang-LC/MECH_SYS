from sensor import generate_sensor_data
from null_filter import apply_null_fil

def write(data, file_name):
    with open(file_name, 'w') as file:
        for d in data:
            file.write(str(d) + '\n')


write(generate_sensor_data(50), 'sensor_data')

data = []
with open('sensor_data', 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        data.extend([line])
filter_data = apply_null_filter(data)

write(filter_data, 'filted_data')
