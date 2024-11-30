<script setup>
import { onBeforeMount, ref } from 'vue';
import axios from 'axios';

const baggages = ref([]);
const clients = ref([]);
const tickets = ref([]); // Массив билетов
const newBaggage = ref({
  ticket: null,
  weight: '',
  baggage_type: ''
});
const baggageToEdit = ref({});
const baggageToRemove = ref(null); 
const showDeleteConfirmModal = ref(false); 

const stats = ref({ count: 0, avg: 0, max: 0, min: 0 });

async function fetchBaggagesStats() {
  try {
    const response = await axios.get("/api/baggage/stats/");
    stats.value = response.data;
  } catch (error) {
    console.error("Ошибка при получении статистики:", error);
  }
}

// Функция получения всех клиентов
async function fetchClients() {
  const r = await axios.get('/api/clients/');
  clients.value = r.data;
}

// Функция получения билетов
async function fetchTickets() {
  const r = await axios.get('/api/tickets/');
  tickets.value = r.data;
}

// Функция получения багажа
async function fetchBaggages() {
  const r = await axios.get('/api/baggage/');
  baggages.value = r.data;
}

// Добавление багажа
async function addBaggage() {
  try {
    await axios.post('/api/baggage/', newBaggage.value);
    newBaggage.value = { ticket: null, weight: '', baggage_type: '' };
    await fetchBaggages();
  } catch (error) {
    console.error("Ошибка при добавлении багажа:", error.response ? error.response.data : error.message);
  }
}

// Удаление багажа
async function removeBaggage(id) {
  try {
    await axios.delete(`/api/baggage/${id}/`);
    await fetchBaggages();
  } catch (error) {
    console.error("Ошибка при удалении багажа:", error);
  }
}

// Открытие модального окна подтверждения удаления
function confirmRemoveBaggage(baggage) {
  baggageToRemove.value = baggage;
  showDeleteConfirmModal.value = true; // Открываем модальное окно
}

// Подтверждение удаления багажа
async function onRemoveConfirmed() {
  if (baggageToRemove.value) {
    await removeBaggage(baggageToRemove.value.id); 
    showDeleteConfirmModal.value = false; 
    baggageToRemove.value = null; 
  }
}
const showEditModal = ref(false);

async function onBaggageEditClick(baggage) {
  // Устанавливаем данные о багаже
  baggageToEdit.value = {
    ...baggage,
    ticket: baggage.ticket_detail.id // Передаем только ID билета
  };
  showEditModal.value = true; // Открытие модального окна для редактирования
}

async function updateBaggage() {
  try {
    const formData = {
      weight: baggageToEdit.value.weight,
      baggage_type: baggageToEdit.value.baggage_type,
      ticket: baggageToEdit.value.ticket 
    };

    console.log("Form Data to update:", formData); // Логирование данных
    console.log("Baggage ID:", baggageToEdit.value.id); // Логирование ID багажа

    await axios.put(`/api/baggage/${baggageToEdit.value.id}/`, formData);
    await fetchBaggages(); // Обновление списка багажа после сохранения
  } catch (error) {
    console.error("Ошибка при обновлении багажа:", error.response ? error.response.data : error);
  }
  showEditModal.value = false; // Закрытие модального окна после обновления
}



onBeforeMount(async () => {
  await fetchClients();
  await fetchTickets();
  await fetchBaggages();
  await fetchBaggagesStats();
});
</script>

<template>
  <div class="container">
    <h1 class="my-4">Багаж</h1>
    <form @submit.prevent="addBaggage" class="mb-4">
      <div class="row">
        <div class="col">
          <select v-model="newBaggage.ticket" class="form-select" required>
            <option value="" disabled>Выберите билет</option>
            <option v-for="ticket in tickets" :key="ticket.id" :value="ticket.id">
              {{ ticket.seat_number }} ({{ ticket.client_detail.name }})
            </option>
          </select>
        </div>
        <div class="col">
          <input v-model="newBaggage.weight" type="number" class="form-control" placeholder="Вес (кг)" required />
        </div>
        <div class="col">
          <input v-model="newBaggage.baggage_type" type="text" class="form-control" placeholder="Тип багажа" required />
        </div>
        <div class="col-auto">
          <button class="btn btn-primary" type="submit">Добавить багаж</button>
        </div>
      </div>
    </form>

    <!-- Вывод статистики -->
    <div class="p-2">
            <h3>Статистика</h3>
            <ul>
              <li>Всего багажа: {{ stats.count }}</li>
              <li>Средний ID: {{ stats.avg }}</li>
              <li>Максимальный ID: {{ stats.max }}</li>
              <li>Минимальный ID: {{ stats.min }}</li>
            </ul>
      </div>

    <div v-for="baggage in baggages" :key="baggage.id" class="baggage-item mb-3 p-3 border rounded">
      <div class="col-8">
        <h5>{{ baggage.baggage_type }} - Вес: {{ baggage.weight }} кг</h5>
        <p><strong>Билет:</strong> {{ baggage.ticket_detail.seat_number }} ({{ baggage.ticket_detail.client_detail.name }})</p>
      </div>
      <button class="btn btn-success" @click="onBaggageEditClick(baggage)" data-bs-toggle="modal" data-bs-target="#editBaggageModal">
        <i class="bi bi-pen-fill"></i>
      </button>
      <button class="btn btn-danger" @click="confirmRemoveBaggage(baggage)">
        <i class="bi bi-x"></i>
      </button>
    </div>
  

  <!-- Модальное окно для подтверждения удаления  -->
  <div v-if="showDeleteConfirmModal" class="modal fade show" tabindex="-1" style="display: block;" @click="showDeleteConfirmModal = false">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Подтверждение удаления</h5>
            <button type="button" class="btn-close" @click="showDeleteConfirmModal = false"></button>
          </div>
          <div class="modal-body">
            <p>Вы действительно хотите удалить багаж ?</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" @click="showDeleteConfirmModal = false">Отмена</button>
            <button type="button" class="btn btn-danger" @click="onRemoveConfirmed">Удалить</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Модальное окно для редактирования багажа -->
    <div class="modal fade" id="editBaggageModal" tabindex="-1" aria-labelledby="editBaggageModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-lg"> 
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="editBaggageModalLabel">Редактировать багаж</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div class="row g-3"> 
              <div class="col-12">
                <div class="form-floating">
                  <input type="text" class="form-control" id="editBaggageType" v-model="baggageToEdit.baggage_type" required />
                  <label for="editBaggageType">Тип багажа</label>
                </div>
              </div>
              <div class="col-12">
                <div class="form-floating">
                  <input type="number" class="form-control" id="editBaggageWeight" v-model="baggageToEdit.weight" required />
                  <label for="editBaggageWeight">Вес (кг)</label>
                </div>
              </div>
              <div class="col-12">
                <select class="form-select" v-model="baggageToEdit.ticket" required>
                  <option value="" disabled>Выберите билет</option>
                  <option v-for="ticket in tickets" :key="ticket.id" :value="ticket.id">
                    {{ ticket.seat_number }} ({{ ticket.client_detail.name }})
                  </option>
                </select>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Закрыть</button>
            <button type="button" class="btn btn-primary" @click="updateBaggage" data-bs-dismiss="modal">Сохранить</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.baggage-item {
  padding: 0.5rem;
  border: 1px solid silver;
  margin: 1rem 0;
  box-shadow: 0 0 4px silver;
  border-radius: 8px;
  display: grid;
  grid-template-columns: 1fr auto auto auto;
  gap: 16px;
  align-items: center;
}
</style>
