/* worksheet_viewer.js — minimal fin123 worksheet renderer
   Reads a precompiled worksheet JSON artifact and renders it into a target element. */
(function () {
    'use strict';

    function formatValue(val, format) {
        if (val == null) return '';
        if (format === 'currency') return '$' + val.toFixed(2);
        if (format === 'percent')  return (val * 100).toFixed(1) + '%';
        return String(val);
    }

    function render(artifact, targetId) {
        var el = document.getElementById(targetId);
        if (!el || !artifact) return;

        var table = document.createElement('table');
        table.className = 'ws-table';

        // header
        var thead = document.createElement('thead');
        var hr = document.createElement('tr');
        artifact.columns.forEach(function (col) {
            var th = document.createElement('th');
            th.textContent = col.name;
            if (col.type === 'number') th.className = 'ws-num';
            hr.appendChild(th);
        });
        // flags column
        var thFlag = document.createElement('th');
        thFlag.textContent = 'flags';
        hr.appendChild(thFlag);
        thead.appendChild(hr);
        table.appendChild(thead);

        // body
        var tbody = document.createElement('tbody');
        artifact.rows.forEach(function (row) {
            var tr = document.createElement('tr');
            var hasFlag = row.flags && row.flags.length > 0;
            if (hasFlag) tr.className = 'ws-flagged';

            artifact.columns.forEach(function (col) {
                var td = document.createElement('td');
                td.textContent = formatValue(row[col.name], col.format);
                if (col.type === 'number') td.className = 'ws-num';
                tr.appendChild(td);
            });

            var tdFlag = document.createElement('td');
            tdFlag.className = 'ws-flag-cell';
            if (hasFlag) {
                var span = document.createElement('span');
                span.className = 'ws-flag';
                span.textContent = row.flags[0];
                tdFlag.appendChild(span);
            }
            tr.appendChild(tdFlag);

            tbody.appendChild(tr);
        });
        table.appendChild(tbody);
        el.appendChild(table);
    }

    // fetch artifact and render
    var target = document.querySelector('[data-worksheet]');
    if (target) {
        var src = target.getAttribute('data-worksheet');
        var id  = target.id;
        var req = new XMLHttpRequest();
        req.open('GET', src, true);
        req.onload = function () {
            if (req.status === 200) {
                render(JSON.parse(req.responseText), id);
            }
        };
        req.send();
    }
})();
