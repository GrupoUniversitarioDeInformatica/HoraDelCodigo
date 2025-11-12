<template>
  <div class="flex-1 overflow-y-auto space-y-2">
    <div v-if="!selectedPostId" class="text-[15px] text-slate-500">
      Selecciona un post para ver sus comentarios.
    </div>
    <div v-else-if="loading" class="text-[15px] text-slate-500">
      Cargando comentarios...
    </div>
    <div v-else-if="error" class="text-[15px] text-red-400">
      {{ error }}
    </div>
    <div v-else-if="selectedPostId && !comments.length" class="text-[15px] text-slate-500">
      No hay comentarios para este post todavía.
    </div>
    <ul v-else class="space-y-2">
      <li
        v-for="c in comments"
        :key="c.id"
        class="p-2 rounded-xl bg-slate-900/80 border border-slate-800"
      >
        <div class="flex justify-between items-center">
          <span class="text-[18px] text-sky-300">
            user #{{ c.user_id }}
          </span>
          <span class="text-[15px] text-slate-500">
            #{{ c.id }}
          </span>
        </div>
        <p class="mt-1 text-[16px] text-slate-200">
          {{ c.content }}
        </p>
      </li>
    </ul>
  </div>
</template>

<script setup>
defineProps({
  comments: { type: Array, default: () => [] },
  selectedPostId: { type: Number, default: null },
  loading: { type: Boolean, default: false },
  error: { type: String, default: '' }
})
</script>
