---
type: deity
source-type: "Remaster"
domains: "Ambition, Destruction, Earth, Undeath"
favored-weapon: "Naginata"
divine-font: "Harm"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Grim Tendrils]], Rank 2: [[Feast Of Ashes]], Rank 7: [[Possession]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Fumeiyoshi is a Tian Xia deity most often associated with the undead and graves, although he is also the patron deity of the evil oni.

**Title** Lord of Envy

**Areas of Concern** Envy, graves, infamy, undead

**Edicts** Punish those who have good fortune they don't deserve, devour the pleasures of the living, encourage resentment, make graveyards supernaturally unsafe

**Anathema** Pass by food without stealing a bite, allow honor or tradition to prevent you from taking what you want

**Religious Symbol** red demonic face

**Sacred Animal** snake

**Sacred Colors** red, yellow

**Source:** `= this.source` (`= this.source-type`)
