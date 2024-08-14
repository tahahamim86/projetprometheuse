from flask import Flask, request, render_template, redirect, url_for
import yaml

app = Flask(__name__)

PROMETHEUS_CONFIG_FILE = r'C:\prometheus\prometheus\prometheus.yml'

def load_config():
    with open(PROMETHEUS_CONFIG_FILE, 'r') as file:
        return yaml.safe_load(file)

def save_config(config):
    with open(PROMETHEUS_CONFIG_FILE, 'w') as file:
        yaml.safe_dump(config, file)

@app.route('/')
def index():
    config = load_config()
    scrape_configs = {job['job_name']: job for job in config['scrape_configs']}
    return render_template('index.html', scrape_configs=scrape_configs)

@app.route('/edit/<job_name>', methods=['GET', 'POST'])
def edit(job_name):
    config = load_config()
    scrape_configs = {job['job_name']: job for job in config['scrape_configs']}
    job = scrape_configs[job_name]
    if request.method == 'POST':
        new_targets = request.form.getlist('targets')
        job['static_configs'][0]['targets'] = new_targets
        save_config(config)
        return redirect(url_for('index'))
    return render_template('edit.html', job_name=job_name, targets=job['static_configs'][0]['targets'])

if __name__ == '__main__':
    app.run(debug=True)
