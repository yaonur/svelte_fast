import { error, redirect } from "@sveltejs/kit"
import type {RequestHandler} from "./$types"

export const POST:RequestHandler=async({locals})=>{
	const {error:err} =await locals.sb.auth.signOut()
	if (err){
		throw error(500,"something went wrong logging you out")
	}
	return redirect(303,"/")
}