---
type: deity
source-type: "Remaster"
domains: "Ambition, Indulgence, Might, Zeal"
favored-weapon: "Dagger"
divine-font: "Harm"
divine-skill: "Deception"
divine-spells: "Rank 1: [[Pest Form]], Rank 5: [[Toxic Cloud]], Rank 7: [[Mask Of Terror]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The serpentfolk god is not dead, but in his decapitated state, he might as well be. Reduced to a feral, animalistic existence, Ydersius is even less aware of his legacy than the lowest of the aapoph. Ydersius's symbol is a snake's skull surrounded by a skeletal ouroboros.

**Title** Lord of Coiling Poison

**Areas of Concern** Immortality, poison, serpentfolk

**Edicts** Seek to return Ydersius to life Fulfill your passions, conquer your foes with no mercy, achieve glory for serpentkind

**Anathema** Put the needs of others above those of serpentfolk, aid the spawn of Azlant

**Religious Symbol** snake skull and ouroboros

**Sacred Animal** snake

**Sacred Colors** green, red

**Source:** `= this.source` (`= this.source-type`)
