---
type: deity
source-type: "Remaster"
domains: "Creation, Fire, Metal, Truth"
favored-weapon: "Staff"
divine-font: "Heal"
divine-skill: "Crafting"
divine-spells: "Rank 1: [[Temporary Tool]], Rank 6: [[Wall Of Metal]], Rank 8: [[Ferrous Form]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** Lord of Eternity

**Areas of Concern** Architecture, craftsmanship, creation, metalworking

**Edicts** Craft your ideas into reality, encourage stability, listen to prayers, perform ceremonies as needed

**Anathema** Make shoddy or unsafe buildings, lie, enforce injustice, violate the protection of Ptah

**Religious Symbol** staff composed of the ankh, djed, and wax

**Sacred Animal** bull

**Sacred Colors** blue, green

**Source:** `= this.source` (`= this.source-type`)
