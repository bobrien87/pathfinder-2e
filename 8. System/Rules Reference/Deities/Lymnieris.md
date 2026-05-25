---
type: deity
source-type: "Remaster"
domains: "Change, Passion, Protection, Repose"
favored-weapon: "Longsword"
divine-font: "Heal"
divine-skill: "Society"
divine-spells: "Rank 1: [[Leaden Steps]], Rank 3: [[Threefold Aspect]], Rank 4: [[Containment]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** The Auroral Tower

**Areas of Concern** Rites of passage, sex workers, virginity

**Edicts** Help others achieve their desires, aid and protect sex workers, help others through difficult transitions

**Anathema** Persecute sex workers, force or support unwanted marriages

**Religious Symbol** White-hooded profile

**Sacred Animal** Rabbit

**Sacred Colors** Red, white

**Source:** `= this.source` (`= this.source-type`)
