<template>
  <div class="modal fade show" tabindex="-1" style="display: block;" v-if="isVisible">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Двухфакторная аутентификация</h5>
          <button type="button" class="btn-close" @click="closeModal"></button>
        </div>
        <div class="modal-body">
          <input 
            type="text" 
            v-model="otpCode" 
            placeholder="Введите код" 
            class="form-control">
          <p v-if="isExpired" class="text-danger mt-2">Время для ввода кода истекло! Пожалуйста, запросите новый код.</p>
        </div>
        <div class="modal-footer">
          <button class="btn btn-primary" @click="verifyCode" :disabled="isExpired">Проверить</button>
          <button class="btn btn-secondary" @click="closeModal">Закрыть</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue';

const otpCode = ref('');
const isVisible = ref(true);
const isExpired = ref(false);  // Флаг истечения времени
const otpStartTime = ref(null); // Время ввода кода

defineProps({
  onSuccess: {
    type: Function,
    required: true,
  },
  onClose: {
    type: Function,
    required: true,
  },
});

const emit = defineEmits(['onSuccess', 'onClose']);

function verifyCode() {
  if (otpCode.value === '1234') { // Замените "1234" на реальную проверку
    otpStartTime.value = Date.now(); // Сохраняем время успешного ввода кода
    emit('onSuccess');
  } else {
    alert('Неверный код!');
  }
}

function closeModal() {
  emit('onClose');
  isVisible.value = false;
}

// Следим за временем и проверяем, не истекло ли 5 минут
watch(otpStartTime, () => {
  if (otpStartTime.value) {
    const elapsedTime = (Date.now() - otpStartTime.value) / 1000; // Время в секундах
    if (elapsedTime >= 300) { // Если прошло больше 5 минут (300 секунд)
      isExpired.value = true;  // Код истек
    }
  }
});

onMounted(() => {
  // При монтировании окна проверим, не истекло ли время
  isExpired.value = false;
});
</script>
