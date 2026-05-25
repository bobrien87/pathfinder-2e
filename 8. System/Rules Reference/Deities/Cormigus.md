---
type: deity
source-type: "Remaster"
domains: "Creation, Glyph, Knowledge, Travel"
favored-weapon: "Flyssa"
divine-font: "Heal"
divine-skill: "Diplomacy"
divine-spells: "Rank 1: [[Message Rune]], Rank 4: [[Honeyed Words]], Rank 9: [[Unfathomable Song]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** The Chime Above All

**Areas of Concern** Language, news, and sounds

**Edicts** Encourage communication with others, share important news, visit sites of extreme loudness or silence

**Anathema** Cast [[Silence]] and similar spells, intentionally share information you know to be incorrect, remove others' ability to speak

**Religious Symbol** Fist holding a runed scroll

**Sacred Animal** pigeon

**Sacred Colors** purple, teal

**Source:** `= this.source` (`= this.source-type`)
