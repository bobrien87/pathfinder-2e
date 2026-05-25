---
type: deity
source-type: "Remaster"
domains: "Creation, Fate, Nature, Water"
favored-weapon: "Shortbow"
divine-font: "Heal"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Sure Strike]], Rank 5: [[Control Water]], Rank 6: [[Arrow Salvo]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** Ruler of Arrows

**Areas of Concern** Hunting, war, weaving

**Edicts** Protect the dead, open pathways, aid single mothers, lend your prowess to hunts and war

**Anathema** Disrupt the cosmic balance, trap a soul, pollute waterways

**Religious Symbol** shield and two crossed arrows

**Sacred Animal** bee

**Sacred Colors** green, red

**Source:** `= this.source` (`= this.source-type`)
