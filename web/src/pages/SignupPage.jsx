import { Link } from "react-router-dom";
import SEO from "../components/SEO";
import InputField from "../components/input/InputField";


const SignUpPage = () => {

	return (
		<>
			<SEO title={"signup"} />
			<div className="flex">
				<div className="flex items-center bg-primary_light w-1/2 bg-[url('signup.svg')] h-[calc(100vh-56px)] bg-no-repeat" />

				<div className="flex-grow">
					<div className="grid grid-cols-2 mt-20 px-10 gap-2">
						<h1 className="font-bold text-primary text-3xl self-center col-span-2">Sign up</h1>
						<InputField label={"First Name"} type="text" name="firstName" containerStyle="mr-2" />
						<InputField label={"Last Name"} type="text" name="lastName" containerStyle="" />
						<InputField label={"Email"} type="email" name="email" containerStyle="col-span-2" />
						<InputField label={"Username"} type="text" name="username" containerStyle="col-span-2" />
						<InputField label={"Password"} type="password" name="password" containerStyle="col-span-2" />
						<button className="bg-primary text-white py-2 rounded-lg col-span-2">Continue</button>
						<p className="my-2">Already have an acount? <Link to={"/signin"}><span className="text-primary cursor-pointer text-sm self-end font-bold">Login</span></Link></p>

					</div>

				</div>
			</div >
		</>
	)
}

export default SignUpPage;