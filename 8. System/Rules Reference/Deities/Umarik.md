---
type: deity
source-type: "Remaster"
domains: "Air, Destruction, Nature, Water"
favored-weapon: "Trident"
divine-font: "Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Gust Of Wind]], Rank 5: [[Howling Blizzard]], Rank 8: [[Punishing Winds]]"
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** Father Storm

**Areas of Concern** Storms

**Edicts** Spend time appreciating storms, support your family and close friends, seek places where lightning has struck

**Anathema** Take shelter from rain when you are healthy, warn fools about upcoming storms, seek positions of political power

**Religious Symbol** Silver storm clouds

**Sacred Animal** Toad

**Sacred Colors** Gray, silver

**Source:** `= this.source` (`= this.source-type`)
