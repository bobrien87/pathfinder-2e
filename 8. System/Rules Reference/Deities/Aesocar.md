---
type: deity
source-type: "Remaster"
domains: "Creation, Healing, Protection, Repose"
favored-weapon: "Flail"
divine-font: "Heal"
divine-skill: "Medicine"
divine-spells: "Rank 1: [[Soothe]], Rank 2: [[False Vitality]], Rank 4: [[Creation]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Aesocar, the Healing Touch, was the Azlanti god of creation, health and medicine. His clerics were some of the first who practiced the art of melding faith with science. Aesocar taught that while some ailments could be cured through divine means, his followers should also learn all they could about medicine and ways to heal not only humanity, but all in need. His clerics were among the first to master the art of prosthetics and creating life from nothing.

**Title** The Healing Touch

**Areas of Concern** Creation, health, medicine

**Edicts** Provide healing and aid to those who need it, promote the value of connecting faith and science, strive to defend and protect others in battle

**Anathema** Do unnecessary harm, spread disease, fail to aid someone in need

**Religious Symbol** enclosed six-pointed star

**Sacred Animal** starfish

**Sacred Colors** gold

**Source:** `= this.source` (`= this.source-type`)
