document.addEventListener('DOMContentLoaded', function () {
    const authButtonsContainer = document.getElementById('auth-buttons-container');
    const container = document.getElementById("auth-buttons");
    const signupUrl = container.dataset.signupUrl;
    // Estado inicial (no autenticado)
    let isAuthenticated = false;

    // Función para renderizar los botones según el estado de autenticación
    function renderAuthButtons() {
        // Limpiar el contenedor
        authButtonsContainer.innerHTML = '';

        if (!isAuthenticated) {
            // Botones para usuario NO autenticado (Login y Signup)
            authButtonsContainer.innerHTML = `
                        <a href="#" id="login-button" class="inline-flex items-center justify-center w-9 h-9 rounded-full border border-goodbudget text-goodbudget hover:bg-green-50" title="Iniciar sesión">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 9V5.25A2.25 2.25 0 0013.5 3h-6a2.25 2.25 0 00-2.25 2.25v13.5A2.25 2.25 0 007.5 21h6a2.25 2.25 0 002.25-2.25V15m3 0l3-3m0 0l-3-3m3 3H9" />
                            </svg>
                        </a>
                        <a href="${signupUrl}" id="signup-button" class="inline-flex items-center justify-center w-9 h-9 rounded-full bg-goodbudget text-white hover:bg-goodbudget-dark" title="Registrarse">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M19 7.5v3m0 0v3m0-3h3m-3 0h-3m-2.25-4.125a3.375 3.375 0 11-6.75 0 3.375 3.375 0 016.75 0zM4 19.235v-.11a6.375 6.375 0 0112.75 0v.109A12.318 12.318 0 0110.374 21c-2.331 0-4.512-.645-6.374-1.766z" />
                            </svg>
                        </a>
                    `;

            // Agregar evento al botón de login
            document.getElementById('login-button').addEventListener('click', function (e) {
                e.preventDefault();
                // Simular inicio de sesión exitoso
                isAuthenticated = true;
                renderAuthButtons();
                console.log('Usuario ha iniciado sesión');
            });

        } else {
            // Botón para usuario autenticado (Logout)
            authButtonsContainer.innerHTML = `
                        <div class="flex items-center">
                            <span class="text-sm text-gray-600 mr-2 hidden sm:inline">Usuario</span>
                            <a href="#" id="logout-button" class="inline-flex items-center justify-center w-9 h-9 rounded-full border border-goodbudget text-goodbudget hover:bg-green-50" title="Cerrar sesión">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 9V5.25A2.25 2.25 0 0013.5 3h-6a2.25 2.25 0 00-2.25 2.25v13.5A2.25 2.25 0 007.5 21h6a2.25 2.25 0 002.25-2.25V15M12 9l-3 3m0 0l3 3m-3-3h12.75" />
                                </svg>
                            </a>
                        </div>
                    `;

            // Agregar evento al botón de logout
            document.getElementById('logout-button').addEventListener('click', function (e) {
                e.preventDefault();
                // Simular cierre de sesión
                isAuthenticated = false;
                renderAuthButtons();
                console.log('Usuario ha cerrado sesión');
            });
        }
    }

    // Renderizar los botones inicialmente
    renderAuthButtons();
});