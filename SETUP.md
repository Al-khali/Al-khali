# 🛠️ Profile Setup Guide

## GitHub Actions Configuration

### 1. Snake Animation (Already configured ✅)
Le workflow `snake.yml` génère automatiquement l'animation de tes contributions.

**Actions requises:**
- Aucune configuration nécessaire
- Le workflow se lance automatiquement toutes les 12h
- Tu peux aussi le lancer manuellement depuis l'onglet "Actions"

### 2. GitHub Metrics (Optionnel)

Pour activer les métriques avancées:

1. Créer un Personal Access Token (classic):
   - Va sur https://github.com/settings/tokens
   - "Generate new token" → "Generate new token (classic)"
   - Nom: `METRICS_TOKEN`
   - Expiration: No expiration ou 1 year
   - Scopes nécessaires:
     - ✅ `repo` (all)
     - ✅ `read:user`
     - ✅ `read:org`
   - Copie le token

2. Ajouter le token aux secrets:
   - Va sur https://github.com/Al-khali/Al-khali/settings/secrets/actions
   - "New repository secret"
   - Name: `METRICS_TOKEN`
   - Value: [colle ton token]

### 3. WakaTime Stats (Optionnel - Tracking de temps)

WakaTime track automatiquement ton temps de code dans différents languages/projets.

**Setup:**

1. Créer un compte sur [WakaTime](https://wakatime.com/signup)

2. Installer WakaTime dans ton éditeur:
   ```bash
   # Pour Neovim
   # Ajoute dans ton config (packer/lazy)
   use 'wakatime/vim-wakatime'
   
   # Pour VSCode
   # Installe l'extension WakaTime
   ```

3. Récupérer ton API Key:
   - Va sur https://wakatime.com/settings/account
   - Copie ta "Secret API Key"

4. Ajouter aux GitHub secrets:
   - Name: `WAKATIME_API_KEY`
   - Value: [ta clé API]

5. Ajouter ce badge dans ton README:
   ```markdown
   <img src="https://wakatime.com/badge/user/[TON_USER_ID].svg" alt="wakatime"/>
   ```

### 4. Personnalisation des Couleurs

Les couleurs actuelles (Lain/Ergo Proxy inspired):
- **Cyan**: `#00f5ff` - Couleur principale (thème Lain)
- **Magenta**: `#ff00ff` - Accents (holographique)
- **Dark**: `#0d1117` - Background (profondeur)

Pour modifier, édite les URLs des badges dans le README.

### 5. Badges Personnalisés

Tu peux créer des badges custom sur [shields.io](https://shields.io):
```
https://img.shields.io/badge/[LABEL]-[MESSAGE]-[COLOR]?style=flat-square
```

## Aesthetic Tips

### ASCII Art Generator
Pour créer des headers ASCII:
- [patorjk.com/software/taag/](https://patorjk.com/software/taag/)
- Font recommandée: ANSI Shadow

### Color Palette (Cyberpunk 2000s)
```
Cyber Cyan:    #00f5ff, #00d9ff, #00bfff
Neon Magenta:  #ff00ff, #ff1493, #da00ff
Matrix Green:  #00ff00, #39ff14
Deep Dark:     #0d1117, #010409, #0a0e14
```

### Références Subtiles

Actuellement intégré:
- 🔹 "Present Day, Present Time" - Lain opening
- 🔹 "Connected to the Wired" - Référence au réseau de Lain
- 🔹 "No matter where you go, everyone's connected" - Citation Lain
- 🔹 "PROTOCOL LAYER 7" - Référence réseau OSI (subtle tech)
- 🔹 Palette cyan/magenta - Aesthetic Lain/Ergo Proxy

## Maintenance

### Update Stats
Les stats se mettent à jour automatiquement:
- Snake: toutes les 12h
- Metrics: quotidiennement
- Badges: en temps réel

### Manual Trigger
Pour forcer une mise à jour:
1. Va sur l'onglet "Actions" de ton repo
2. Sélectionne le workflow
3. "Run workflow" → "Run workflow"

## Pro Tips

1. **Ne jamais commiter de tokens** dans le code
2. Les workflows peuvent prendre 1-2 minutes
3. La branche `output` est auto-générée
4. Les images peuvent prendre quelques minutes à se rafraîchir

---

```
╔══════════════════════════════════════╗
║  SYSTEM CONFIGURED • ALL GREEN ✓    ║
╚══════════════════════════════════════╝
```
