---
type: deity
source-type: "Remaster"
domains: "Confidence, Might, Knowledge, Wealth"
favored-weapon: "Trident"
divine-font: "Harm, Heal"
divine-skill: "Performance"
divine-spells: "Rank 1: [[Sure Strike]], Rank 2: [[Invisibility]], Rank 4: [[Weapon Storm]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** The Evil Prince

**Areas of Concern** Majesty, power, refinement

**Edicts** Improve yourself with music and literature, take what you want, seek power above others

**Anathema** Abuse a loyal subject, harm or kill a non-combatant

**Religious Symbol** sitar made from a human head

**Sacred Animal** wolf

**Sacred Colors** green, red

**Source:** `= this.source` (`= this.source-type`)
