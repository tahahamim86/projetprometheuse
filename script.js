window.onload = function() {
    fetch('http://localhost:9090/api/v1/query?query=probe_success')
    .then(response => response.json())
    .then(data => {
        const statusBody = document.getElementById('status-body');
        data.data.result.forEach(result => {
            const application = result.metric.instance;
            const status = result.value[1] === '1' ? '<h3 style="color:green">Up</h3>' : '<h3 style="color:red">Down</h3>';
            const row = `<tr>
                            <td>${application}</td>
                            <td>${status}</td>
                        </tr>`;
            statusBody.innerHTML += row;
        });
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });
};

