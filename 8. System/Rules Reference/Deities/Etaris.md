---
type: deity
source-type: "Remaster"
domains: "Ambition, Confidence, Nature, Secrecy"
favored-weapon: "Staff"
divine-font: "Heal"
divine-skill: "Society"
divine-spells: "Rank 1: [[Summon Animal]], Rank 2: [[Speak With Animals]], Rank 5: [[Slither]]"
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** The Bride of Ydersius

**Areas of Concern** Agriculture, civilization, secrets

**Edicts** Tend to the needs of the weak as a means to accumulate strength and power, delve deep into the mysteries of the ancient past, band in great numbers to overwhelm the enemy, reclaim the past glory of the old Aishmayar civilization

**Anathema** Bow down before an unworthy master, undermine the success of the heirs of the ancient Aishmayar civilization

**Religious Symbol** two serpents entwined around an ivory staff

**Sacred Animal** snake

**Sacred Colors** green, purple

**Source:** `= this.source` (`= this.source-type`)
