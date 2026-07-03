# 🛠️ Profile Setup Guide

## ⚡ Quick Start - Already Working!

Les éléments suivants fonctionnent immédiatement **sans configuration** :
- ✅ GitHub Stats (via github-readme-stats.vercel.app)
- ✅ Streak Stats (via streak-stats.demolab.com) 
- ✅ Contribution Snake Animation (workflow automatique)
- ✅ Contribution Heatmap
- ✅ Profile views counter

## GitHub Actions Configuration

### 1. Snake Animation (Configured ✅)
Le workflow `snake.yml` génère automatiquement l'animation de tes contributions.

**Status:** Prêt à l'emploi
- Lance-le une fois manuellement depuis l'onglet "Actions" → "Generate Snake" → "Run workflow"
- Ensuite, il se met à jour automatiquement toutes les 12h
- Aucune configuration supplémentaire nécessaire

### 2. GitHub Metrics (Optionnel - Désactivé par défaut)

Le fichier `metrics.yml.disabled` contient une config avancée mais nécessite un token.

**Pour l'activer (optionnel):**

1. Créer un Personal Access Token:
   - https://github.com/settings/tokens
   - "Generate new token (classic)"
   - Scopes: `repo`, `read:user`, `read:org`
   - Copie le token

2. Ajouter aux secrets:
   - https://github.com/Al-khali/Al-khali/settings/secrets/actions
   - Name: `METRICS_TOKEN`
   - Value: [ton token]

3. Renommer le workflow:
   ```bash
   mv .github/workflows/metrics.yml.disabled .github/workflows/metrics.yml
   git add . && git commit -m "Enable metrics" && git push
   ```

**Note:** Les stats actuelles fonctionnent déjà sans ça !

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

## 🎨 Aesthetic Tips

### Working Widget Sources (Nov 2025)

**Stats Cards:**
- `github-readme-stats.vercel.app` - Stats & Languages (working)
- `streak-stats.demolab.com` - Contribution streaks (Heroku est mort, utilise demolab)
- `github-profile-trophy.vercel.app` - Achievement badges
- `ghchart.rshah.org` - Simple contribution heatmap

**Alternatives si un service tombe:**
- Stats Generator: https://github-stats.omsimos.com/
- GitHobby: https://githobby.com/
- GH Stats Gen: https://gh-stats-gen.vercel.app/

### ASCII Art Generator
- [patorjk.com/software/taag/](https://patorjk.com/software/taag/)
- Font: ANSI Shadow (utilisée pour "LAYER 11")

### Color Palette (Cyberpunk 2000s)
```
Cyber Cyan:    #00f5ff, #00d9ff, #00bfff
Neon Magenta:  #ff00ff, #ff1493, #da00ff
Matrix Green:  #00ff00, #39ff14
Deep Dark:     #0d1117, #010409, #0a0e14
```

### Références Subtiles Intégrées

- 🔹 "Present Day, Present Time" - Serial Experiments Lain opening
- 🔹 "Connected to the Wired" - Le réseau de Lain
- 🔹 "No matter where you go, everyone's connected" - Citation iconique
- 🔹 "PROTOCOL LAYER 7" - OSI model (layer 7 = Application layer)
- 🔹 "LAYER 11" ASCII - Référence aux protocoles de Lain
- 🔹 Palette cyan/magenta - Aesthetic Lain/Ergo Proxy années 2000

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

## 🐛 Troubleshooting

### "Something went wrong" sur les stats?
- **Cause:** Les services Vercel gratuits ont des rate limits
- **Solution:** Attends 5-10 minutes, GitHub cache les images
- **Alternative:** Change le domaine vers les alternatives listées plus haut

### Snake animation ne s'affiche pas?
- Lance le workflow manuellement la première fois
- Vérifie que la branche `output` existe après l'exécution
- Le SVG prend quelques minutes à apparaître

### Heroku apps down?
- ❌ `herokuapp.com` services sont morts/instables
- ✅ Utilise `demolab.com` ou `vercel.app` à la place

### Stats pas à jour?
- Les badges se rafraîchissent toutes les ~15min
- Force refresh: `Ctrl+Shift+R` (ou `Cmd+Shift+R` sur Mac)
- GitHub CDN peut cacher pendant 1h max

## 💡 Pro Tips

1. **Ne jamais commiter de tokens** dans le code
2. Les workflows prennent 1-2 minutes max
3. La branche `output` est auto-générée par le snake workflow
4. Les images peuvent être cachées, force refresh si nécessaire
5. **Évite `include_all_commits=true`** sur stats (cause rate limits)
6. Si un service tombe, remplace l'URL par une alternative

## 🔄 Maintenance Notes (Nov 2025)

**Services qui fonctionnent:**
- ✅ `github-readme-stats.vercel.app` (stats)
- ✅ `streak-stats.demolab.com` (streaks)
- ✅ `github-profile-trophy.vercel.app` (trophies)
- ✅ Platane/snk@v3 (snake, sans svg-only)

**Services à éviter:**
- ❌ `*.herokuapp.com` (Heroku free tier mort)
- ❌ `include_all_commits=true` (rate limits)
- ⚠️ `github-readme-activity-graph` (peut être lent)

---

```
╔══════════════════════════════════════╗
║  SYSTEM CONFIGURED • ALL GREEN ✓    ║
╚══════════════════════════════════════╝
```
