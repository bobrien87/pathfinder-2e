---
type: deity
source-type: "Remaster"
domains: "Earth, Might, Protection, Repose"
favored-weapon: "Greatsword"
divine-font: "Harm, Heal"
divine-skill: "Crafting"
divine-spells: "Rank 1: [[Shattering Gem]], Rank 4: [[Shape Stone]], Rank 5: [[Wall Of Stone]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Ashukharma is the Vudran goddess of canyons and cliffs. She is the jilted lover of Dinehdal, god of mountain peaks, and lover of Matravash, goddess of the Matra River; her tale draws prayers from scorned lovers and those dealing with rifts between themselves and their friends or families.

**Title** The Divine Divide

**Areas of Concern** Canyons, cliffs, gorges, ravines

**Edicts** Hinder travel, create and enforce physical and emotional boundaries, build defensive earthworks

**Anathema** Destroy a natural barrier, pursue a personal relationship after being refused, betray a lover

**Religious Symbol** a deep, jagged gorge in dry earth

**Sacred Animal** goat

**Sacred Colors** green, orange

**Source:** `= this.source` (`= this.source-type`)
