---
type: deity
source-type: "Remaster"
domains: "Fate, Naga, Sorrow, Truth"
favored-weapon: "Jaws, Light-mace"
divine-font: "Harm"
divine-skill: "Occultism"
divine-spells: "Rank 1: [[Charm]], Rank 2: [[Animal Form]], Rank 4: [[Clairvoyance]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The Mother of Nagas, the Karmic Pillar, and the Chalice-Bearer of the danavas, Ravithra was decapitated and brought low by treachery. She grants boons only to mortal champions who seek to topple the treacherous and to restore her to her rightful role.

**Title** The Chalice-Bearer

**Areas of Concern** Judgment, karma, law, vengeance

**Edicts** Enforce karma's pitiless judgment, shame fools, kill traitors, pursue the Chalice of Amrit

**Anathema** Make decisions erratically or randomly, provide aid to Vasaghati or her followers, engage in treachery

**Religious Symbol** gilded sun wheel

**Sacred Animal** snake

**Sacred Colors** silver, white

**Source:** `= this.source` (`= this.source-type`)
