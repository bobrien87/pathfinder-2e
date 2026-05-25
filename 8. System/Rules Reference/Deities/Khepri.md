---
type: deity
source-type: "Remaster"
domains: "Creation, Healing, Protection, Sun"
favored-weapon: "Sling"
divine-font: "Heal"
divine-skill: "Medicine"
divine-spells: "Rank 1: [[Flourishing Flora]], Rank 2: [[Floating Flame]], Rank 3: [[Elemental Absorption]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** The Humble Hand

**Areas of Concern** Freedom, the rising sun, work

**Edicts** Work steadily and consistantly, pray to the rising sun, aid in the renewal and creation of life, perform resurrections

**Anathema** Kill a plant or a creature with cold damage, seal a building to completely block sunlight, harm a pregnant creature

**Religious Symbol** blue scarab

**Sacred Animal** scarab beetle

**Sacred Colors** blue, red

**Source:** `= this.source` (`= this.source-type`)
