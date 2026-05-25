---
type: deity
source-type: "Remaster"
domains: "Ambition, Darkness, Nightmares, Trickery"
favored-weapon: "Morningstar"
divine-font: "Harm"
divine-skill: "Stealth"
divine-spells: "Rank 1: [[Phantom Pain]], Rank 4: [[Rewrite Memory]], Rank 5: [[Umbral Journey]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Taking the form of a massive shadow, Reshmit is the Forsaken patron of broken things, forgetting, and unexpected violence.

**Title** Shredsong

**Areas of Concern** Broken things, forgetting, unexpected violence

**Edicts** Attack at your whim, shatter objects, sing

**Anathema** Repair an object you've broken, seek lost memories

**Religious Symbol** Torn steel plate

**Sacred Animal** none

**Sacred Colors** black, Silver

An owb prophet can transfer the power they gain from a Forsaken patron to those who worship them, effectively serving as a deity. Each owb prophet decides their own follower alignments, edicts, and anathema.

**Source:** `= this.source` (`= this.source-type`)
