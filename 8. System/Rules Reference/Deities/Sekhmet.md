---
type: deity
source-type: "Remaster"
domains: "Destruction, Healing, Indulgence, Might"
favored-weapon: "Claw, Battle-axe"
divine-font: "Harm, Heal"
divine-skill: "Medicine"
divine-spells: "Rank 1: [[Sure Strike]], Rank 4: [[Wall Of Fire]], Rank 5: [[Moon Frenzy]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** Lady of Slaughter

**Areas of Concern** Fire, healing, vengeance, war

**Edicts** Slaughter your enemies, drink the blood of defeated foes, heal battle injuries

**Anathema** Spare an evil fiend, fail to placate Sekhmet with daily rituals

**Religious Symbol** seven arrows

**Sacred Animal** lion

**Sacred Colors** green, red

**Source:** `= this.source` (`= this.source-type`)
