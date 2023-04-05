import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load = (async (event) => {
    console.log("login page.server-------------->")
    const {data,error}=await event.locals.supabase.auth.signInWithPassword(
        {        email: 'ya_onur@hotmail.com',
        password: '123123'}
    )
    console.log("login page.server-------------->")
    console.log("error>")
    console.log(error)
    console.log("data>")
    console.log(data)
    console.log("login page.server success-------------->")
    redirect(303,'/')
    return {};
}) satisfies PageServerLoad;