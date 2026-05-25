---
type: deity
source-type: "Remaster"
domains: "Darkness, Luck, Swarm, Trickery"
favored-weapon: "Dagger, Shuriken-drone"
divine-font: "Harm"
divine-skill: "Thievery"
divine-spells: "Rank 1: [[Summon Animal]], Rank 2: [[Knock]], Rank 3: [[Veil Of Privacy]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** Old Rat Woman

**Areas of Concern** Night, rats, thieves

**Edicts** Work quietly toward your goals in the shadows, steal what you need, keep an ear among the ignored and downtrodden

**Anathema** Work honestly for something you could steal instead, risk too much for another creature

**Religious Symbol** emaciated rat

**Sacred Animal** rat

**Sacred Colors** black, green

**Source:** `= this.source` (`= this.source-type`)
