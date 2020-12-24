from flask import Flask, render_template, request, escape
import direction_of_walking
from log_sys import log_request


app = Flask(__name__)


@app.route('/')
def base():
    title = '步行路径规划'
    return render_template('entry.html',
                           the_title=title,)


@app.route('/search0', methods=['POST'])
def do_search_0() -> 'html':
    key = request.form['key']
    start_address = request.form['start_address']
    end_address = request.form['end_address']
    title = '查询结果'
    df = direction_of_walking.direction_walking(key, start_address, end_address)
    results = df.loc[:, ['instruction', 'distance', 'duration']]
    results.columns = ['指引', '路程', '时间']
    total_walk = direction_of_walking.total_walk(df)
    total_walk_time = direction_of_walking.total_walk_time(df)
    route = results['指引'].tolist()
    log_request(request, route)
    return render_template('results.html',
                           the_title=title,
                           the_start_address=start_address,
                           the_end_address=end_address,
                           the_results=results,
                           the_html_table=results.to_html(index=False),
                           the_total_walk=total_walk,
                           the_total_walk_time=total_walk_time,)


@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('walking.log', 'r') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('用户输入数据', '远程地址', '用户代理', '查询结果')
    return render_template('log.html',
                           the_title='查看日志',
                           the_row_titles=titles,
                           the_data=contents,)


if __name__ == '__main__':
    app.run(debug=True)
