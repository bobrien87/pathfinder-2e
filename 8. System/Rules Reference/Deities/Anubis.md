---
type: deity
source-type: "Remaster"
domains: "Death, Protection, Soul, Vigil"
favored-weapon: "Flail"
divine-font: "Harm, Heal"
divine-skill: "Occultism"
divine-spells: "Rank 1: [[Phantasmal Minion]], Rank 3: [[Shifting Sand]], Rank 5: [[Wall Of Stone]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Anubis is the son of Osiris and Nephthys, born out of wedlock and he assisted Isis in the mummification of his father. He frequently works with Isis, Neith, Nephthys, and Selket in the protection of the dead, and is an enemy of Set due to his association with undead.

**Title** Guardian of the Tomb

**Areas of Concern** Burial, the dead, funeral rites, mummification, tombs

**Edicts** Lay bodies to rest, destroy undead, be impartial in judgment

**Anathema** Desecrate a corpse, take from the dead in bad faith, trap a soul

**Religious Symbol** black jackal head

**Sacred Animal** jackal

**Sacred Colors** black, gold

**Source:** `= this.source` (`= this.source-type`)
