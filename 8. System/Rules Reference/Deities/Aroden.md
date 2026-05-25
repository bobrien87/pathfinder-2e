---
type: deity
source-type: "Remaster"
domains: "Ambition, Creation, Fate, Knowledge"
favored-weapon: "Longsword"
divine-font: "Harm, Heal"
divine-skill: "Society"
divine-spells: "Rank 1: [[Fleet Step]], Rank 3: [[Hypercognition]], Rank 7: [[Contingency]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** The Last Azlanti

**Areas of Concern** Culture, fulfillment of destiny, history, humanity, innovation

**Edicts** Create inventions and make innovations, record history, support your fellow humans, work toward your goals and destiny

**Anathema** Destroy historical texts or records; sabotage another's attempts to achieve their destiny; undermine civilization through assassination, theft, and other societal ills

**Religious Symbol** eye of Aroden

**Sacred Animal** rabbit

**Sacred Colors** green, gold

**Source:** `= this.source` (`= this.source-type`)
