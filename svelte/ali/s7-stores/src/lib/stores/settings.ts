import { writable } from 'svelte/store';

function createSettings() {
	const { subscribe, set, update } = writable(0);

	return {
		subscribe,
	};
}

export const settings = createSettings();

