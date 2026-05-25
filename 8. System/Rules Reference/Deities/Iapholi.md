---
type: deity
source-type: "Remaster"
domains: "Confidence, Introspection, Might, Perfection"
favored-weapon: "War-flail"
divine-font: "Harm, Heal"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Sure Strike]], Rank 2: [[Hidebound]], Rank 8: [[Monstrosity Form]]"
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** Child of Bloodstone

**Areas of Concern** monstrous heritage and acceptance

**Edicts** Develop unique strengths, ally with those who appear different than you do, defend monsters who have been falsely vilified

**Anathema** vilify a monster based on the reputation of their species, terrorize others for fun

**Religious Symbol** winged egg

**Sacred Animal** hoatzin

**Sacred Colors** crimson and green

**Source:** `= this.source` (`= this.source-type`)
