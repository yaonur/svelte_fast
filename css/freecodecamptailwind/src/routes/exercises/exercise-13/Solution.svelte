<script lang="ts">
  let isOpen = false;
  let links = [
    "Dashboard",
    "Team",
    "Projects",
    "Calendar",
    "Reports"
  ];
  
  function toggleIsOpen() {
    isOpen = !isOpen;
  }
</script>
<div class="min-h-screen bg-white">
  <nav class="bg-white border-b border-gray-200">
    <div class="px-4 mx-auto max-w-7xl md:px-6 lg:px-8">
      <div class="flex justify-between h-16">
        <div class="flex">
          <!-- Desktop menu -->
          <div class="hidden -ml-8 md:-my-px md:flex">
            {#each links as link}
              <a
                href="#"
                class="inline-flex items-center px-1 pt-1 ml-8 text-sm font-medium leading-5 text-gray-500 transition duration-150 ease-in-out border-b-2 border-transparent hover:text-gray-700 hover:border-gray-300 focus:outline-none focus:text-gray-700 focus:border-gray-300"
              >
                {link}
              </a>
            {/each}
          </div>
        </div>
        
        <div class="flex items-center -mr-2 md:hidden">
          <button
            class="inline-flex items-center justify-center p-2 text-gray-400 transition duration-150 ease-in-out rounded-md hover:text-gray-500 hover:bg-gray-100 focus:outline-none focus:bg-gray-100 focus:text-gray-500"
            on:click={toggleIsOpen}
          >
            <svg
              class="w-6 h-6"
              stroke="currentColor"
              fill="none"
              viewBox="0 0 24 24"
            >
              <path
                class:hidden:inline-flex={isOpen}
                
                
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M4 6h16M4 12h16M4 18h16"
              ></path>
              <path
                class:hidden:inline-flex={isOpen}
                
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M6 18L18 6M6 6l12 12"
              ></path>
            </svg>
          </button>
        </div>
      </div>
    </div>
    <!-- Mobile menu -->
    <div class:hidden:block={isOpen}>
      <div class="pt-2 pb-3">
        {#each links as link}
          <a
            href="{link}"
            class="block py-2 pl-3 pr-4 mt-1 text-base font-medium text-gray-600 transition duration-150 ease-in-out border-l-4 border-transparent hover:text-gray-800 hover:bg-gray-50 hover:border-gray-300 focus:outline-none focus:text-gray-800 focus:bg-gray-50 focus:border-gray-300"
          >
            {link}
          </a>
        {/each}
      </div>
    </div>
  </nav>
  
  <div class="py-10">
    <header>
      <div class="px-4 mx-auto max-w-7xl md:px-6 lg:px-8">
        <h1 class="text-3xl font-bold leading-tight text-gray-900">
          Dashboard
        </h1>
      </div>
    </header>
    <main>
      <div class="mx-auto max-w-7xl md:px-6 lg:px-8">
        <div class="px-4 py-8 md:px-0">
          <div
            class="border-4 border-gray-200 border-dashed rounded-lg h-96"
          ></div>
        </div>
      </div>
    </main>
  </div>
</div>