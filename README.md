# MMR System

Gamify your coding life. MMR System tracks your GitHub commits and awards you a **Matchmaking Rating** — just like Dota 2, League of Legends, or APEX — based on how consistently and actively you push code.

Your rank is shown live in the VS Code status bar. Click it to open the rank panel.

---

## Ranks

| MMR | Rank |
|-----|------|
| 9000+ | Immortal |
| 7000–8999 | Divine |
| 5000–6999 | Ancient |
| 3500–4999 | Legend |
| 2000–3499 | Archon |
| 1000–1999 | Crusader |
| 500–999 | Guardian |
| 0–499 | Herald |

---

## How MMR is calculated

- **+10 MMR** per commit across all your repos
- **+100 MMR** per repository you own
- **+30 MMR** per day in your longest commit streak
- **−10 MMR** per day since your last commit (penalty kicks in after 3 inactive days)

MMR never drops below 0.

---

## Setup

### 1. Create a GitHub Personal Access Token

1. Go to **GitHub → Settings → Developer settings → Personal access tokens → Fine-grained tokens**
2. Create a token with **read-only** access to **Repository contents** and **Metadata**
3. Copy the token

### 2. Enter your credentials in VS Code settings

Open Settings (`Cmd+,` on Mac / `Ctrl+,` on Windows) and search for `mmrSystem`:

| Setting | Description |
|---------|-------------|
| `mmrSystem.githubToken` | Your GitHub Personal Access Token |
| `mmrSystem.githubUsername` | Your GitHub username |

MMR loads automatically and refreshes every 30 minutes.

---

## Extension Settings

- `mmrSystem.githubToken` — GitHub Personal Access Token (fine-grained, read-only)
- `mmrSystem.githubUsername` — Your GitHub username

---

## Security

Your token is stored in VS Code's built-in settings and is only sent to the official GitHub API (`api.github.com`). Use a fine-grained token with minimum required scopes — never a classic token with broad permissions.

---

## Known Issues

- Only fetches the first 100 repos and 100 commits per repo (pagination not yet implemented)
- Private repos require the token to have private repository access

---

## Release Notes

### 0.0.1

Initial release — status bar MMR, rank panel with badge art, 30-minute auto-refresh.
