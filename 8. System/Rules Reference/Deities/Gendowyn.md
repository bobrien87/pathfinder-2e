---
type: deity
source-type: "Remaster"
domains: "Earth, Family, Luck, Nature"
favored-weapon: "Whip"
divine-font: "Heal"
divine-skill: "Stealth"
divine-spells: "Rank 1: [[Summon Fey]], Rank 2: [[Oaken Resilience]], Rank 5: [[Nature'S Pathway]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** Lady of the Fangwood

**Areas of Concern** Fangwood Forest

**Edicts** Preserve primal areas, destroy blighted fey and agents of Cyth-V'sug, protect those who placate you with offerings

**Anathema** Parley or make a deal with fiends, forgive those who deceive you, harm an innocent child

**Religious Symbol** flower eye surrounded by vine wreath

**Sacred Animal** doe

**Sacred Colors** green, purple

**Source:** `= this.source` (`= this.source-type`)
