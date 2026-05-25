---
type: deity
source-type: "Remaster"
domains: "Might, Protection, Water, Wyrmkin"
favored-weapon: "Falchion"
divine-font: "Harm, Heal"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Hydraulic Push]], Rank 3: [[Feet To Fins]], Rank 4: [[Dinosaur Form]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** The Raging Torrent

**Areas of Concern** Crocodiles, fertility, military prowess, rivers

**Edicts** Take what you want, indulge in base desires, feast on luxurious food, kill demons and evil creatures

**Anathema** Cower from fights, despoil the land, kill the innocent

**Religious Symbol** Green crocodile

**Sacred Animal** crocodile

**Sacred Colors** green, gold

**Source:** `= this.source` (`= this.source-type`)
