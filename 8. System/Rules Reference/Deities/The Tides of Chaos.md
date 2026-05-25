---
type: deity
source-type: "Remaster"
domains: "Cities, Darkness, Destruction, Secrecy"
favored-weapon: "Dagger"
divine-font: "Harm"
divine-skill: "Stealth"
divine-spells: "Rank 1: [[Ill Omen]], Rank 2: [[Invisibility]], Rank 5: [[Subconscious Suggestion]]"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Covenant Members** Calistria, Norgorber, Scal, Ulon

**Areas of Concern** chaos, disruption, mischief, secrets

**Edicts** keep all secrets entrusted to you, sow mistrust, doubt, and conspiracy at every opportunity, take risks

**Anathema** aid in the establishment of a government or ruling power, embrace complacency, reveal secrets entrusted to you

**Religious Symbol** chaotic spider web

**Source:** `= this.source` (`= this.source-type`)
