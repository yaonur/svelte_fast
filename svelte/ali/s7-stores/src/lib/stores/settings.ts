import { writable } from 'svelte/store';

function createSettings() {
	const defaultSettings = {
				colorScheme:"dark",
		language:"en",
		fontSize:12,

	}
	const { subscribe, set, update } = writable({...defaultSettings})
	const reset = () => {
		set({...defaultSettings})
	}
	const updateSetting=(setting,value)=>{
			update((settings)=>{
				return {...settings,[setting]:value}
			})
		}

	const toggleColorScheme = () => {
		update((settings)=>{
			return {...settings,colorScheme:settings.colorScheme==="dark"?"light":"dark"}
		})
	}
	return {
		subscribe,
		set,
		update,
		updateSetting,
		toggleColorScheme,
		reset
	};
}

export const settings = createSettings();


