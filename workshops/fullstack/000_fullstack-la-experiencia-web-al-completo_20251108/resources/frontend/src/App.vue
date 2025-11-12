<template>
  <div class="min-h-screen flex flex-col bg-slate-950 text-slate-100">
    <!-- Topbar -->
    <header class="border-b border-slate-800 bg-slate-900/70 backdrop-blur">
      <div class="mx-auto max-w-7xl px-4 py-4 flex items-center justify-between gap-4">
        <h1 class="text-2xl font-semibold text-sky-400">
          Full Stack Workshop
        </h1>
        <div class="flex flex-wrap gap-2 text-[15px] text-slate-400">
          <span>Frontend: Vue 3 + Vite + Tailwind</span>
          <span>Backend: FastAPI</span>
          <span>API base: <code class="text-sky-300">/api</code></span>
        </div>
      </div>
    </header>

    <!-- Nav -->
    <nav class="bg-slate-900/80 border-b border-slate-800">
      <div class="mx-auto max-w-7xl px-4 py-2 flex gap-3 text-[16px]">
        <RouterLink
          to="/"
          class="px-3 py-1 rounded-full border border-transparent text-slate-400 hover:text-sky-300 hover:border-sky-600 transition"
          active-class="bg-sky-600/20 text-sky-300 border-sky-600"
          exact
        >
          Dashboard
        </RouterLink>
        <RouterLink
          to="/users"
          class="px-3 py-1 rounded-full border border-transparent text-slate-400 hover:text-sky-300 hover:border-sky-600 transition"
          active-class="bg-sky-600/20 text-sky-300 border-sky-600"
        >
          Usuarios
        </RouterLink>
        <RouterLink
          to="/posts"
          class="px-3 py-1 rounded-full border border-transparent text-slate-400 hover:text-sky-300 hover:border-sky-600 transition"
          active-class="bg-sky-600/20 text-sky-300 border-sky-600"
        >
          Posts
        </RouterLink>
      </div>
    </nav>

    <!-- Contenido -->
    <main class="flex-1 mx-auto max-w-7xl w-full px-4 py-6">
      <RouterView :postId="Number($route.params.postId)"/>
    </main>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>
