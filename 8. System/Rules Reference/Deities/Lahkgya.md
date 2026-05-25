---
type: deity
source-type: "Remaster"
domains: "Indulgence, Nature, Swarm, Trickery"
favored-weapon: "Jaws, Battle-axe"
divine-font: "Harm"
divine-skill: "Thievery"
divine-spells: "Rank 1: [[Fleet Step]], Rank 3: [[Mad Monkeys]], Rank 4: [[Confusion]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** Patron of Monkeys

**Areas of Concern** Mischief, monkeys, riches

**Edicts** Steal luxuries for yourself, destroy property for fun, demand bribes to spare creatures from your torments

**Anathema** Work honestly for something you could steal instead, kill a monkey

**Religious Symbol** monkey hand grasping a fang

**Sacred Animal** monkey

**Sacred Colors** gray, red

**Source:** `= this.source` (`= this.source-type`)
