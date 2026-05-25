---
type: deity
source-type: "Remaster"
domains: "Destruction, Indulgence, Knowledge, Void"
favored-weapon: "Greatclub"
divine-font: "Harm"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Endure]], Rank 2: [[Feast Of Ashes]], Rank 5: [[Acid Storm]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Thuskchoon is a towering slug with numerous limbs and ravenous maws that slithers through the Outer Rifts, consuming all that he finds. In the wake of his near-mindless devastation, his mouths leaves swaths of disgusting tar. Sometimes, Everglutton stumbles across a portal to another plane, though these changes of scenery barely register with the qlippoth lord. He simply continues to indulge his insatiable hunger, uncaring of what (or who) he eats.

**Title** Everglutton

**Areas of Concern** Blinding hunger, mindless consumption, revealed secrets

**Edicts** Devour everything at your disposal, discover hidden knowledge by any means, relish in your desires

**Anathema** Fast of your own accord, keep information to yourself, let food rot

**Religious Symbol** triangular rune with teeth

**Sacred Animal** none

**Sacred Colors** green

**Source:** `= this.source` (`= this.source-type`)
