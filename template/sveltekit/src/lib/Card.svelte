<script lang="ts">
	import type { Card } from 'types';
	export let card: Card;
</script>

<div class="rounded overflow-hidden bg-white shadow-md">
	<img src="/img/{card.fileName}" alt={card.fileName} />
	<div>
		<span>{card.mealName}</span>
		<span>{card.ownerName}</span>
	</div>
</div>
