---
type: deity
source-type: "Remaster"
domains: "Indulgence, Luck, Nature, Swarm"
favored-weapon: "Club"
divine-font: "Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Summon Plant Or Fungus]], Rank 2: [[Stupefy]], Rank 4: [[Speak With Plants]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Halcamora is an agathion empyreal lord who watches over gardens, parks, and wineries.

**Title** Lady of Ripe Bounty

**Areas of Concern** Gardens, orchards, wine

**Edicts** Cultivate gardens, share wine, keep helpful insects, teach others to farm

**Anathema** Salt or despoil the earth, spread plague or pestilence, carelessly use pesticides

**Religious Symbol** Jug of grapes

**Sacred Animal** Ladybug

**Sacred Colors** red, white

**Source:** `= this.source` (`= this.source-type`)
