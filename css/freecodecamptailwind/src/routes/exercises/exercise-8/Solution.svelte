<script lang="ts">
let items = [
    { title: "Full name", data: "Margot Foster" },
    { title: "Application for", data: "Backend Developer" },
    { title: "Email address", data: "margotfoster@example.com" },
    { title: "Salary expectation", data: "$120,000" },
    {
      title: "About",
      data:
        "Fugiat ipsum ipsum deserunt culpa aute sint do nostrud anim incididunt cillum culpa consequat. Excepteur qui ipsum aliquip consequat sint. Sit id mollit nulla mollit nostrud in ea officia proident. Irure nostrud pariatur mollit ad adipisicing reprehenderit deserunt qui eu."
    }
  ];
</script>
<div class="h-full p-8 bg-gray-50">
  
  <div class="overflow-hidden bg-white shadow lg:rounded-lg">
    <div class="px-4 py-5 border-b border-gray-200 lg:px-6">
      <h3 class="text-lg font-medium leading-6 text-gray-900">
        Applicant Information
      </h3>
      <p class="max-w-2xl mt-1 text-sm leading-5 text-gray-500">
        Personal details and application.
      </p>
    </div>
    <div class="px-4 py-5 lg:p-0">
      <dl>
        {#each items as item ,index}
          <div
            class="lg:grid lg:grid-cols-3 lg:gap-4 lg:px-6 lg:py-5"
            class:conditional={index==0}
          >
            <dt class="text-sm font-medium leading-5 text-gray-500">
              {item.title}
            </dt>
            <dd
              class="mt-1 text-sm leading-5 text-gray-900 lg:mt-0 lg:col-span-2"
            >
              {item.data}
            </dd>
          </div>
        {/each}
      </dl>
    </div>
  </div>
</div>
<style lang="postcss">
  .conditional {
    @apply mt-8 lg:mt-0 lg:border-t lg:border-gray-200;
  }
</style>