import { createClient } from "@supabase/supabase-js";
import {
	PUBLIC_SUPABASE_ANON_KEY,
	PUBLIC_SUPABASE_URL
  } from '$env/static/public';

const supabaseUrl: any = PUBLIC_SUPABASE_URL;
const supabaseKey: any = PUBLIC_SUPABASE_ANON_KEY;
const supabase = createClient(supabaseUrl, supabaseKey);

export default supabase;