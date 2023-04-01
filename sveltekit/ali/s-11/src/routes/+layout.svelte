    <script>
      import "../app.css";
    </script>

    <nav class="bg-slate-200 p-1">
      <a href="/">Home</a>
      <a href="/products">Products</a>
    </nav>
    
    <slot />

    <style lang="postcss"> 
    a{
      @apply text-slate-600 border-gray-600 border px-1 bg-slate-100;
    }
    </style>
