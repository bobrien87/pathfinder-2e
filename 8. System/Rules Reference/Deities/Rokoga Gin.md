---
type: deity
source-type: "Remaster"
domains: "Cities, Freedom, Protection, Travel"
favored-weapon: "Hand-cannon"
divine-font: "Harm, Heal"
divine-skill: "Acrobatics"
divine-spells: "Rank 1: [[Fleet Step]], Rank 3: [[Haste]], Rank 7: [[True Target]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** The World Walker

**Areas of Concern** Travelers, firearms, martial arts

**Edicts** Seek new horizons, protect travelers on the road, learn something new each day

**Anathema** Willingly stay in one place for longer than your duty requires, accost travelers

**Religious Symbol** nunchaku made from two linked hand cannons

**Sacred Animal** horse

**Sacred Colors** blue, gray

**Source:** `= this.source` (`= this.source-type`)
