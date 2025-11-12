<template>
  <div class="flex-1 overflow-y-auto space-y-1">
    <div v-if="loading" class="text-[15px] text-slate-500">Cargando usuarios...</div>
    <div v-else-if="error" class="text-[10px] text-red-400">{{ error }}</div>
    <div v-else-if="!users.length" class="text-[10px] text-slate-500">
      No hay usuarios. Crea uno desde el formulario inferior.
    </div>
    <ul v-else class="space-y-1">
      <li
        v-for="u in users"
        :key="u.id"
        @click="$emit('select', u.id)"
        class="px-2 py-1 rounded-lg text-[18px] cursor-pointer flex flex-col bg-slate-900/80 border border-slate-800 hover:border-sky-500 hover:bg-slate-900 transition"
        :class="u.id === selectedUserId ? 'border-sky-500 bg-slate-900' : ''"
      >
        <div class="flex justify-between gap-2">
          <span class="font-medium text-slate-100">{{ u.name }}</span>
          <span class="text-[13px] text-slate-500">#{{ u.id }}</span>
        </div>
        <span class="text-[16px] text-slate-400">{{ u.email }}</span>
      </li>
    </ul>
  </div>
</template>

<script setup>
defineProps({
  users: { type: Array, default: () => [] },
  selectedUserId: { type: Number, default: null },
  loading: { type: Boolean, default: false },
  error: { type: String, default: '' }
})
</script>
