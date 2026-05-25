---
type: deity
source-type: "Remaster"
domains: "Healing, Magic, Nature, Protection"
favored-weapon: "Staff"
divine-font: "Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Summon Plant Or Fungus]], Rank 2: [[One With Plants]], Rank 8: [[Burning Blossoms]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Arundhat is a goddess of the Vudran pantheon known as the bringer of blossoms and scent.

**Title** The Sacred Perfume

**Areas of Concern** Blossoms, diplomacy, scent

**Edicts** Offer appropriate flowers to other divinities, practice herbalism, tend to sacred flowers

**Anathema** Dispose of waste near flowers, dispose of withered flowers improperly, harvest flowers without offering the proper prayers

**Religious Symbol** lamp with flower as flame

**Sacred Animal** sunbird

**Sacred Colors** pink, white

**Source:** `= this.source` (`= this.source-type`)
