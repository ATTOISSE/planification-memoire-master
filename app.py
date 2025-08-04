import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
from data.task import taches
import psycopg2
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# --- PostgreSQL Config ---
DB_CONFIG = {
    'dbname': os.getenv('DB_NAME', 'plan'),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', 'pgsql@33'),
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', '5432')
}

def get_db_conn():
    try:
        return psycopg2.connect(**DB_CONFIG)
    except psycopg2.Error as e:
        st.error(f"❌ Erreur de connexion à la base : {e}")
        st.stop()

def create_tasks_table():
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            phase TEXT,
            semaine TEXT,
            titre TEXT,
            duree TEXT,
            description TEXT,
            objectif TEXT,
            outils TEXT,
            statut TEXT,
            date_debut DATE,
            date_fin DATE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    cur.close()
    conn.close()

def load_tasks_from_db():
    create_tasks_table()
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute('SELECT id, phase, semaine, titre, duree, description, objectif, outils, statut, date_debut, date_fin FROM tasks ORDER BY id')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    
    tasks = []
    for row in rows:
        tasks.append({
            "id": row[0],
            "phase": row[1],
            "semaine": row[2],
            "titre": row[3],
            "duree": row[4],
            "description": row[5],
            "objectif": row[6],
            "outils": row[7].split('|') if row[7] else [],
            "statut": row[8],
            "date_debut": str(row[9]) if row[9] else None,
            "date_fin": str(row[10]) if row[10] else None
        })
    return tasks

