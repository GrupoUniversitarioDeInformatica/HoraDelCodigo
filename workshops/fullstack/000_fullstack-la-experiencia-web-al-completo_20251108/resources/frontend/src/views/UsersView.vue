<template>
  <section 
    v-if="$route.name == 'users'"
    class="grid grid-cols-1 md:grid-cols-3 gap-4">
    <!-- Listado -->
    <div class="md:col-span-2 bg-slate-900/70 border border-slate-800 rounded-2xl p-4 flex flex-col gap-3">
      <div class="flex items-center justify-between">
        <h2 class="text-2xl font-semibold text-slate-200">Usuarios</h2>
        <button
          class="text-[15px] px-2 py-1 rounded-full border border-slate-700 text-slate-400 hover:border-sky-500 hover:text-sky-300 hover:cursor-pointer transition"
          @click="loadUsers"
        >
          Recargar
        </button>
      </div>
      <UsersPanel
        :users="users"
        :selected-user-id="selectedUserId"
        :loading="loading"
        :error="error"
        @select="selectUser"
      />
    </div>

    <!-- Formulario -->
    <div class="bg-slate-900/70 border border-slate-800 rounded-2xl p-4 flex flex-col gap-2">
      <h3 class="text-2xl font-semibold text-slate-200">Crear usuario</h3>
      <p class="text-[13px] text-slate-400">
        Rellena el formulario y conecta este submit con <code>/api/users</code>.
      </p>

      <form @submit.prevent="handleCreateUser" class="space-y-2">
        <input
          v-model="form.name"
          type="text"
          placeholder="Nombre"
          class="w-full px-2 py-1 rounded-lg bg-slate-900 border border-slate-700 text-sm focus:outline-none focus:ring-1 focus:ring-sky-500"
        />
        <input
          v-model="form.email"
          type="email"
          placeholder="Email"
          class="w-full px-2 py-1 rounded-lg bg-slate-900 border border-slate-700 text-sm focus:outline-none focus:ring-1 focus:ring-sky-500"
        />
        <input
          v-model="form.password"
          type="password"
          placeholder="Password"
          class="w-full px-2 py-1 rounded-lg bg-slate-900 border border-slate-700 text-sm focus:outline-none focus:ring-1 focus:ring-sky-500"
        />
        <button
          type="submit"
          class="w-full mt-1 text-[16px] py-1 rounded-lg bg-sky-600 hover:bg-sky-500 text-white transition hover:cursor-pointer"
        >
          Crear usuario
        </button>
      </form>

      <div v-if="selectedUserId" class="mt-3 text-[13px] text-slate-400">
        Usuario seleccionado: <span class="text-sky-300">#{{ selectedUserId }}</span>
      </div>
    </div>
  </section>
  <RouterView v-else></RouterView>
</template>

<script setup>
import { ref } from 'vue'
import UsersPanel from '@/components/UsersPanel.vue'

const users = ref([])
const selectedUserId = ref(null)
const loading = ref(false)
const error = ref('')
const form = ref({ name: '', email: '', password: '' })

function loadUsers() {
  loading.value = true
  error.value = ''

  // TODO: Reemplazar mock por GET /api/users
  setTimeout(() => {
    users.value = [
      { id: 1, name: 'Alice', email: 'alice@example.local' },
      { id: 2, name: 'Bob', email: 'bob@example.local' },
      { id: 3, name: 'Carol', email: 'carol@example.local' }
    ]
    loading.value = false
  }, 200)
}

function selectUser(id) {
  selectedUserId.value = id
}

function handleCreateUser() {
  // TODO: POST /api/users con form.value
  console.log('TODO: crear usuario vía API', form.value)
}

// carga inicial mock
loadUsers()
</script>
