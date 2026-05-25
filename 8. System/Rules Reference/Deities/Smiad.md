---
type: deity
source-type: "Remaster"
domains: "Confidence, Wyrmkin, Might, Zeal"
favored-weapon: "Greatsword"
divine-font: "Heal"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Sure Strike]], Rank 4: [[Fire Shield]], Rank 6: [[Disintegrate]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** The Pitiless Dragonslayer

**Areas of Concern** Dragon-hunting, honor, renown

**Edicts** Slay evil dragons, aid benevolent dragons, train others in dragonslaying techniques

**Anathema** Accept the words of an evil dragon as truth, allow benevolent dragons to be harmed by your actions or inaction, fail to teach others the differences between dragons

**Religious Symbol** slain dragon

**Sacred Animal** heron

**Sacred Colors** gold, red

**Source:** `= this.source` (`= this.source-type`)
