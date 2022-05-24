import plotly.express as px

def chart_builder(dict_data):
    
    if 'group' in  dict_data:
        color = dict_data['group']
    else:
        color = None

    if 'graph_title' in  dict_data:
        graph_title = dict_data['graph_title']
    else:
        graph_title = None

    if 'x_axis_label' in  dict_data:
        x_axis_label = dict_data['x_axis_label']
    else:
        x_axis_label = None

    if 'y_axis_label' in  dict_data:
        y_axis_label = dict_data['y_axis_label']
    else:
        y_axis_label = None

    if 'group_label' in  dict_data:
        group_label = dict_data['group_label']
    else:
        group_label = None

    if 'export_location' in dict_data:
        export_location = dict_data['export_location']
    else:
        export_location = ""

    # Line Chart
    if dict_data['graph_type'] == 'line':
        fig = px.line(
            height=dict_data['graph_height']
            ,width=dict_data['graph_width']
            ,x= dict_data['x_axis']
            ,y= dict_data['y_axis']
            ,template= 'simple_white'
            ,color=color
            ,title= graph_title
            ,labels={'x': x_axis_label, 'y':y_axis_label, 'color':group_label}
            )
        fig.write_image(export_location + '.' + dict_data['export_type'])
    
    # Bar Chart
    if dict_data['graph_type'] == 'bar':
        fig = px.bar(
            barmode='group'
            ,height=dict_data['graph_height']
            ,width=dict_data['graph_width']
            ,x= dict_data['x_axis']
            ,y= dict_data['y_axis']
            ,template= 'simple_white'
            ,color=color
            ,title= graph_title
            ,labels={'x': x_axis_label, 'y':y_axis_label, 'color':group_label}
            )
        fig.write_image(export_location + '.' + dict_data['export_type'])

    # Scatter Chart
    if dict_data['graph_type'] == 'scatter':
        fig = px.scatter(
            height=dict_data['graph_height']
            ,width=dict_data['graph_width']
            ,x= dict_data['x_axis']
            ,y= dict_data['y_axis']
            ,template= 'simple_white'
            ,color=color
            ,title= graph_title
            ,labels={'x': x_axis_label, 'y':y_axis_label, 'color':group_label}
            )
        fig.write_image(export_location + '.' + dict_data['export_type'])