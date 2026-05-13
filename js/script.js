/*****************************************************************************************************************************************************************************/
/*                                                                                                                                                                           */
/*                                                                  Scripts para el Proyecto SoccerCards                                                                     */
/*                                                                                                                                                                           */
/*****************************************************************************************************************************************************************************/
/*                                                                                                                                                                           */
/* Autor: Magallanes López Carlos Gabriel                                                                                                                                    */
/* Versión del Proyecto: 1.0                                                                                                                                                 */
/* Correo: cgmagallanes23@gmail.com                                                                                                                                          */
/* Ultima Modificación: 22/03/2026                                                                                                                                           */
/*                                                                                                                                                                           */
/*****************************************************************************************************************************************************************************/

// i18n - Traducciones
const translations = {
    es: {
        // Nav
        navTeams:           "Equipos",
        navHowTo:           "Cómo Jugar",
        navDownload:        "Descargar",
        // Hero
        heroBadge:          "🏆 Edición Fútbol 2025",
        heroT1:             "El Memorama",
        heroT2:             "más Épico",
        heroT3:             "del Fútbol",
        heroDesc:           "Desafía tu memoria con los escudos de los mejores equipos del mundo. ¡Encuentra todos los pares y demuestra que eres un crack!",
        heroBtn1:           "⬇ Descargar Gratis",
        heroBtn2:           "¿Cómo Jugar?",
        // Teams
        teamsTag:           "⚽ Los 4 Equipos",
        teamsTitle:         "Conoce los <span>Equipos</span>",
        teamsDesc:          "Cuatro grandes clubes del fútbol mundial te esperan. ¿Puedes recordar dónde está cada uno?",
        team1Name:          "FC Barcelona",
        team1League:        "LaLiga · España",
        team2Name:          "Real Madrid CF",
        team2League:        "LaLiga · España",
        team3Name:          "Paris Saint-Germain",
        team3League:        "Ligue 1 · Francia",
        team4Name:          "Inter de Milán",
        team4League:        "Serie A · Italia",
        // How To Play
        howtoTag:           "🎮 Reglas",
        howtoTitle:         "¿Cómo <span>Jugar</span>?",
        howtoDesc:          "Simple, rápido y adictivo. En menos de un minuto estás jugando.",
        step1Title:         "Inicia el Juego",
        step1Desc:          "Haz clic en \"Iniciar Juego\" para mezclar las cartas y comenzar la partida.",
        step2Title:         "Voltea una Carta",
        step2Desc:          "Haz clic en cualquier carta para revelar qué equipo se esconde debajo.",
        step3Title:         "Encuentra el Par",
        step3Desc:          "Voltea una segunda carta. Si coinciden, ¡se quedan! Si no, se ocultan de nuevo.",
        step4Title:         "¡Gana!",
        step4Desc:          "Encuentra los 4 pares para ganar. El juego se reinicia automáticamente.",
        // Preview
        previewTag:         "📸 Vista Previa",
        previewTitle:       "Así se <span>Ve el Juego</span>",
        feat1Title:         "Cartas Aleatorias",
        feat1Desc:          "Las cartas se mezclan en cada partida para un desafío siempre nuevo.",
        feat2Title:         "Revelación Temporizada",
        feat2Desc:          "Las cartas sin par se ocultan después de 1 segundo. ¡Memoriza rápido!",
        feat3Title:         "Solo Clic del Mouse",
        feat3Desc:          "Controles simples e intuitivos. Solo haz clic para jugar.",
        feat4Title:         "Rejugabilidad Infinita",
        feat4Desc:          "Cada partida es diferente. El juego se reinicia al ganar automáticamente.",
        // Download
        dlTag:              "🆓 Gratis",
        dlTitle:            "¡Descárgalo <span>Ahora</span>!",
        dlDesc:             "Sin instalaciones, sin dependencias. Solo descarga y juega directo en Windows.",
        dlBtn:              "⬇ Descargar SoccerCards.exe",
        req1:               "🪟 Windows 7+",
        req2:               "💾 ~50 MB",
        req3:               "🧠 2 GB RAM",
        req4:               "⚡ Sin instalación",
        // Footer
        footerContact:      "Contacto",
        // Lang Button
        langBtn:            "🌐 English"
    },
    en: {
        // Nav
        navTeams:           "Teams",
        navHowTo:           "How to Play",
        navDownload:        "Download",
        // Hero
        heroBadge:          "🏆 Football Edition 2025",
        heroT1:             "The Most",
        heroT2:             "Epic",
        heroT3:             "Football Memory Game",
        heroDesc:           "Challenge your memory with the crests of the best clubs in the world. Find all the pairs and prove you're a legend!",
        heroBtn1:           "⬇ Download Free",
        heroBtn2:           "How to Play?",
        // Teams
        teamsTag:           "⚽ The 4 Teams",
        teamsTitle:         "Meet the <span>Teams</span>",
        teamsDesc:          "Four great football clubs from around the world await you. Can you remember where each one is?",
        team1Name:          "FC Barcelona",
        team1League:        "LaLiga · Spain",
        team2Name:          "Real Madrid CF",
        team2League:        "LaLiga · Spain",
        team3Name:          "Paris Saint-Germain",
        team3League:        "Ligue 1 · France",
        team4Name:          "Inter Milan",
        team4League:        "Serie A · Italy",
        // How To Play
        howtoTag:           "🎮 Rules",
        howtoTitle:         "How to <span>Play</span>?",
        howtoDesc:          "Simple, fast and addictive. In less than a minute you're already playing.",
        step1Title:         "Start the Game",
        step1Desc:          "Click \"Start Game\" to shuffle the cards and begin the match.",
        step2Title:         "Flip a Card",
        step2Desc:          "Click on any card to reveal which team is hiding underneath.",
        step3Title:         "Find the Pair",
        step3Desc:          "Flip a second card. If they match, they stay! If not, they get hidden again.",
        step4Title:         "Win!",
        step4Desc:          "Find all 4 pairs to win. The game restarts automatically.",
        // Preview
        previewTag:         "📸 Preview",
        previewTitle:       "See how the <span>Game Looks</span>",
        feat1Title:         "Random Cards",
        feat1Desc:          "Cards are shuffled every game for a constantly fresh challenge.",
        feat2Title:         "Timed Reveal",
        feat2Desc:          "Unmatched cards hide again after 1 second. Memorize fast!",
        feat3Title:         "Mouse Click Only",
        feat3Desc:          "Simple and intuitive controls. Just click to play.",
        feat4Title:         "Infinite Replayability",
        feat4Desc:          "Every game is different. The game restarts automatically when you win.",
        // Download
        dlTag:              "🆓 Free",
        dlTitle:            "Download <span>Now</span>!",
        dlDesc:             "No installations, no dependencies. Just download and play directly on Windows.",
        dlBtn:              "⬇ Download SoccerCards.exe",
        req1:               "🪟 Windows 7+",
        req2:               "💾 ~50 MB",
        req3:               "🧠 2 GB RAM",
        req4:               "⚡ No install",
        // Footer
        footerContact:      "Contact",
        // Lang Button
        langBtn:            "🌐 Español"
    }
};

