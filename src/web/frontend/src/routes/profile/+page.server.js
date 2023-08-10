export function load({ setHeaders }) {
	setHeaders({
        'Content-Security-Policy': 'https://stats.g.doubleclick.net'
	});
}