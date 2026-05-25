---
type: deity
source-type: "Remaster"
domains: "Confidence, Nightmares, Protection, Travel"
favored-weapon: "Shortsword"
divine-font: "Heal"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Tailwind]], Rank 3: [[Haste]], Rank 7: [[Mask Of Terror]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Jaidz is a powerful agathion Empyreal lord who seeks to inspire courage in the cowardly and immature through compassion and guidance.

**Title** Fearless Claw

**Areas of Concern** Cowards, the untested, youths

**Edicts** Forgive cowards and offer them guidance, encourage others to test their mettle, face and learn from your fears

**Anathema** Punish another creature for cowardice, routinely avoid that which scares you

**Religious Symbol** Path between two trees

**Sacred Animal** black tiger

**Sacred Colors** brown, green

**Source:** `= this.source` (`= this.source-type`)
