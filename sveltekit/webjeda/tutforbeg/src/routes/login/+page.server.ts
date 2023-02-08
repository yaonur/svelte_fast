import type { Actions } from '@sveltejs/kit';
import {redirect} from "@sveltejs/kit"

export const actions: Actions = {
    default: async ({ cookies, request }) => {
        const formData = await request.formData();
        const email = formData.get('email');
        const password = formData.get('password');
        if (email === 'someuser' && password == 'somepassword') {
            // console.log(formData);
            cookies.set('access', 'true', { path: '/', sameSite: 'strict' });
            throw redirect(302, '/dashboard');
        }
        return {error:"password or username is incorrect"}
    }
};
