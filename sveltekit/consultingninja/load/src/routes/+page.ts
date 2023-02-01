export async function load({ fetch }) {
  const fetchPersons = async () => {
    const resp = await fetch("http://randomuser.me/api/");
    const data = await resp.json();
    return {
      data
    };
  };
  return {
    users: fetchPersons()
  };
}
