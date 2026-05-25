---
type: deity
source-type: "Remaster"
domains: "Duty, Perfection, Trickery, Zeal"
favored-weapon: "Tekko-kagi"
divine-font: "Harm, Heal"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Mindlink]], Rank 4: [[Translocate]], Rank 5: [[Strange Geometry]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** The Warrior Queen

**Areas of Concern** Battle, strategy, geometry

**Edicts** Study the art of warfare and strategy, strive to take and maintain control of your situation, hunt and slay hounds of Tindalos

**Anathema** Let your emotions dictate your tactics, hunt felines for sport, permit others of your rank or lower to calculate tactics on your behalf

**Religious Symbol** moon and bow with compass arrow

**Sacred Animal** lion

**Sacred Colors** orange, blue

**Source:** `= this.source` (`= this.source-type`)
