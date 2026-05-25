---
type: deity
source-type: "Remaster"
domains: "Darkness, Destruction, Wyrmkin, Water"
favored-weapon: "Dagger"
divine-font: "Harm"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Grim Tendrils]], Rank 4: [[Hydraulic Torrent]], Rank 8: [[Monstrosity Form]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** Devourer of the Dawn

**Areas of Concern** Chaos, darkness, destruction, snakes

**Edicts** Destroy boats and ships, create lethal hazards in water, extinguish lights, spread chaos, destroy the world

**Anathema** Aid a sun god or their servants, rescue a creature from drowning

**Religious Symbol** coiled serpent

**Sacred Animal** snake

**Sacred Colors** blue, white

**Source:** `= this.source` (`= this.source-type`)
