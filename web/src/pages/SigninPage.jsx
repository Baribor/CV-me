import SEO from "../components/SEO";


const SignInPage = () => {

	return (
		<>
			<SEO title={"login"} />
			<div className="flex">
				<div className="flex items-center bg-primary_light">
					< img src="login.svg" alt="" className="h-2/3" />
				</div >
				<div className="flex-grow">
					<div className="flex flex-col mt-20 h-full px-10">
						<h1 className="font-bold text-primary text-3xl self-center">LOGIN</h1>
						<label htmlFor="email">Email</label>
						<input type="email" name="email" id="" className="border-primary border h-10 rounded-lg focus:border-2 px-2 select-none outline-none" />
						<label htmlFor="password">Password</label>
						<input type="password" name="password" id="" className="border-primary border h-10 rounded-lg focus:border-2 px-2 select-none outline-none" />
						<span className="text-primary cursor-pointer text-sm self-end my-2">Forgot password?</span>
						<button className="bg-primary text-white py-2 rounded-lg">LOGIN</button>
						<p className="my-2">Don&apos;t have an acount? <span className="text-primary cursor-pointer text-sm self-end ">Sign up</span></p>

					</div>
				</div>
			</div>
		</>
	)
}

export default SignInPage;