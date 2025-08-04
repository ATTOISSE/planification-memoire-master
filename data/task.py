taches = [
        # PHASE 1: RECHERCHE & CONCEPTION
        {
            "id": 1, "phase": "PHASE 1 : RECHERCHE & CONCEPTION", "semaine": "Semaine 1 : 5-11 Août",
            "titre": "🔍 Recherche bibliographique intensive", "duree": "5 jours",
            "description": "Collecter et analyser la littérature sur les LLM éducatifs, l'orientation scolaire et le contexte africain",
            "objectif": "50+ articles pertinents identifiés", "outils": ["Semantic Scholar", "Perplexity", "Zotero", "ChatGPT"],
            "statut": "en_attente", "date_debut": "2025-08-05", "date_fin": "2025-08-09"
        },
        {
            "id": 2, "phase": "PHASE 1 : RECHERCHE & CONCEPTION", "semaine": "Semaine 1 : 5-11 Août",
            "titre": "🇸🇳 Analyse du système éducatif sénégalais", "duree": "2 jours",
            "description": "Cartographier les universités, formations disponibles, et processus d'orientation actuels",
            "objectif": "Base de données complète des formations", "outils": ["Web Scraping", "Google Sheets", "ANSD Data"],
            "statut": "en_attente", "date_debut": "2025-08-10", "date_fin": "2025-08-11"
        },
        {
            "id": 3, "phase": "PHASE 1 : RECHERCHE & CONCEPTION", "semaine": "Semaine 2 : 12-18 Août",
            "titre": "🏗️ Conception architecture technique", "duree": "4 jours",
            "description": "Définir l'architecture système, choix technologiques et modèle de données",
            "objectif": "Architecture complète documentée", "outils": ["Figma", "Draw.io", "Notion"],
            "statut": "en_attente", "date_debut": "2025-08-12", "date_fin": "2025-08-15"
        },
        {
            "id": 4, "phase": "PHASE 1 : RECHERCHE & CONCEPTION", "semaine": "Semaine 2 : 12-18 Août",
            "titre": "📊 Collecte des données éducatives", "duree": "3 jours",
            "description": "Rassembler données sur formations, débouchés, témoignages d'étudiants",
            "objectif": "Dataset de 1000+ formations", "outils": ["Python/Scrapy", "Pandas", "APIs"],
            "statut": "en_attente", "date_debut": "2025-08-16", "date_fin": "2025-08-18"
        },
        {
            "id": 5, "phase": "PHASE 1 : RECHERCHE & CONCEPTION", "semaine": "Semaine 3 : 19-25 Août",
            "titre": "🤖 Sélection et configuration du modèle LLM", "duree": "4 jours",
            "description": "Évaluer différents modèles (GPT-4, Claude, Llama) pour le contexte sénégalais",
            "objectif": "Modèle optimal sélectionné", "outils": ["Hugging Face", "OpenAI API", "Anthropic API", "MLflow"],
            "statut": "en_attente", "date_debut": "2025-08-19", "date_fin": "2025-08-22"
        },
        {
            "id": 6, "phase": "PHASE 1 : RECHERCHE & CONCEPTION", "semaine": "Semaine 3 : 19-25 Août",
            "titre": "📝 Préparation corpus d'entraînement", "duree": "3 jours",
            "description": "Nettoyer, structurer et annoter les données pour le fine-tuning",
            "objectif": "Corpus de 10K+ exemples", "outils": ["Label Studio", "spaCy", "NLTK"],
            "statut": "en_attente", "date_debut": "2025-08-23", "date_fin": "2025-08-25"
        },
        {
            "id": 7, "phase": "PHASE 1 : RECHERCHE & CONCEPTION", "semaine": "Semaine 4 : 26 Août - 1 Sept",
            "titre": "🎨 Design UX/UI de la plateforme", "duree": "4 jours",
            "description": "Créer wireframes, maquettes et prototypes interactifs",
            "objectif": "Prototype navigable complet", "outils": ["Figma", "Framer", "Adobe XD"],
            "statut": "en_attente", "date_debut": "2025-08-26", "date_fin": "2025-08-29"
        },
        {
            "id": 8, "phase": "PHASE 1 : RECHERCHE & CONCEPTION", "semaine": "Semaine 4 : 26 Août - 1 Sept",
            "titre": "📋 Finalisation cahier des charges", "duree": "3 jours",
            "description": "Documenter spécifications techniques, fonctionnelles et contraintes",
            "objectif": "Document technique complet", "outils": ["Notion", "GitBook", "Confluence"],
            "statut": "en_attente", "date_debut": "2025-08-30", "date_fin": "2025-09-01"
        },
        
        # PHASE 2: DÉVELOPPEMENT
        {
            "id": 9, "phase": "PHASE 2 : DÉVELOPPEMENT", "semaine": "Semaine 5 : 2-8 Septembre",
            "titre": "🏗️ Setup environnement de développement", "duree": "2 jours",
            "description": "Configuration infrastructure, CI/CD, bases de données et APIs",
            "objectif": "Environnement dev opérationnel", "outils": ["Docker", "GitHub Actions", "PostgreSQL", "VS Code"],
            "statut": "en_attente", "date_debut": "2025-09-02", "date_fin": "2025-09-03"
        },
        {
            "id": 10, "phase": "PHASE 2 : DÉVELOPPEMENT", "semaine": "Semaine 5 : 2-8 Septembre",
            "titre": "🔧 Développement API Backend", "duree": "5 jours",
            "description": "Créer endpoints REST, gestion utilisateurs, authentification",
            "objectif": "API fonctionnelle avec auth", "outils": ["FastAPI", "SQLAlchemy", "JWT", "GitHub Copilot"],
            "statut": "en_attente", "date_debut": "2025-09-04", "date_fin": "2025-09-08"
        },
        {
            "id": 11, "phase": "PHASE 2 : DÉVELOPPEMENT", "semaine": "Semaine 6 : 9-15 Septembre",
            "titre": "🧠 Intégration modèle LLM", "duree": "5 jours",
            "description": "Fine-tuning, optimisation et intégration du modèle dans l'API",
            "objectif": "LLM intégré et performant", "outils": ["Transformers", "LangChain", "CUDA/PyTorch", "Weights & Biases"],
            "statut": "en_attente", "date_debut": "2025-09-09", "date_fin": "2025-09-13"
        },
        {
            "id": 12, "phase": "PHASE 2 : DÉVELOPPEMENT", "semaine": "Semaine 6 : 9-15 Septembre",
            "titre": "📱 Développement Frontend", "duree": "2 jours",
            "description": "Interface utilisateur responsive avec chat intelligent",
            "objectif": "Interface utilisateur complète", "outils": ["React", "Tailwind CSS", "Axios", "Framer Motion"],
            "statut": "en_attente", "date_debut": "2025-09-14", "date_fin": "2025-09-15"
        },
        {
            "id": 13, "phase": "PHASE 2 : DÉVELOPPEMENT", "semaine": "Semaine 7 : 16-22 Septembre",
            "titre": "🔍 Système de recommandation", "duree": "4 jours",
            "description": "Algorithmes de matching formations/profils étudiants",
            "objectif": "Recommandations personnalisées", "outils": ["Scikit-learn", "TensorFlow", "Surprise", "Redis"],
            "statut": "en_attente", "date_debut": "2025-09-16", "date_fin": "2025-09-19"
        },
        {
            "id": 14, "phase": "PHASE 2 : DÉVELOPPEMENT", "semaine": "Semaine 7 : 16-22 Septembre",
            "titre": "📊 Tableau de bord analytics", "duree": "3 jours",
            "description": "Interface d'administration avec métriques et statistiques",
            "objectif": "Dashboard administrateur", "outils": ["Chart.js", "D3.js", "ElasticSearch"],
            "statut": "en_attente", "date_debut": "2025-09-20", "date_fin": "2025-09-22"
        },
        {
            "id": 15, "phase": "PHASE 2 : DÉVELOPPEMENT", "semaine": "Semaine 8 : 23-29 Septembre",
            "titre": "🧪 Tests et débogage", "duree": "4 jours",
            "description": "Tests unitaires, intégration, performance et sécurité",
            "objectif": "Application stable et sécurisée", "outils": ["Pytest", "Jest", "Locust", "SonarQube"],
            "statut": "en_attente", "date_debut": "2025-09-23", "date_fin": "2025-09-26"
        },
        {
            "id": 16, "phase": "PHASE 2 : DÉVELOPPEMENT", "semaine": "Semaine 8 : 23-29 Septembre",
            "titre": "🚀 Déploiement MVP", "duree": "3 jours",
            "description": "Mise en production version bêta pour tests utilisateurs",
            "objectif": "MVP accessible en ligne", "outils": ["AWS/Heroku", "Docker", "Nginx", "CloudFlare"],
            "statut": "en_attente", "date_debut": "2025-09-27", "date_fin": "2025-09-29"
        },
        
        # PHASE 3: VALIDATION & TESTS
        {
            "id": 17, "phase": "PHASE 3 : VALIDATION & TESTS", "semaine": "Semaine 9 : 30 Sept - 6 Oct",
            "titre": "👥 Recrutement testeurs", "duree": "2 jours",
            "description": "Identifier et mobiliser étudiants, conseillers d'orientation, parents",
            "objectif": "50+ testeurs volontaires", "outils": ["Google Forms", "WhatsApp", "LinkedIn"],
            "statut": "en_attente", "date_debut": "2025-09-30", "date_fin": "2025-10-01"
        },
        {
            "id": 18, "phase": "PHASE 3 : VALIDATION & TESTS", "semaine": "Semaine 9 : 30 Sept - 6 Oct",
            "titre": "🔬 Tests utilisateurs intensifs", "duree": "5 jours",
            "description": "Sessions de test guidées et observation comportementale",
            "objectif": "Feedback détaillé collecté", "outils": ["Zoom", "Hotjar", "UserTesting", "Miro"],
            "statut": "en_attente", "date_debut": "2025-10-02", "date_fin": "2025-10-06"
        },
        {
            "id": 19, "phase": "PHASE 3 : VALIDATION & TESTS", "semaine": "Semaine 10 : 7-13 Octobre",
            "titre": "📈 Analyse des métriques", "duree": "3 jours",
            "description": "Évaluation performance, satisfaction utilisateur, précision recommandations",
            "objectif": "Rapport d'évaluation quantitatif", "outils": ["Google Analytics", "Python/Pandas", "Tableau", "SPSS"],
            "statut": "en_attente", "date_debut": "2025-10-07", "date_fin": "2025-10-09"
        },
        {
            "id": 20, "phase": "PHASE 3 : VALIDATION & TESTS", "semaine": "Semaine 10 : 7-13 Octobre",
            "titre": "🎯 Optimisations ciblées", "duree": "4 jours",
            "description": "Corrections bugs, améliorations UX basées sur les retours",
            "objectif": "Version optimisée déployée", "outils": ["Git", "Jira", "A/B Testing"],
            "statut": "en_attente", "date_debut": "2025-10-10", "date_fin": "2025-10-13"
        },
        {
            "id": 21, "phase": "PHASE 3 : VALIDATION & TESTS", "semaine": "Semaine 11 : 14-20 Octobre",
            "titre": "📊 Benchmark concurrentiel", "duree": "3 jours",
            "description": "Comparaison avec solutions existantes (Parcoursup, plateformes locales)",
            "objectif": "Étude comparative complète", "outils": ["SimilarWeb", "Ahrefs", "Survey Monkey"],
            "statut": "en_attente", "date_debut": "2025-10-14", "date_fin": "2025-10-16"
        },
        {
            "id": 22, "phase": "PHASE 3 : VALIDATION & TESTS", "semaine": "Semaine 11 : 14-20 Octobre",
            "titre": "📝 Validation académique", "duree": "4 jours",
            "description": "Entretiens experts éducation, validation méthodologie par directeur mémoire",
            "objectif": "Validation scientifique obtenue", "outils": ["Calendly", "Zoom", "Notion"],
            "statut": "en_attente", "date_debut": "2025-10-17", "date_fin": "2025-10-20"
        },
        
        # PHASE 4: RÉDACTION & FINALISATION
        {
            "id": 23, "phase": "PHASE 4 : RÉDACTION & FINALISATION", "semaine": "Semaine 12 : 21-27 Octobre",
            "titre": "📚 Rédaction État de l'art", "duree": "5 jours",
            "description": "Synthèse littérature, problématique, positionnement scientifique",
            "objectif": "30 pages état de l'art", "outils": ["Notion AI", "Grammarly", "Zotero", "LaTeX"],
            "statut": "en_attente", "date_debut": "2025-10-21", "date_fin": "2025-10-25"
        },
        {
            "id": 24, "phase": "PHASE 4 : RÉDACTION & FINALISATION", "semaine": "Semaine 12 : 21-27 Octobre",
            "titre": "🎯 Rédaction Méthodologie", "duree": "2 jours",
            "description": "Approche scientifique, choix techniques, protocoles expérimentaux",
            "objectif": "15 pages méthodologie", "outils": ["Draw.io", "ChatGPT", "Word/LaTeX"],
            "statut": "en_attente", "date_debut": "2025-10-26", "date_fin": "2025-10-27"
        },
        {
            "id": 25, "phase": "PHASE 4 : RÉDACTION & FINALISATION", "semaine": "Semaine 13 : 28 Oct - 3 Nov",
            "titre": "⚙️ Rédaction Conception & Développement", "duree": "4 jours",
            "description": "Architecture technique, choix technologiques, implémentation",
            "objectif": "25 pages conception", "outils": ["Screenshots", "Code snippets", "Figma exports", "Jasper AI"],
            "statut": "en_attente", "date_debut": "2025-10-28", "date_fin": "2025-10-31"
        },
        {
            "id": 26, "phase": "PHASE 4 : RÉDACTION & FINALISATION", "semaine": "Semaine 13 : 28 Oct - 3 Nov",
            "titre": "📊 Rédaction Résultats & Analyse", "duree": "3 jours",
            "description": "Présentation données, analyse performance, interprétation résultats",
            "objectif": "20 pages résultats", "outils": ["Matplotlib", "Plotly", "Excel", "DeepL Write"],
            "statut": "en_attente", "date_debut": "2025-11-01", "date_fin": "2025-11-03"
        },
        {
            "id": 27, "phase": "PHASE 4 : RÉDACTION & FINALISATION", "semaine": "Semaine 14 : 4-10 Novembre",
            "titre": "💭 Rédaction Discussion & Perspectives", "duree": "3 jours",
            "description": "Interprétation, limites, perspectives d'amélioration, impact social",
            "objectif": "15 pages discussion", "outils": ["Mind mapping", "Claude AI", "Hemingway Editor"],
            "statut": "en_attente", "date_debut": "2025-11-04", "date_fin": "2025-11-06"
        },
        {
            "id": 28, "phase": "PHASE 4 : RÉDACTION & FINALISATION", "semaine": "Semaine 14 : 4-10 Novembre",
            "titre": "📑 Finalisation parties transversales", "duree": "4 jours",
            "description": "Introduction, conclusion, résumé, abstract, annexes",
            "objectif": "Mémoire structure complète", "outils": ["Table des matières auto", "Vérification format", "Bibliographie"],
            "statut": "en_attente", "date_debut": "2025-11-07", "date_fin": "2025-11-10"
        },
        {
            "id": 29, "phase": "PHASE 4 : RÉDACTION & FINALISATION", "semaine": "Semaine 15 : 11-18 Novembre",
            "titre": "🔍 Révision & Corrections", "duree": "4 jours",
            "description": "Relecture approfondie, corrections orthographe/style, cohérence",
            "objectif": "Mémoire finalisé et corrigé", "outils": ["Grammarly Premium", "Antidote", "Peer review", "LanguageTool"],
            "statut": "en_attente", "date_debut": "2025-11-11", "date_fin": "2025-11-14"
        },
        {
            "id": 30, "phase": "PHASE 4 : RÉDACTION & FINALISATION", "semaine": "Semaine 15 : 11-18 Novembre",
            "titre": "🎯 Préparation soutenance", "duree": "3 jours",
            "description": "Présentation PowerPoint, préparation arguments, simulation oral",
            "objectif": "Soutenance prête", "outils": ["PowerPoint/Canva", "Prezi", "OBS Studio", "Teleprompter"],
            "statut": "en_attente", "date_debut": "2025-11-15", "date_fin": "2025-11-18"
        }
    ]
