<script lang=ts>
	import  supabase  from '$lib/utils/supabase';

  let email = 'ya_onur@hotmail.com';
  let password="123123"
  let user_id=""
	// your script goes here
 
const getTodos = async () => {
  const { data, error } = await supabase
    .from('todos')
    .select('*')
  console.log(data)
  console.log(error)
}
const logUser=async ()=>{

let { data, error } = await supabase.auth.getUser()
if(data!.user){
	console.log(data)
	user_id=data.user.id
}

}
</script>


<button on:click={getTodos}>Get todos</button>
<button on:click={logUser}>Log user</button>
<br>
<h2>Current user id is:</h2>
<h2>{user_id}</h2>