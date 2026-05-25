---
type: deity
source-type: "Remaster"
domains: "Air, Earth, Fire, Metal, Nature, Water, Wood"
favored-weapon: "Sickle, Claw"
divine-font: "Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Summon Animal]], Rank 2: [[Speak With Animals]], Rank 3: [[Wall Of Thorns]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The worshippers of the Green Faith count many druids among their number. They view nature as divine and draw strength from the knowledge of their place in the natural order.

**Covenant Members** natural spirits, powerful animals

**Areas of Concern** veneration of the natural world

**Edicts** guide civilization to grow in harmony with nature, live sustainably and according to natural cycles, preserve areas of natural wilderness, protect the balance of nature, protect endangered species

**Anathema** cause damage to natural settings, kill animals for reasons other than self-defense or sustenance, remove an element or indigenous species from a natural area, encourage imbalance in nature, allow abuse of natural resources

**Religious Symbol** green man's face

**Source:** `= this.source` (`= this.source-type`)
