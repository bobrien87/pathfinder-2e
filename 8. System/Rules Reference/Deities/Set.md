---
type: deity
source-type: "Remaster"
domains: "Death, Darkness, Dust, Lightning"
favored-weapon: "Spear"
divine-font: "Harm"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Penumbral Shroud]], Rank 3: [[Cup Of Dust]], Rank 6: [[Disintegrate]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Set is the most reviled of all the Ancient Osirian pantheon. He is the encroaching desert, the invader, the sandstorm destroying everything in its path, as well as the dead who rise from their graves.

**Title** Lord of the Dark Desert

**Areas of Concern** Darkness, deserts, murder, storms

**Edicts** Bring chaos to society, murder those who stand in your way, defeat your foes with personal strength and cunning, kill fiends

**Anathema** Permit the spread of the desert to fertile lands, refuse to fight your own battles, aid Apep or other omnicidal gods

**Religious Symbol** Sha head

**Sacred Animal** Sha

**Sacred Colors** red, yellow

**Source:** `= this.source` (`= this.source-type`)
