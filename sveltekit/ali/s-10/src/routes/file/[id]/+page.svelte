<script lang="ts">
	import { page } from '$app/stores';

	console.log($page);
</script>

{JSON.stringify($page.params, null, 2)}
