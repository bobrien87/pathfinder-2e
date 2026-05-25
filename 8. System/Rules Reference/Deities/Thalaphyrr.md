---
type: deity
source-type: "Remaster"
domains: "Ambition, Darkness, Nightmares, Trickery"
favored-weapon: "Spear"
divine-font: "Harm"
divine-skill: "Stealth"
divine-spells: "Rank 1: [[Phantom Pain]], Rank 3: [[Slow]], Rank 5: [[Umbral Journey]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The Forsaken patron of failed heroics, imprisonment, and squandered time.

**Title** Martyr-Minder

**Areas of Concern** Failed heroics, imprisonment, squandered time

**Edicts** Learn from your failures, watch over prisoners

**Anathema** Consider anything a poor use of time, allow a prisoner to escape

**Religious Symbol** hands grasping a set of prison bars

**Sacred Animal** hermit crab

**Sacred Colors** black, gray

An owb prophet can transfer the power they gain from a Forsaken patron to those who worship them, effectively serving as a deity. Each owb prophet decides their own follower alignments, edicts, and anathema.

**Source:** `= this.source` (`= this.source-type`)
