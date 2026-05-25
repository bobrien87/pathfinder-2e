---
type: deity
source-type: "Remaster"
domains: "Healing, Knowledge, Magic, Protection"
favored-weapon: "Mace"
divine-font: "Heal"
divine-skill: "Medicine"
divine-spells: "Rank 1: [[Soothe]], Rank 2: [[False Vitality]], Rank 4: [[Containment]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** Master of Medicine

**Areas of Concern** Cycles, elements, health, medicine

**Edicts** Teach knowledge to others, relieve suffering despite personal difficulty, heal sickness and injury

**Anathema** Deal lethal damage to another living creature (unless as part of a necessary medical treatment)

**Religious Symbol** wheel with spokes of the five elements

**Sacred Animal** crane

**Sacred Colors** red, yellow, white, black, green

**Source:** `= this.source` (`= this.source-type`)
