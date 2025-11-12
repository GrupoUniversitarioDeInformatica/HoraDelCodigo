<template>
  <section class="space-y-4">
    <div class="flex items-center justify-between gap-2">
      <h2 class="text-2xl font-semibold text-slate-200">Comentarios del post</h2>
      <button
        class="text-[15px] px-2 py-1 rounded-full border border-slate-700 text-slate-400 hover:border-sky-500 hover:text-sky-300 transition"
        @click="loadComments"
      >
        Recargar
      </button>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-4">
      <!-- Listado -->
      <div class="lg:col-span-2 bg-slate-900/70 border border-slate-800 rounded-2xl p-4">
        <CommentsPanel
          :comments="comments"
          :selected-post-id="Number(filterPostId)"
          :loading="loading"
          :error="error"
        />
      </div>

      <!-- Formulario -->
      <div class="bg-slate-900/70 border border-slate-800 rounded-2xl p-4 space-y-2">
        <h3 class="text-xl font-semibold text-slate-200">Crear comentario</h3>
        <p class="text-[15px] text-slate-400">
          Conecta este formulario a <code>POST /api/comments</code>.
        </p>
        <form @submit.prevent="handleCreateComment" class="space-y-2">
          <input
            v-model.number="form.user_id"
            type="number"
            placeholder="user_id"
            class="w-full px-2 py-1 rounded-lg bg-slate-900 border border-slate-700 text-sm focus:outline-none focus:ring-1 focus:ring-sky-500"
          />
          <textarea
            v-model="form.content"
            rows="3"
            placeholder="Contenido"
            class="w-full px-2 py-1 rounded-lg bg-slate-900 border border-slate-700 text-sm focus:outline-none focus:ring-1 focus:ring-sky-500 resize-none"
          ></textarea>
          <button
            type="submit"
            class="w-full text-[16px] py-1 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white transition hover:cursor-pointer"
          >
            Crear comentario
          </button>
        </form>

        
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import CommentsPanel from '../components/CommentsPanel.vue'

const props = defineProps({
    postId: { type: Number, required: true }
});

const comments = ref([])
const loading = ref(false)
const error = ref('')
const form = ref({ post_id: props.postId, user_id: null, content: '' })
const filterPostId = ref(props.postId)

function loadComments() {
  loading.value = true
  error.value = ''
  // TODO: GET /api/comments (y opcionalmente ?post_id=)
  setTimeout(() => {
    comments.value = [
      { id: 1, post_id: 1, user_id: 2, content: 'Comentario demo 1' },
      { id: 2, post_id: 1, user_id: 3, content: 'Otro comentario demo' }
    ].filter(post => post.post_id == filterPostId.value)
    loading.value = false
  }, 200)
}

function handleCreateComment() {
  // TODO: POST /api/comments con form.value
  console.log('TODO: crear comentario vía API', form.value)
}

function applyFilter() {
  // TODO: GET /api/comments?post_id=filterPostId.value
  console.log('TODO: filtrar comentarios por post_id', filterPostId.value)
}

loadComments()
</script>
