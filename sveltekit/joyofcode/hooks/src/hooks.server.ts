import type { Handle, HandleServerError } from "@sveltejs/kit";
import { sequence } from "@sveltejs/kit/hooks";

const auth:Handle=async({event,resolve})=>{
	console.log('auth hook runned')
	return resolve(event)
}
const i18n:Handle=async({event,resolve})=>{
	console.log('i18n hook runned')
	return resolve(event)
}
export const handle:Handle=sequence(auth,i18n)

// export const handle: Handle = async ({ event, resolve }) => {
// 	// event.cookies.set('session', 'banana')
// 	// const session = event.cookies.get('session', )
// 	// console.log(session)
// 	event.locals.user="Test"
// 	const locale='tr'
// 	event.locals.locale=locale
//
//
// 	if (event.url.pathname.startsWith('/banana')) return new Response('banana !!')
// 	else return resolve(event, {
// 		transformPageChunk:({html})=>html.replace("%lang%",locale)
// 	});
// };
//
export const handleError:HandleServerError=async({error,event})=>{
	console.log(error)
	return { message:"Yikes! 💩"}
}