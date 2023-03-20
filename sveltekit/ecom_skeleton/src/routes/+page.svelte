<script lang="ts">
import ProductCard from "../lib/ProductCard.svelte";

const products=[

]
</script>

<div class="container h-full mx-auto flex justify-center items-center">
  <div class="grid grid-cols-3 gap-4">
    <div class="col-span-3">
      <h1>Sveltik store</h1>
    </div>
      <ProductCard></ProductCard>
    <div class="col-span-3">
      <button class="btn variant-filled-primary">Checkout with Stripe Api</button>
    </div>
  </div>
</div>
