<template>
  <section class="space-y-4">
    <h2 class="text-xl font-semibold text-slate-100">
      Dashboard
    </h2>
    <p class="text-base text-slate-300 max-w-2xl">
      Esta SPA está pensada para un taller de introducción a programación web full stack:
      frontend con Vue, backend con FastAPI y base de datos MariaDB/MySQL.
    </p>

    <ul class="text-base text-slate-300 list-disc ml-5 space-y-1">
      <li><strong>/users</strong>: gestión de usuarios.</li>
      <li><strong>/posts</strong>: publicaciones asociadas a usuarios.</li>
      <li><strong>/comments</strong>: comentarios ligados a posts y usuarios.</li>
    </ul>

    <p class="text-[14px] text-slate-500 max-w-xl">
      Cada vista tiene huecos marcados como
      <code class="text-sky-300">TODO</code> donde puedes conectar fácilmente con
      tu API REST (<code>/api/users</code>, <code>/api/posts</code>, <code>/api/comments</code>).
      Es una buena base para enseñar cómo el frontend habla con el backend.
    </p>
  </section>
</template>

<script setup>
</script>
