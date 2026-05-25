---
type: deity
source-type: "Remaster"
domains: "Decay, Destruction, Metal, Void"
favored-weapon: "Pick"
divine-font: "Harm"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Conductive Weapon]], Rank 3: [[Noxious Metals]], Rank 4: [[Rust Cloud]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Ferrumnestra, the Lady of Rust, is the elemental lord of metal, decay, and inevitability. Eternally wandering across the Plane of Metal, Ferrumnestra's touch is that of slow decline, the rust of ages that eats away at even the strongest of steel. While she has no particular desire to hasten any endings, she is there to consume the last crumbling detritus of its inevitable demise, leaving nonexistence in her wake. She keeps no permanent dwelling, always on the move as is her purpose; her few devotees usually follow her example, traveling across the world and destroying the wreckage of ancient ruins in their wake.

**Title** The Lady of Rust

**Areas of Concern** Decline, inevitability, metal, mourning

**Edicts** Accept the inevitable, clear what remains of that which has fallen to ruin, usher the past into obscurity

**Anathema** Preserve knowledge that has outlived its time, restore an object or structure that has been reclaimed by the elements

**Religious Symbol** rusted metal antennae

**Sacred Animal** isopod

**Sacred Colors** rust red, silver

**Source:** `= this.source` (`= this.source-type`)
