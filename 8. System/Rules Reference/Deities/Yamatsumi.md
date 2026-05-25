---
type: deity
source-type: "Remaster"
domains: "Cold, Earth, Fire, Might"
favored-weapon: "Greatclub"
divine-font: "Harm, Heal"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Shockwave]], Rank 3: [[Shifting Sand]], Rank 7: [[Volcanic Eruption]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** The Mountain Lord

**Areas of Concern** Mountains, volcanoes, winter

**Edicts** Strive to be self-sufficient, respect nature, test yourself against the elements

**Anathema** Become reliant on civilization, destroy something without creating or growing something in its place

**Religious Symbol** Erupting, snowcapped volcano

**Sacred Animal** ram

**Sacred Colors** blue, white

**Source:** `= this.source` (`= this.source-type`)
