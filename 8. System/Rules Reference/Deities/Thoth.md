---
type: deity
source-type: "Remaster"
domains: "Glyph, Knowledge, Magic, Moon"
favored-weapon: "Sickle"
divine-font: "Harm, Heal"
divine-skill: "Arcana"
divine-spells: "Rank 1: [[Message Rune]], Rank 3: [[Sea Of Thought]], Rank 5: [[Moon Frenzy]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** Lord of Divine Words

**Areas of Concern** Magic, the moon, wisdom, writing

**Edicts** Maintain order in society and the multiverse, innovate scientific and magical knowledge, record events

**Anathema** Upset stable mechanisms or ecosystems, fail to correct false information

**Religious Symbol** scroll with lunar disk and crescent

**Sacred Animal** ibis

**Sacred Colors** green, white

**Source:** `= this.source` (`= this.source-type`)
