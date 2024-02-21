import SEO from "../components/SEO";
import InputField from "../components/input/InputField";


const ForgotPasswordPage = () => {

	return (
		<>
			<SEO title={"forgot password"} />
			<div className="flex">
				<div className="hidden md:flex items-center bg-primary_light w-1/2 bg-[url('forgotpassword.svg')] h-[calc(100vh-56px)] bg-no-repeat bg-cover" />
				<div className="flex-grow">
					<div className="flex flex-col mt-20 h-full px-10 gap-4">
						<div>
							<h1 className="font-bold text-primary text-3xl">Forgot password?</h1>
							<span className="text-sm text-gray-800">No worries, we&apos;ll send you reset instructions.</span>
						</div>
						<InputField label={"Email"} type="email" name="email" />
						<button className="bg-primary text-white py-2 rounded-lg">Reset Password</button>
					</div>
				</div>
			</div>
		</>
	)
}

export default ForgotPasswordPage;