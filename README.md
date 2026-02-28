{% extends 'base.htm' %}
{% block title %}Отчётность — Круизы и каюты{% endblock %}
{% block content %}
<section class="hero compact">
  <h1>Учёт продаж и отчётность</h1>
  <p class="muted">Ниже выводятся данные по продажам кают, загрузке рейсов и ежедневной выручке.</p>
</section>

<section class="card">
  <h2>Продажи по рейсам</h2>
  <div class="table-scroll">
    <table class="table">
      <thead>
        <tr>
          <th>ID</th>
          <th>Круиз</th>
          <th>Лайнер</th>
          <th>Дата</th>
          <th class="right">Продано</th>
          <th class="right">Возврат</th>
          <th class="right">Всего кают</th>
          <th class="right">Выручка, ₽</th>
        </tr>
      </thead>
      <tbody>
        {% for row in sales %}
        <tr>
          <td>#{{ row.performance_id }}</td>
          <td>{{ row.cruise_name }}</td>
          <td>{{ row.ship_name }}</td>
          <td>{{ row.starts_at[:16] }}</td>
          <td class="right">{{ row.sold_count }}</td>
          <td class="right">{{ row.returned_count }}</td>
          <td class="right">{{ row.total_tickets }}</td>
          <td class="right">{{ '%.2f'|format(row.revenue or 0) }}</td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
  </div>
</section>

<section class="card">
  <h2>Заполняемость рейсов</h2>
  <div class="table-scroll">
    <table class="table">
      <thead>
        <tr>
          <th>Рейс</th>
          <th>Дата</th>
          <th class="right">Всего</th>
          <th class="right">Продано</th>
          <th class="right">В резерве</th>
          <th>Индикатор</th>
        </tr>
      </thead>
      <tbody>
        {% for row in occupancy %}
        {% set percent = (row.sold * 100 / row.issued_tickets) if row.issued_tickets else 0 %}
        <tr>
          <td>{{ row.cruise_name }}</td>
          <td>{{ row.starts_at[:16] }}</td>
          <td class="right">{{ row.issued_tickets }}</td>
          <td class="right">{{ row.sold }}</td>
          <td class="right">{{ row.reserved }}</td>
          <td>
            <span class="meter"><span style="width: {{ percent|round(0) }}%"></span></span>
            <span class="badge {% if percent >= 70 %}ok{% elif percent >= 40 %}warn{% else %}err{% endif %}">{{ percent|round(0) }}%</span>
          </td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
  </div>
</section>

<section class="card">
  <h2>Выручка по дням</h2>
  <div class="table-scroll">
    <table class="table">
      <thead>
        <tr><th>Дата</th><th class="right">Выручка, ₽</th></tr>
      </thead>
      <tbody>
        {% for row in revenue %}
        <tr>
          <td>{{ row.day }}</td>
          <td class="right">{{ '%.2f'|format(row.revenue or 0) }}</td>
        </tr>
        {% endfor %}
      </tbody>
      <tfoot>
        <tr>
          <td class="right"><strong>Итого</strong></td>
          <td class="right"><strong>{{ '%.2f'|format(revenue|sum(attribute='revenue')) }}</strong></td>
        </tr>
      </tfoot>
    </table>
  </div>
</section>
{% endblock %}
