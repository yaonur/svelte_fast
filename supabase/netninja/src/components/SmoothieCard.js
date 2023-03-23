const SmoothieCard=({smoothie})=>{
	return (
		<div className="smoothie-card">
			<h2>{smoothie.title}</h2>
			<p>{smoothie.metod}</p>
			<div className="rating">{smoothie.rating}</div>
		</div>
	)
}

export default SmoothieCard