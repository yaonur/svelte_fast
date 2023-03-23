<script lang="ts">
	import { goto } from '$app/navigation';
	import { supabase } from '../../supabase';
	import type { PageData } from './$types';
    
    let email: string="ya_onur@hotmail.com";
    let password:string="123123"
    

	const signIn = async () => {
		const { data, error } = await supabase.auth.signInWithPassword({
            email,
            password
			
		});
        if(error) {
            console.log(error);
        } else{
            console.log(data)
            goto("/admin")
        }
	};

</script>

<form action="" on:submit|preventDefault={signIn}>
    <label for="email">Email</label>
    <input type="text" placeholder="email" id="email" bind:value={email}>
    <label for="password">Password</label>
    <input type="password" placeholder="password" id="password" bind:value={password}>
    <button >Login</button>
</form>