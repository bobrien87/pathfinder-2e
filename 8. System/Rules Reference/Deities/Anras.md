---
type: deity
source-type: "Remaster"
domains: "Air, Fate, Moon, Sun"
favored-weapon: "Bo-staff"
divine-font: "Heal"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Thunderstrike]], Rank 3: [[Wall Of Wind]], Rank 6: [[Chain Lightning]]"
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** Mother Sky

**Areas of Concern** Astronomy, prediction, weather

**Edicts** Seek new discoveries in the night sky, make weather predictions, help prepare locals for storms

**Anathema** Attempt to control the weather, force a prediction to come true, curse the coming of bad weather

**Religious Symbol** Parting clouds against a starry sky

**Sacred Animal** Mouse

**Sacred Colors** Black, silver

**Source:** `= this.source` (`= this.source-type`)
