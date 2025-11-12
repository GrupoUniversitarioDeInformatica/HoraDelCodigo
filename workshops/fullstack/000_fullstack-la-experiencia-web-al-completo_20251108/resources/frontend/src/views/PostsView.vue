<template>
  <section class="space-y-4" v-if="$route.name == 'posts'">
    <div class="flex items-center justify-between gap-2">
      <h2 class="text-2xl font-semibold text-slate-200">Posts</h2>
      <div class="flex gap-2">
        <button
          class="text-[15px] px-2 py-1 rounded-full border border-slate-700 text-slate-400 hover:border-sky-500 hover:text-sky-300 transition"
          @click="loadPosts"
        >
          Recargar
        </button>
      </div>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-4">
      <!-- Listado -->
      <div class="lg:col-span-2 bg-slate-900/70 border border-slate-800 rounded-2xl p-4">
        <PostsPanel
          :posts="posts"
          :selected-post-id="Number(selectedPostId)"
          :loading="loading"
          :error="error"
          @select="selectPost"
        />
      </div>

      <!-- Formulario -->
      <div class="bg-slate-900/70 border border-slate-800 rounded-2xl p-4 space-y-2">
        <h3 class="text-2xl font-semibold text-slate-200">Crear post</h3>
        <p class="text-[12px] text-slate-400">
          Usa un <code>user_id</code> existente. Conecta este formulario a
          <code>POST /api/posts</code>.
        </p>
        <form @submit.prevent="handleCreatePost" class="space-y-2">
          <input
            v-model.number="form.user_id"
            type="number"
            placeholder="user_id"
            class="w-full px-2 py-1 rounded-lg bg-slate-900 border border-slate-700 text-sm focus:outline-none focus:ring-1 focus:ring-sky-500"
          />
          <input
            v-model="form.title"
            type="text"
            placeholder="Título"
            class="w-full px-2 py-1 rounded-lg bg-slate-900 border border-slate-700 text-sm focus:outline-none focus:ring-1 focus:ring-sky-500"
          />
          <textarea
            v-model="form.body"
            rows="3"
            placeholder="Contenido"
            class="w-full px-2 py-1 rounded-lg bg-slate-900 border border-slate-700 text-sm focus:outline-none focus:ring-1 focus:ring-sky-500 resize-none"
          ></textarea>
          <button
            type="submit"
            class="w-full text-[15px] py-1 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white transition"
          >
            Crear post
          </button>
        </form>

        <div v-if="selectedPostId" class="mt-3 text-[13px] text-slate-400">
          Post seleccionado: <span class="text-sky-300">#{{ selectedPostId }}</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import PostsPanel from '@/components/PostsPanel.vue'
import { useRouter } from 'vue-router';

const posts = ref([])
const selectedPostId = ref(null)
const loading = ref(false)
const error = ref('')
const form = ref({ user_id: null, title: '', body: '' })

const router = useRouter();

function loadPosts() {
  loading.value = true;
  error.value = '';
  // TODO: GET /api/posts
  setTimeout(() => {
    posts.value = [
      { id: 1, user_id: 1, title: 'Primer post', body: 'Contenido de ejemplo' },
      { id: 2, user_id: 2, title: 'Hola mundo', body: 'Más contenido' }
    ]
    loading.value = false
  }, 200)
}

function selectPost(id) {
  selectedPostId.value = id
  router.push({ name: 'comments', params: { postId: Number(selectedPostId.value) }});
}

function handleCreatePost() {
  // TODO: POST /api/posts con form.value
  console.log('TODO: crear post vía API', form.value)
}

loadPosts()
</script>
