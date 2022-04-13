from fastapi import FastAPI
import plotly.graph_objects as go


app = FastAPI()


@app.get("/hello")
def return_hello():
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=["Math", "Literature", "Watermelon", "Pears"],
        y=[3, 2, 1.39, 7]
    ))

    fig.update_layout(
        autosize=False,
        width=700,
        height=700,
        yaxis=dict(
            title_text="Average mark",
            ticktext=["1", "2", "3", "4"],
            tickvals=[1, 2, 3, 4],
            tickmode="array",
            titlefont=dict(size=30),
        )
    )

    fig.update_yaxes(automargin=True)

    fig.show()