---
type: deity
source-type: "Remaster"
domains: "Decay, Nature, Void, Undeath"
favored-weapon: "Flail"
divine-font: "Harm"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Grim Tendrils]], Rank 2: [[Entangling Flora]], Rank 5: [[Toxic Cloud]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

An especially reclusive Outer God who hunts along the shores of the River of Souls, Nhimbaloth is a shapeless entity known as the Empty Death. She preys on those who hunt souls as they travel down the river, but she devours both hunter and soul indiscriminately; those she consumes have no afterlife or potential for resurrection. They are forever gone, and forever nothing.

Nhimbaloth is said to see through will-o'-wisps, and her trace is left behind in a symmetrical pattern of seven divots along the shoreline, said to be her fingerprints. Faceless undead haunt the places she has passed through, and plant and animal life in the area is especially hostile to the living. One place where she has particular influence is within the Mushfens of southern Varisia, where will-o'-wisp oracles sap the drive and reason from their victims and leave them wandering in a vacuous stupor through the blasted swamp.

**Title** The Empty Death

**Areas of Concern** Despair, ghosts, swamps

**Edicts** Create undead, feast upon carnivores that have recently feasted upon others

**Anathema** None

**Religious Symbol** dripping skull with jaw stuffed with wet moss

**Sacred Animal** none

**Sacred Colors** green, white

**Source:** `= this.source` (`= this.source-type`)
