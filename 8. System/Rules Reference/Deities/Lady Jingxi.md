---
type: deity
source-type: "Remaster"
domains: "Creation, Glyph, Knowledge, Repose"
favored-weapon: "Fighting-fan"
divine-font: "Heal"
divine-skill: "Performance"
divine-spells: "Rank 1: [[Dizzying Colors]], Rank 3: [[Enthrall]], Rank 7: [[Project Image]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** The Poet of Dawn and Dusk

**Areas of Concern** Daybreak, liminal spaces, twilight, solitude

**Edicts** Create art with words, master the written language, display the soft beauty of natural colors

**Anathema** Destroy a natural plum tree, drink excessive amounts of alcohol, act rude or boorish, commit torture or murder, knowingly harm an innocent

**Religious Symbol** plum blossoms framing a mirror

**Sacred Animal** swift

**Sacred Colors** pink, purple

**Source:** `= this.source` (`= this.source-type`)
