import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load:PageServerLoad = (async ({locals}) => {
    if (locals.session && locals.session.user){
        redirect(303,"/login")
    }
    const user_id=locals.session.user.id
    console.log(user_id)
    const {data,error}  = await locals.sb
    .from('Todos')
    .select('*')

    return {
        todos:data,
        error:error
    };
})  