---
type: deity
source-type: "Remaster"
domains: "Air, Moon, Protection, Sun"
favored-weapon: "Khopesh"
divine-font: "Heal"
divine-skill: "Diplomacy"
divine-spells: "Rank 1: [[Carryall]], Rank 3: [[Wall Of Wind]], Rank 4: [[Aerial Form]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Horus is the Osirian god of the sky, whose eyes are the sun and the moon, whose feathers are the stars, and whose wings are the sky. As Horakhty (meaning Horus of the Two Horizons), he is a deity of the rising and setting suns. Horus is said to be the legendary ruler of Osirion during the Age of Anguish, and is also a god of pharaohs.

**Title** The Distant Falcon

**Areas of Concern** Rulership, the sky, the sun

**Edicts** Protect those you have authority over, maintain harmony in your community

**Anathema** Undermine a rightful ruler, knowingly serve a usurper

**Religious Symbol** eye of Horus

**Sacred Animal** falcon

**Sacred Colors** blue, white

**Source:** `= this.source` (`= this.source-type`)
