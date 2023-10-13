from datetime import datetime
import json
import urllib.request

def __check_date(starttime, endtime):
    if starttime > endtime:
        raise ValueError("Error! Start time must be before or equal to end time")
    return True

def __check_index(index):
    allowed_indices = ['Kp', 'ap', 'Ap', 'Cp', 'C9', 'Hp30', 'Hp60', 'ap30', 'ap60', 'SN', 'Fobs', 'Fadj']
    if index not in allowed_indices:
        raise ValueError(f"Error! Wrong index parameter! Allowed values are: {', '.join(allowed_indices)}")
    return True

def __check_status(status):
    allowed_statuses = ['all', 'def']
    if status not in allowed_statuses:
        raise ValueError(f"Error! Wrong option parameter! Allowed values are: {', '.join(allowed_statuses)}")
    return True

def __add_status(url, status):
    if status == 'def':
        url = url + '&status=def'
    return url

def getKpindex(starttime, endtime, index, status='all'):
    """
    Download 'Kp', 'ap', 'Ap', 'Cp', 'C9', 'Hp30', 'Hp60', 'ap30', 'ap60', 'SN', 'Fobs', or 'Fadj' index data from kp.gfz-potsdam.de.
    Date format for starttime and endtime is 'yyyy-mm-dd' or 'yyyy-mm-ddTHH:MM:SSZ'.
    An optional 'def' parameter can be used to get only definitive values (only available for 'Kp', 'ap', 'Ap', 'Cp', 'C9', 'SN').
    'Hp30', 'Hp60', 'ap30', 'ap60', 'Fobs', and 'Fadj' do not have status info.
    Example: (time, index, status) = getKpindex('2021-09-29', '2021-10-01', 'Ap', 'def')
    Example: (time, index, status) = getKpindex('2021-09-29T12:00:00Z', '2021-10-01T12:00:00Z', 'Kp')
    """
    timestamps = []
    index_data = []
    status_data = []

    if len(starttime) == 10 and len(endtime) == 10:
        starttime = starttime + 'T00:00:00Z'
        endtime = endtime + 'T23:59:00Z'

    try:
        d1 = datetime.strptime(starttime, '%Y-%m-%dT%H:%M:%SZ')
        d2 = datetime.strptime(endtime, '%Y-%m-%dT%H:%M:%SZ')

        __check_date(d1, d2)
        __check_index(index)
        __check_status(status)

        time_string = "start=" + d1.strftime('%Y-%m-%dT%H:%M:%SZ') + "&end=" + d2.strftime('%Y-%m-%dT%H:%M:%SZ')
        url = 'https://kp.gfz-potsdam.de/app/json/?' + time_string + "&index=" + index
        if index not in ['Hp30', 'Hp60', 'ap30', 'ap60', 'Fobs', 'Fadj']:
            url = __add_status(url, status)

        webURL = urllib.request.urlopen(url)
        binary = webURL.read()
        text = binary.decode('utf-8')

        try:
            data = json.loads(text)
            timestamps = tuple(data["datetime"])
            index_data = tuple(data[index])
            if index not in ['Hp30', 'Hp60', 'ap30', 'ap60', 'Fobs', 'Fadj']:
                status_data = tuple(data["status"])
        except Exception as e:
            print("Error parsing JSON data:", e)

    except Exception as e:
        print("An error occurred:", e)

    return timestamps, index_data, status_data

# Example usage:
# (time, index, status) = getKpindex('2021-09-29', '2021-10-01', 'Ap', 'def')
# (time, index, status) = getKpindex('2021-09-29T12:00:00Z', '2021-10-01T12:00:00Z', 'Kp')


# ejemplo de datos de entrada
start_date = '2016-01-01'
end_date = '2016-01-02'
index_type = 'Kp'
status = 'all'

# llamo a la función para obtener datos
timestamps, index_data, status_data = getKpindex(start_date, end_date, index_type, status)

# Imprimo los datos
for time, value, stat in zip(timestamps, index_data, status_data):
    print(f"Timestamp: {time}, Index Value: {value}, Status: {stat}")
