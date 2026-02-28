{% extends 'base.htm' %}
{% block title %}Мои заказы — Круизы и каюты{% endblock %}
{% block content %}
<section class="hero compact">
  <h1>Мои заказы</h1>
  <p class="muted">Здесь отображаются ваши оформленные бронирования и их текущий статус.</p>
</section>

<section class="card">
  <div class="table-scroll">
    <table class="table">
      <thead>
        <tr>
          <th>Заказ</th>
          <th>Круиз</th>
          <th>Лайнер</th>
          <th>Дата</th>
          <th>Каюты</th>
          <th>Статус</th>
          <th>Оплата</th>
          <th class="right">Сумма, ₽</th>
        </tr>
      </thead>
      <tbody>
        {% for row in orders %}
        <tr>
          <td>#{{ row.id }}</td>
          <td>{{ row.cruise_name }}</td>
          <td>{{ row.ship_name }}</td>
          <td>{{ row.starts_at[:16] }}</td>
          <td>{{ row.cabins }}</td>
          <td><span class="badge {% if row.status == 'confirmed' %}ok{% else %}warn{% endif %}">{{ row.status }}</span></td>
          <td><span class="badge {% if row.payment_status == 'paid' %}ok{% else %}warn{% endif %}">{{ row.payment_status }}</span></td>
          <td class="right">{{ '%.2f'|format(row.total_amount) }}</td>
        </tr>
        {% else %}
        <tr><td colspan="8" class="center muted">У вас пока нет заказов.</td></tr>
        {% endfor %}
      </tbody>
    </table>
  </div>
</section>
{% endblock %}
