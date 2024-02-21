import { Link, useNavigate } from "react-router-dom";
import SEO from "../components/SEO";
import InputField from "../components/input/InputField";
import * as yup from "yup";
import { useFormik } from "formik"
import CircularProgress from '@mui/material/CircularProgress';
import Visibility from '@mui/icons-material/Visibility';
import VisibilityOff from '@mui/icons-material/VisibilityOff';
import IconButton from '@mui/material/IconButton';
import { useState } from "react";

const validationSchema = yup.object({
	email: yup.string().email().required(),
	password: yup.string().required()
})

const SignInPage = () => {
	const navigate = useNavigate();
	const [showPassword, setShowPassword] = useState(false)

	const formik = useFormik({
		initialValues: {
			email: '',
			password: '',
		},
		validationSchema,
		onSubmit: (values, helpers) => {
			console.log('submitting now');

			setTimeout(() => {
				navigate("/dashboard")
			}, 5000)
		}
	})
	return (
		<>
			<SEO title={"login"} />
			<div className="flex">
				<div className="hidden md:flex items-center bg-primary_light w-1/2 bg-[url('login.svg')] h-[calc(100vh-56px)] bg-no-repeat bg-cover" />
				<div className="flex-grow">
					<div className="flex flex-col mt-20 h-full px-10 gap-2">
						<h1 className="font-bold text-primary text-3xl">LOGIN</h1>
						<InputField label={"Email"} type="email" name="email" disabled={formik.isSubmitting}
							error={formik.touched.email && formik.errors.email}
							helperText={formik.touched.email && formik.errors.email}
							onChange={formik.handleChange}
						/>
						<InputField label={"Password"} type={showPassword ? 'text' : 'password'} name="password" disabled={formik.isSubmitting}
							error={formik.touched.password && formik.errors.password}
							helperText={formik.touched.password && formik.errors.password}
							onChange={formik.handleChange}
						>
							<IconButton
								onClick={() => setShowPassword((c) => !c)}>
								{
									showPassword ? <VisibilityOff /> : <Visibility />
								}
							</IconButton>
						</InputField>
						<Link to={"/forgot-password"} className="text-primary cursor-pointer text-sm self-end my-2 font-semibold">
							<span>Forgot password?</span>
						</Link>
						<button className="bg-primary text-white py-2 rounded-lg uppercase h-12" onClick={formik.handleSubmit} disabled={formik.isSubmitting}>
							{
								formik.isSubmitting ? (<CircularProgress size='1.5rem' color="inherit" />) : 'Submit'
							}
						</button>
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