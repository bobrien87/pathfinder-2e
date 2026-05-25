---
type: deity
source-type: "Remaster"
domains: "Glyph, Void, Secrecy, Wealth"
favored-weapon: "Rapier"
divine-font: "Harm"
divine-skill: "Deception"
divine-spells: "Rank 1: [[Illusory Disguise]], Rank 4: [[Confusion]], Rank 5: [[Hallucination]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Hastur is a Great Old One who, though confined to the city of Carcosa on a planet orbiting a faraway star, is nevertheless in the midst of a transformation into a true Outer God. He works toward this feat through his avatar, the King in Yellow, which can manifest anywhere in the universe the light from Carcosa's sun can be seen. The King in Yellow appears as a humanoid figure draped in yellow clothing, but there is nothing within the cloth save a shapeless, horrifying presence. Hastur is also referred to as Him Who Is Not To Be Named, or simply the Unspeakable.

**Title** The King in Yellow

**Areas of Concern** Decadence, disorder, nihilism

**Edicts** Spread Hastur's Yellow Sign, hide the true nature of your worship, promulgate the play The King in Yellow

**Anathema** None

**Religious Symbol** the Yellow Sign

**Sacred Animal** none

**Sacred Colors** yellow

**Source:** `= this.source` (`= this.source-type`)
