{% extends 'base.htm' %}
{% block title %}Вход — Круизы и каюты{% endblock %}
{% block content %}
<section class="hero compact">
  <h1>Вход</h1>
  <p class="muted">Введите логин и пароль, чтобы продолжить работу с бронированиями.</p>
</section>

<form class="card form narrow" method="post">
  <div class="form-row">
    <label for="login">Логин</label>
    <input id="login" name="login" type="text" required pattern="^[A-Za-z0-9]{6,}$" autocomplete="username">
  </div>
  <div class="form-row">
    <label for="password">Пароль</label>
    <input id="password" name="password" type="password" required minlength="8" autocomplete="current-password">
  </div>
  <div class="form-actions">
    <button type="submit" class="btn primary">Войти</button>
    <a class="btn ghost" href="{{ url_for('register') }}">Создать аккаунт</a>
  </div>

  <div class="hint-box">
    <strong>Демо-доступ:</strong><br>
    admin123 / Admin123!<br>
    client25 / Client123!
  </div>
</form>
{% endblock %}
