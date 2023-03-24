import { supabase } from '$lib/supabase';
import { writable } from 'svelte/store';

export const content = writable([]);

export const loadContent = async () => {
	const { data, error } = await supabase.from('Share').select('*');
	if (error) {
		console.log('error', error);
	}
	if (data) {
		console.log(data);
		// @ts-ignore
		content.set(data);
	}
};
