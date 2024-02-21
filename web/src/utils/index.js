import { BASE_URL, TOKEN_KEY } from "./constants";

export const getFullUrl = (endpoint) => BASE_URL + endpoint;

export const makeAPIRequest = async ({
	path,
	method = "GET",
	body,
	headers,
}) => {
	const token = localStorage.getItem(TOKEN_KEY);

	const payload = {
		method,
		headers: headers ?? {
			Authorization: `Bearer ${token}`,
		},
	};

	if (body) {
		payload.headers["Content-type"] = "application/json";
		payload.body = JSON.stringify(body);
	}

	try {
		const res = await fetch(getFullUrl(path), payload);

		if (res.status === 401) {
			/* If token has expired. Redirect to home page */
			localStorage.removeItem(TOKEN_KEY);
			window.location.replace("/auth/login");
		} else {
			const data = await res.json();
			return data;
		}
	} catch (error) {
		return {
			status: false,
			message: "Connection error",
		};
	}
};