import { Link, useNavigate } from "react-router-dom";
import SEO from "../components/SEO";
import InputField from "../components/input/InputField";
import * as yup from "yup"
import { useFormik } from "formik";
import { useState } from "react";
import CircularProgress from '@mui/material/CircularProgress';
import Visibility from '@mui/icons-material/Visibility';
import VisibilityOff from '@mui/icons-material/VisibilityOff';
import IconButton from '@mui/material/IconButton';
import { enqueueSnackbar } from "notistack";

const validationSchema = yup.object({
	firstName: yup.string().required(),
	lastName: yup.string().required(),
	email: yup.string().email().required(),
	username: yup.string().required(),
	password: yup.string().required(),
})

const SignUpPage = () => {
	const navigate = useNavigate();
	const [showPassword, setShowPassword] = useState(false)

	const formik = useFormik({
		initialValues: {
			firstName: '',
			lastName: '',
			email: '',
			username: '',
			password: '',
		},
		validationSchema,
		onSubmit: (values, helper) => {
			setTimeout(() => {
				enqueueSnackbar({
					message: "Account creation successful",
					variant: "success"
				})
				setTimeout(() => navigate("/signin"), 1500);
			}, 5000)
		}
	})
	return (
		<>
			<SEO title={"signup"} />
			<div className="flex">
				<div className="hidden md:flex items-center bg-primary_light w-1/2 bg-[url('signup.svg')] h-[calc(100vh-56px)] bg-no-repeat bg-cover" />

				<div className="flex-grow">
					<div className="grid grid-cols-2 mt-20 px-10 gap-2">
						<h1 className="font-bold text-primary text-3xl self-center col-span-2 mb-4">Sign up</h1>
						<InputField label={"First Name"} type="text" name="firstName" containerStyle="mr-2 col-span-2 md:col-span-1"
							error={formik.touched.firstName && formik.errors.firstName}
							helperText={formik.touched.firstName && formik.errors.firstName}
							onChange={formik.handleChange}
							disabled={formik.isSubmitting} />
						<InputField label={"Last Name"} type="text" name="lastName"
							error={formik.touched.lastName && formik.errors.lastName}
							helperText={formik.touched.lastName && formik.errors.lastName}
							onChange={formik.handleChange}
							disabled={formik.isSubmitting}
							containerStyle="col-span-2 md:col-span-1" />
						<InputField label={"Email"} type="email" name="email" containerStyle="col-span-2"
							error={formik.touched.email && formik.errors.email}
							helperText={formik.touched.email && formik.errors.email}
							onChange={formik.handleChange}
							disabled={formik.isSubmitting} />
						<InputField label={"Username"} type="text" name="username" containerStyle="col-span-2"
							error={formik.touched.username && formik.errors.username}
							helperText={formik.touched.username && formik.errors.username}
							onChange={formik.handleChange}
							disabled={formik.isSubmitting} />
						<InputField label={"Password"} type={showPassword ? 'text' : 'password'} name="password"
							containerStyle="col-span-2"
							error={formik.touched.password && formik.errors.password}
							helperText={formik.touched.password && formik.errors.password}
							onChange={formik.handleChange}
							disabled={formik.isSubmitting}
						>
							<IconButton
								onClick={() => setShowPassword((c) => !c)}>
								{
									showPassword ? <VisibilityOff /> : <Visibility />
								}
							</IconButton>
						</InputField>
						<button className="bg-primary text-white py-2 rounded-lg col-span-2" onClick={formik.handleSubmit} disabled={formik.isSubmitting}>
							{
								formik.isSubmitting ? (<CircularProgress size='1.5rem' color="inherit" />) : 'Continue'
							}
						</button>
						<p className="my-2 text-sm text-gray-900">Already have an acount? <Link to={"/signin"}><span className="text-primary cursor-pointer text-sm self-end font-bold">Login</span></Link></p>

					</div>

				</div>
			</div >
		</>
	)
}

export default SignUpPage;