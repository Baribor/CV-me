import { Link } from "react-router-dom"


const NavBar = () => {

	return (
		<nav className="h-[56px] bg-black text-white flex justify-between items-center px-4">
			{/* Logo */}
			<div>
				<Link to="/">
					<span className="text-primary font-extrabold font-[cursive] text-3xl">CV ME</span>
				</Link>
			</div>

			{/* Navs */}
			<div>
				<ul className="flex gap-4 items-center">
					<li>
						<Link to="contact-us" className="hover:text-blue-400">
							Contact us
						</Link>
					</li>
					<li>
						<Link to="signin">
							<button className="bg-white text-black px-4 rounded-md py-1 active:scale-95">Sign in</button>
						</Link>
					</li>
				</ul>
			</div>
		</nav>
	)
}

export default NavBar;