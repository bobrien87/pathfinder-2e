---
type: deity
source-type: "Remaster"
domains: "Duty, Might, Protection, Zeal"
favored-weapon: "Spear"
divine-font: "Heal"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Endure]], Rank 4: [[Mountain Resilience]], Rank 5: [[Wall Of Stone]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** The Golden Bulwark

**Areas of Concern** Bodyguards, protection, watchfulness

**Edicts** Protect those weaker than you; remain alert for danger; create, maintain, or patrol defenses

**Anathema** Abandon others while you retreat, engage in needless destruction or bloodshed, intentionally fall asleep or grow lax on watch

**Religious Symbol** gauntlet and briars

**Sacred Animal** golden eagle

**Sacred Colors** gold, purple

**Source:** `= this.source` (`= this.source-type`)
