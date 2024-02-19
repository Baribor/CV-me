import { Link } from "react-router-dom";
import SEO from "../components/SEO";
import InputField from "../components/input/InputField";


const SignInPage = () => {

	return (
		<>
			<SEO title={"login"} />
			<div className="flex">
				<div className="flex items-center bg-primary_light w-1/2 bg-[url('login.svg')] h-[calc(100vh-56px)] bg-no-repeat" />
				<div className="flex-grow">
					<div className="flex flex-col mt-20 h-full px-10 gap-2">
						<h1 className="font-bold text-primary text-3xl">LOGIN</h1>
						<InputField label={"Email"} type="email" name="email" placeHolder="Enter your email" />
						<InputField label={"Password"} type="password" name="password" placeHolder="Enter your password" />
						<Link to={"/forgot-password"} className="text-primary cursor-pointer text-sm self-end my-2 font-semibold">
							<span>Forgot password?</span>
						</Link>
						<button className="bg-primary text-white py-2 rounded-lg">LOGIN</button>
						<p className="my-2">Don&apos;t have an acount?
							<Link to={"/signup"}><span className="text-primary cursor-pointer text-sm self-end font-bold"> Sign up</span>
							</Link> </p>

					</div>
				</div>
			</div>
		</>
	)
}

export default SignInPage;