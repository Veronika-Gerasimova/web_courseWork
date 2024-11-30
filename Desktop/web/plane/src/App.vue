<script setup>
import { onBeforeMount } from 'vue';
import axios from 'axios';
import Cookies from 'js-cookie';
import useUserStore from './stores/userStore';
import { storeToRefs } from 'pinia';

const userStore = useUserStore();
const {
  isAuthenticated,
  username,
  userId,
} = storeToRefs(userStore);

onBeforeMount(() => {
  axios.defaults.headers.common['X-CSRFToken'] = Cookies.get("csrftoken");
})

</script>

<template>
  <div class="container">
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid">
        <a class="navbar-brand" href="/">Главная</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavDropdown">
          <ul class="navbar-nav">
            <li class="nav-item">
              <router-link class="nav-link" to="/clients">Клиенты</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/tickets">Билеты</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/baggages">Багаж</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/flights">Рейсы</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/airplanes">Самолеты</router-link>
            </li>
          </ul>
          <ul class="navbar-nav">
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  Пользователь
                </a>
                <ul class="dropdown-menu">
                  <li><a class="dropdown-item" href="/admin">Админка</a></li>
                  <li><a class="dropdown-item" href="/login">Вход</a></li>
                </ul>
              </li>
          </ul>
        </div>
      </div>
    </nav>
  </div>

  <div class="container">
    <router-view/>
  </div>

</template>

<style scoped>

</style>