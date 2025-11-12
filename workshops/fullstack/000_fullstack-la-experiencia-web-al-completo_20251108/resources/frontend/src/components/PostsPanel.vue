<template>
  <div class="flex-1 overflow-y-auto space-y-2">
    <div v-if="loading" class="text-[15px] text-slate-500">Cargando posts...</div>
    <div v-else-if="error" class="text-[15px] text-red-400">{{ error }}</div>
    <div v-else-if="!posts.length" class="text-[15px] text-slate-500">
      No hay posts. Crea uno usando el formulario inferior.
    </div>
    <ul v-else class="space-y-2">
      <li
        v-for="p in posts"
        :key="p.id"
        @click="$emit('select', p.id)"
        class="p-3 rounded-xl bg-slate-900/80 border border-slate-800 hover:border-sky-500 hover:bg-slate-900 transition cursor-pointer"
        :class="p.id === selectedPostId ? 'border-sky-500 bg-slate-900' : ''"
      >
        <div class="flex justify-between items-center">
          <h3 class="text-lg font-semibold text-slate-100">
            {{ p.title }}
          </h3>
          <span class="text-[12px] text-slate-500">
            by #{{ p.user_id }} · #{{ p.id }}
          </span>
        </div>
        <p class="mt-1 text-[14px] text-slate-300 line-clamp-3">
          {{ p.body }}
        </p>
      </li>
    </ul>
  </div>
</template>

<script setup>
defineProps({
  posts: { type: Array, default: () => [] },
  selectedPostId: { type: Number, default: null },
  loading: { type: Boolean, default: false },
  error: { type: String, default: '' }
})
</script>
