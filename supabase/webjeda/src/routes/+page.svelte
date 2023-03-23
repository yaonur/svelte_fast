<script>
	import  supabase  from '../config/supabase';

  let email = 'ya_onur@hotmail.com';
  let password="123123"
	// your script goes here
  async function signUp() {
    let { data, error } = await supabase.auth.signUp({
  email: email,
  password: password
})
  console.log (data)
  console.log(error)
}
	async function signInWithEmail() {
    let resp = await supabase.auth.signInWithPassword({
  email: email,
  password: password
})
  console.log (resp.data)
}
const getTodos = async () => {
  const { data, error } = await supabase
    .from('todo')
    .select('*')
  console.log(data)
  console.log(error)
}
const logUser=async ()=>{

let { data, error } = await supabase.auth.getUser(email)
console.log(data)

}
</script>

<input type="text" bind:value={email}>
<input type="text" bind:value={password}>
<button on:click={signInWithEmail}>Login</button>
<button on:click={signUp}>SignUp</button>
<button on:click={getTodos}>Get todos</button>
<button on:click={logUser}>Log user</button>