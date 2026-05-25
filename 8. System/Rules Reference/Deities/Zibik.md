---
type: deity
source-type: "Remaster"
domains: "Decay, Healing, Nature, Protection"
favored-weapon: "Scythe"
divine-font: "Harm, Heal"
divine-skill: "Medicine"
divine-spells: "Rank 1: [[Flourishing Flora]], Rank 4: [[Life Draining Roots]], Rank 6: [[Tangling Creepers]]"
source: "Pathfinder #203: Shepherd of Decay"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Most of Zibik's worshippers are leshies, ardandes, and wood elementals, though a few are humanoid clerics; Zibik only accepts clerics who show the fortitude and ability to ensure nature takes its course, sacrificing

**Areas of Concern** decay, fresh starts, and fungi

**Edicts** foster natural cycles of decay and regrowth, eradicate invasive creatures, treat unnatural diseases

**Anathema** ignore mistreatment of the environment, delay natural death, cause imbalance in an ecosystem

**Source:** `= this.source` (`= this.source-type`)
