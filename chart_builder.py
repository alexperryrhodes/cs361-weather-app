import plotly.express as px

def chart_builder(dict_data):
    
    # Series of if statements allow for optional data
    if 'group' in  dict_data:
        color = dict_data['group']
    else:
        color = None

    if 'group_label' in  dict_data:
        group_label = dict_data['group_label']
    else:
        group_label = None

    # Creates Line Chart 
    if dict_data['graph_type'] == 'line':
        fig = px.line(
            height=dict_data['graph_height']
            ,width=dict_data['graph_width']
            ,x= dict_data['x_axis']
            ,y= dict_data['y_axis']
            ,template= 'simple_white'
            ,color=color
            ,title= dict_data['graph_title']
            ,labels={'x': dict_data['x_axis_label'], 'y':dict_data['y_axis_label'], 'color':group_label}
            )
        fig.write_image(dict_data['export_location'] + '.' + dict_data['export_type'])
    
    # Creates Bar Chart
    if dict_data['graph_type'] == 'bar':
        fig = px.bar(
            barmode='group'
            ,height=dict_data['graph_height']
            ,width=dict_data['graph_width']
            ,x= dict_data['x_axis']
            ,y= dict_data['y_axis']
            ,template= 'simple_white'
            ,color=color
            ,title= dict_data['graph_title']
            ,labels={'x': dict_data['x_axis_label'], 'y':dict_data['y_axis_label'], 'color':group_label}
            )
        fig.write_image(dict_data['export_location'] + '.' + dict_data['export_type'])

    # Creates Scatter Chart
    if dict_data['graph_type'] == 'scatter':
        fig = px.scatter(
            height=dict_data['graph_height']
            ,width=dict_data['graph_width']
            ,x= dict_data['x_axis']
            ,y= dict_data['y_axis']
            ,template= 'simple_white'
            ,color=color
            ,title= dict_data['graph_title']
            ,labels={'x': dict_data['x_axis_label'], 'y':dict_data['y_axis_label'], 'color':group_label}
            )
        fig.write_image(dict_data['export_location'] + '.' + dict_data['export_type'])