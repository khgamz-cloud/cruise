{% extends 'base.htm' %}
{% block title %}Круизы — Круизы и каюты{% endblock %}
{% block content %}
<section class="hero">
  <div>
    <h1>Подбор круизов и кают</h1>
    <p>Фильтруйте маршруты по направлению, дате, длительности и лайнеру. Затем выберите доступную каюту и оформите бронирование.</p>
  </div>
  <div class="hero-note">
    <div class="metric"><span>{{ cruises|length }}</span><small>маршрутов найдено</small></div>
    <div class="metric"><span>{{ cabins|length if selected_performance else 0 }}</span><small>кают в выбранном рейсе</small></div>
  </div>
</section>

<section class="card">
  <h2>Фильтры</h2>
  <form class="grid-4" method="get">
    <div class="form-row">
      <label for="direction">Направление</label>
      <select id="direction" name="direction">
        <option value="">Все</option>
        {% for item in directions %}
          <option value="{{ item.direction }}" {% if selected_direction == item.direction %}selected{% endif %}>{{ item.direction }}</option>
        {% endfor %}
      </select>
    </div>
    <div class="form-row">
      <label for="departure_date">Дата отправления</label>
      <input id="departure_date" name="departure_date" type="date" value="{{ selected_date }}">
    </div>
    <div class="form-row">
      <label for="duration_days">Длительность</label>
      <select id="duration_days" name="duration_days">
        <option value="">Любая</option>
        {% for item in durations %}
          <option value="{{ item.duration_days }}" {% if selected_duration == item.duration_days|string %}selected{% endif %}>{{ item.duration_days }} дней</option>
        {% endfor %}
      </select>
    </div>
    <div class="form-row">
      <label for="ship_id">Лайнер</label>
      <select id="ship_id" name="ship_id">
        <option value="">Все</option>
        {% for ship in ships %}
          <option value="{{ ship.id }}" {% if selected_ship == ship.id|string %}selected{% endif %}>{{ ship.name }}</option>
        {% endfor %}
      </select>
    </div>
    <div class="form-actions grid-full">
      <button class="btn primary" type="submit">Показать круизы</button>
      <a class="btn ghost" href="{{ url_for('index') }}">Сбросить</a>
    </div>
  </form>
</section>

<section class="cards-grid cruises-list">
  {% for cruise in cruises %}
    <article class="card cruise-card {% if selected_performance_id == cruise.id|string %}selected{% endif %}">
      <div class="space-between gap-12 wrap">
        <h3>{{ cruise.cruise_name }}</h3>
        <span class="badge ok">{{ cruise.direction }}</span>
      </div>
      <p class="muted">{{ cruise.ship_name }} · {{ cruise.duration_days }} дней · старт {{ cruise.starts_at[:16].replace('T', ' ') }}</p>
      <p><strong>Порты:</strong> {{ cruise.ports }}</p>
      <p><strong>Включено:</strong> {{ cruise.includes }}</p>
      <div class="price-line">от <strong>{{ '%.2f'|format(cruise.base_price) }} ₽</strong> за базовую каюту</div>
      <div class="form-actions">
        <a class="btn primary" href="{{ url_for('index', direction=selected_direction, departure_date=selected_date, duration_days=selected_duration, ship_id=selected_ship, performance_id=cruise.id) }}">Выбрать рейс</a>
      </div>
    </article>
  {% else %}
    <div class="card"><p>По заданным фильтрам круизы не найдены.</p></div>
  {% endfor %}
</section>

{% if selected_performance %}
<section class="card mt-24">
  <div class="space-between wrap gap-12">
    <div>
      <h2>Выбор каюты — {{ selected_performance.cruise_name }}</h2>
      <p class="muted">{{ selected_performance.ship_name }} · {{ selected_performance.duration_days }} дней · отправление {{ selected_performance.starts_at[:16] }}</p>
    </div>
    <div class="legend">
      <span class="legend-item"><i class="legend-box free"></i>Свободна</span>
      <span class="legend-item"><i class="legend-box reserved"></i>Забронирована</span>
      <span class="legend-item"><i class="legend-box sold"></i>Продана</span>
    </div>
  </div>

  <form method="post" action="{{ url_for('reserve') }}">
    <input type="hidden" name="performance_id" value="{{ selected_performance.id }}">

    <div class="cabin-grid">
      {% for cabin in cabins %}
        <label class="cabin-card {{ cabin.status }}">
          <input type="checkbox" name="ticket_ids" value="{{ cabin.ticket_id }}" {% if cabin.status != 'free' %}disabled{% endif %}>
          <span class="cabin-number">Каюта {{ cabin.cabin_number }}</span>
          <span>{{ cabin.category }}</span>
          <span>Палуба {{ cabin.deck }}</span>
          <span>До {{ cabin.capacity }} пассажиров</span>
          <strong>{{ '%.2f'|format(cabin.price) }} ₽</strong>
        </label>
      {% endfor %}
    </div>

    <div class="grid-3 mt-24">
      <div class="form-row">
        <label for="passengers">Количество пассажиров</label>
        <input id="passengers" name="passengers" type="number" min="1" value="1" required>
      </div>
      <div class="form-row">
        <label for="payment_method_id">Способ оплаты</label>
        <select id="payment_method_id" name="payment_method_id" required>
          <option value="1">Банковская карта</option>
          <option value="2">Перевод по реквизитам</option>
          <option value="3">Корпоративная оплата</option>
          <option value="4">Онлайн-платёж</option>
        </select>
      </div>
      <div class="form-row">
        <label for="email_to">E-mail для подтверждения</label>
        <input id="email_to" name="email_to" type="email" required placeholder="tickets@example.com" value="{{ current_user.email if current_user else '' }}">
      </div>
    </div>

    <div class="form-actions mt-16">
      {% if current_user %}
        <button class="btn primary" type="submit">Оформить бронирование</button>
      {% else %}
        <a class="btn primary" href="{{ url_for('login') }}">Войдите для бронирования</a>
      {% endif %}
    </div>
  </form>
</section>
{% endif %}
{% endblock %}
