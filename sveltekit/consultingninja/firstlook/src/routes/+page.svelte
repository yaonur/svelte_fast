<script lang="ts">
  import SlottedComponent from "../lib/SlottedComponent.svelte";
  
  const item = { name: "item", value: 1 };
</script>

<SlottedComponent {item}>
  <h1 slot="slotOne" let:prop={passedBack}>Home page on slotOne item name:{passedBack.name}</h1>
</SlottedComponent>
