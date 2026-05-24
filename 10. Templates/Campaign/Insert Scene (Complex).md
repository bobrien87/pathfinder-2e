---
type: scene
played: false
sub-type: complex
rewards:
  - "{wikilink:item}"
---
### `= this.file.name`
{summary}

#### Secrets & Clues
- [ ] {discovery}

### Hook
{hook}

### 1. {beat-heading}
{beat-content}

### 2. {beat-heading}
{beat-content}

### 3. {beat-heading}
{beat-content}

### Resolution
{resolution}

#### Rewards
``` dataview
LIST
WHERE file.path = this.file.path
FLATTEN this.rewards as reward
```

#### Developments
{developments}