def save_tasks_to_db(tasks):
    create_tasks_table()
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute('DELETE FROM tasks')
    for t in tasks:
        cur.execute('''
            INSERT INTO tasks (id, phase, semaine, titre, duree, description, objectif, outils, statut, date_debut, date_fin)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (
            t["id"], t["phase"], t["semaine"], t["titre"], t["duree"], 
            t["description"], t["objectif"], '|'.join(t["outils"]), 
            t["statut"], t["date_debut"], t["date_fin"]
        ))
    conn.commit()
    cur.close()
    conn.close()

# Configuration de la page
st.set_page_config(
    page_title="Planning Mémoire - Plateforme LLM Sénégal",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .phase-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #3498db;
        margin-bottom: 1rem;
    }
    .task-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #e0e6ed;
        margin-bottom: 0.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .status-en-attente {
        border-left: 4px solid #ffc107;
        background: #fff8e1;
    }
    .status-en-cours {
        border-left: 4px solid #17a2b8;
        background: #e1f5fe;
    }
    .status-termine {
        border-left: 4px solid #28a745;
        background: #e8f5e8;
    }
</style>
""", unsafe_allow_html=True)

def init_tasks_data():
    tasks = load_tasks_from_db()
    if not tasks:
        tasks = taches
        save_tasks_to_db(tasks)
    return tasks

# Initialisation des données en session state
if 'tasks' not in st.session_state:
    st.session_state.tasks = init_tasks_data()

# Header principal
st.markdown("""
    <div class="main-header">
        <h1>🎓 Planning Mémoire Interactif</h1>
        <h3>Plateforme Intelligente d'Orientation - LLM pour le Sénégal</h3>
        <p>Suivi en temps réel de votre progression • 30 tâches • 4 phases • 15 semaines</p>
    </div>
""", unsafe_allow_html=True)

# Test de connexion
try:
    conn = get_db_conn()
    conn.close()
    st.success("🟢 Connecté à PostgreSQL")
except:
    st.error("🔴 Erreur de connexion PostgreSQL")

# Sidebar pour les contrôles
st.sidebar.header("⚙️ Contrôles")

# Filtres
phases = list(set([task['phase'] for task in st.session_state.tasks]))
selected_phase = st.sidebar.selectbox("Filtrer par phase", ["Toutes"] + phases)

statuts = ["en_attente", "en_cours", "termine"]
selected_statut = st.sidebar.selectbox("Filtrer par statut", ["Tous"] + statuts)

# Statistiques
total_tasks = len(st.session_state.tasks)
en_attente = len([t for t in st.session_state.tasks if t['statut'] == 'en_attente'])
en_cours = len([t for t in st.session_state.tasks if t['statut'] == 'en_cours'])
termine = len([t for t in st.session_state.tasks if t['statut'] == 'termine'])

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("📋 Total Tâches", total_tasks)
with col2:
    st.metric("⏳ En Attente", en_attente)
with col3:
    st.metric("🔄 En Cours", en_cours)
with col4:
    st.metric("✅ Terminées", termine)

# Progression
if total_tasks > 0:
    progress_percent = (termine / total_tasks) * 100
    st.subheader("📈 Progression Globale")
    st.progress(progress_percent / 100)
    st.write(f"**{progress_percent:.1f}% terminé** ({termine}/{total_tasks} tâches)")

# Graphiques
col1, col2 = st.columns(2)

with col1:
    fig_pie = px.pie(
        values=[en_attente, en_cours, termine],
        names=['En Attente', 'En Cours', 'Terminé'],
        title="Répartition des Statuts",
        color_discrete_map={
            'En Attente': '#ffc107',
            'En Cours': '#17a2b8', 
            'Terminé': '#28a745'
        }
    )
    st.plotly_chart(fig_pie, use_container_width=True)

# Filtrer les tâches
filtered_tasks = st.session_state.tasks
if selected_phase != "Toutes":
    filtered_tasks = [t for t in filtered_tasks if t['phase'] == selected_phase]
if selected_statut != "Tous":
    filtered_tasks = [t for t in filtered_tasks if t['statut'] == selected_statut]

# Affichage des tâches
phases_dict = {}
for task in filtered_tasks:
    phase = task['phase']
    if phase not in phases_dict:
        phases_dict[phase] = []
    phases_dict[phase].append(task)

for phase, tasks in phases_dict.items():
    st.markdown(f"""
        <div class="phase-card">
            <h3>{phase}</h3>
            <p><strong>{len([t for t in tasks if t['statut'] == 'termine'])}/{len(tasks)}</strong> tâches terminées</p>
        </div>
    """, unsafe_allow_html=True)
    
    for task in tasks:
        status_class = f"status-{task['statut'].replace('_', '-')}"
        
        with st.container():
            st.markdown(f'<div class="task-card {status_class}">', unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([3, 1, 1])
            
            with col1:
                st.markdown(f"**{task['titre']}**")
                st.markdown(f"<span style='font-size:0.9em;color:#666;'>{task['description']}</span>", unsafe_allow_html=True)
                st.markdown(f"<span style='font-size:0.85em;color:#888;'>Objectif : {task['objectif']}</span>", unsafe_allow_html=True)
                st.markdown(f"<span style='font-size:0.85em;color:#888;'>Outils : {', '.join(task['outils'])}</span>", unsafe_allow_html=True)
                st.markdown(f"<span style='font-size:0.85em;color:#888;'>Durée : {task['duree']}</span>", unsafe_allow_html=True)
                st.markdown(f"<span style='font-size:0.85em;color:#888;'>Du {task['date_debut']} au {task['date_fin']}</span>", unsafe_allow_html=True)
            
            with col2:
                statut_options = ["en_attente", "en_cours", "termine"]
                new_statut = st.selectbox(
                    "Statut", statut_options, 
                    index=statut_options.index(task['statut']), 
                    key=f"statut_{task['id']}"
                )
                if new_statut != task['statut']:
                    task['statut'] = new_statut
                    save_tasks_to_db(st.session_state.tasks)
                    st.rerun()
            
            with col3:
                if st.button("🔍 Détails", key=f"details_{task['id']}"):
                    st.info(f"**{task['titre']}**\n\n{task['description']}")
            
            st.markdown("</div>", unsafe_allow_html=True)