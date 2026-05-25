---
type: deity
source-type: "Remaster"
domains: "Darkness, Duty, Nature, Zeal"
favored-weapon: "Kukri"
divine-font: "Heal"
divine-skill: "Stealth"
divine-spells: "Rank 1: [[Vanishing Tracks]], Rank 3: [[Animal Vision]], Rank 4: [[Aerial Form]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** The Aurulent Eye

**Areas of Concern** Night, owls, watchfulness

**Edicts** Defend rightful borders, scout or patrol for evil, wait to strike until you have the advantage

**Anathema** Abandon your post, tolerate poaching, torment animals

**Religious Symbol** shadowed golden eye

**Sacred Animal** owl

**Sacred Colors** black, gold

**Source:** `= this.source` (`= this.source-type`)
