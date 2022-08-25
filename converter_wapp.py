from flask import Flask, render_template, request
from conversion import Conversion

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def webpage():

    if request.method == 'POST':
        enter = float(request.form['in'])
        conv = Conversion(enter)

        check = request.form['operation']
        output = None
        options = {'f': 0, 'k': 1, 'r': 2}

        out = (
            [None, None, conv.c_f(enter)],
            [None, None, conv.c_k(enter)],
            [None, None, conv.c_r(enter)]
        )

        for x in options.keys():
            if x == check:
                out[options[x]][0] = 'checked'
                out[options[x]][1] = 'autofocus'
                output = out[options[x]][2]

        return render_template('converter.html',
                               enter=enter,
                               output=output,
                               f=out[0][0],
                               k=out[1][0],
                               r=out[2][0],
                               ffocus=out[0][1],
                               kfocus=out[1][1],
                               rfocus=out[2][1],
                               )

    return render_template('converter.html',
                           enter=0,
                           output=0)

if __name__ == '__main__':
    app.run(debug=True)