// Detección y Aplicación de Idioma
function detectLanguage() {
    const saved = localStorage.getItem('lang');                                                  // Obtener el Lenguaje del Local Storage
    if (saved) return saved;                                                                     // Si se obtuvo el Lenguaje del Local Storage Retornar
    const browserLang = navigator.language || navigator.userLanguage;                            // Obtener el Lenguaje del Browser
    return browserLang.startsWith('es') ? 'es' : 'en';                                          // Español si es es-*, inglés para todo lo demás
}

// Aplicar Traducciones al DOM
function applyLanguage(lang) {
    const t = translations[lang];
    document.querySelectorAll('[data-i18n]').forEach(el => {                                     // Traducir Elementos con Texto Simple
        const key = el.getAttribute('data-i18n');
        if (t[key]) el.innerHTML = t[key];
    });
    document.querySelectorAll('[data-i18n-html]').forEach(el => {                                // Traducir Elementos con HTML Interno (spans de color)
        const key = el.getAttribute('data-i18n-html');
        if (t[key]) el.innerHTML = t[key];
    });
    document.documentElement.setAttribute('lang', lang);                                         // Actualizar Atributo lang del HTML para Accesibilidad
    const btn = document.getElementById('langToggleBtn');
    if (btn) btn.textContent = t.langBtn;
    localStorage.setItem('lang', lang);                                                          // Guardar Idioma Seleccionado en localStorage
}

// Crear Botón Flotante de Cambio de Idioma
function createLangButton() {
    const btn = document.createElement('button');                                                // Crear el Elemento
    btn.id = 'langToggleBtn';                                                                    // ID para Aplicar Estilos desde CSS
    btn.addEventListener('click', () => {                                                        // Agregar Callback para el Botón
        const current = localStorage.getItem('lang') || detectLanguage();                        // Obtener Lenguaje Actual
        const next = current === 'es' ? 'en' : 'es';                                            // Alternar entre Español e Inglés
        applyLanguage(next);                                                                     // Aplicar el Lenguaje
    });
    document.body.appendChild(btn);                                                              // Agregar Botón al Documento
}

// Efecto Fade In al hacer Scroll
const observer = new IntersectionObserver((entries) => {                                         // Instanciar Observador Intersección, Detección Elementos en Viewport
    entries.forEach(entry => {                                                                   // Para Cada Elemento Detectado en el Viewport
        if (entry.isIntersecting) {                                                              // Si esta en Viewport
            entry.target.classList.add('visible');                                               // Agregar Clase 'visible' para Efecto Fade In
            observer.unobserve(entry.target);                                                    // Dejar de Observar el Elemento para Mejorar Rendimiento
        }
    });
}, { threshold: 0.1 });                                                                          // Configuración del Observador: Activar cuando el 10% del Elemento sea Visible

// Observar Elementos de la Clase 'Fade-In' para Activar Efecto al Entrar en el Viewport
const fadeElements = document.querySelectorAll('.fade-in');                                      // Seleccionar Todos los Elementos con Clase 'fade-in'
fadeElements.forEach(element => observer.observe(element));                                      // Observar Cada Elemento para Activar Efecto Fade In al Entrar en el Viewport

// Inicialización
createLangButton();                                                                              // Creación del Botón del Lenguaje
applyLanguage(detectLanguage());                                                                 // Aplicación del Lenguaje

/*****************************************************************************************************************************************************************************/
