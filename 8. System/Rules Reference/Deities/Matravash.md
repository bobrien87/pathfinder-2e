---
type: deity
source-type: "Remaster"
domains: "Cities, Nature, Travel, Water"
favored-weapon: "Whip"
divine-font: "Heal"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Share Lore]], Rank 3: [[Slow]], Rank 4: [[Hydraulic Torrent]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** The Wide Water

**Areas of Concern** Matra River

**Edicts** Aid the persecuted, accommodate and facilitate others, practice contemplation and restraint

**Anathema** Destroy lotus fields, interfere with the flow of the Matra river, pollute clean water, reveal the location of non-evil fugitives

**Religious Symbol** lotus blossom floating on a winding river

**Sacred Animal** fish

**Sacred Colors** blue, pink

**Source:** `= this.source` (`= this.source-type`)
