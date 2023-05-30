import { writable } from 'svelte/store';
import type { ColapseContext,  AccordionOptions,  ActiveId, ActiveIdContext} from './types';
import { getContext, setContext } from 'svelte';
const activeCompenentId= writable<ActiveId>(null);

export function setAccordionOptions( {colapse}:AccordionOptions){
	setContext<ColapseContext>('colapse',colapse)
	setContext<ActiveIdContext>('active',activeCompenentId)
}

export function getAccordionOptions(){
	const colapse=getContext<ColapseContext>('colapse')
	const activeComponentId=getContext<ActiveIdContext>('active')
	return {colapse,activeComponentId}
}