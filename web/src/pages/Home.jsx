

const HomePage = () => {

	return (
		<>
			<div className="flex gap-10">
				<div>
					<img src="hero.svg" alt="" />
				</div>
				<div className="flex flex-col justify-center">
					<h1 className="font-bold text-4xl text-primary_text">Create your CV like a pro using our CV builder</h1>

					<button className="bg-primary text-white px-4 py-2 rounded-lg active:scale-[.98] w-fit self-center">BUILD MY CV NOW</button>
				</div>
			</div>
		</>
	)
}

export default HomePage;