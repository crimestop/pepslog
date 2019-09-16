import plotly.graph_objects as go

def plot(ene,ene_sm,diff,title):
	layout = go.Layout(
		title=title,
		paper_bgcolor='rgba(0,0,0,0)',
		plot_bgcolor='rgba(0,0,0,0)',
		xaxis=dict(showgrid=True, gridwidth=1, gridcolor='LightPink',title='n'),
		yaxis=dict(showgrid=True, gridwidth=1, gridcolor='LightPink',title='E'),
	)

	fig = go.Figure(layout=layout)

	fig.add_trace(go.Scatter(
		x=list(range(len(ene))),
		y=ene,
		name='data'
	))

	fig.add_trace(go.Scatter(
		x=list(range(len(ene_sm))),
		y=ene_sm,
		name='data with smear'
	))

	fig.update_layout(
		shapes=[
			# Line reference to the axes
			go.layout.Shape(
				type="line",
				xref="x",
				yref="paper",
				x0=df['pos'],
				y0=0,
				x1=df['pos'],
				y1=1,
				line=dict(
					color="LightSeaGreen",
					width=2,
				),
			)
		for df in diff if df['pos']>0],
		annotations=[
			go.layout.Annotation(
				x=df['pos'],
				y=0.95,
				xref="x",
				yref="paper",
				text=df['info'].replace('\n','<br>'),
				xanchor="left",
				ax=0,
				ay=0
			)
        for df in diff]
	)
	return fig