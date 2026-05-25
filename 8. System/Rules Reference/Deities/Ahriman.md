---
type: deity
source-type: "Remaster"
domains: "Darkness, Death, Destruction, Trickery"
favored-weapon: "Whip"
divine-font: "Harm"
divine-skill: "Deception"
divine-spells: "Rank 1: [[Ill Omen]], Rank 2: [[Shatter]], Rank 5: [[Wave Of Despair]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The dread shadow known as Ahriman counts servants mainly among div as well as a scattering of followers throughout the mortal realm.

**Title** Lord of the Divs

**Areas of Concern** Destruction, divs, nihilism

**Edicts** Foil rulers, the proud, and the powerful; ruin anything created by mortals

**Anathema** Create arts or crafts, serve a mortal, assist in mortal aims except to subvert and corrupt them

**Religious Symbol** black and silver eclipse

**Sacred Animal** snake

**Sacred Colors** black, silver

**Source:** `= this.source` (`= this.source-type`)
