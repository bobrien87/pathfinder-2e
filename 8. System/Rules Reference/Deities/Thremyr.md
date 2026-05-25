---
type: deity
source-type: "Remaster"
domains: "Cold, Creation, Water, Zeal"
favored-weapon: "Greataxe"
divine-font: "Harm"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Sleep]], Rank 5: [[Mantle Of The Frozen Heart]], Rank 7: [[Frigid Flurry]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Thremyr is a mountainous, ancient being with a long, full beard and hair of salt, a stout body of frigid ice, and a set of chilling blue gems for eyes. The earliest available records of the god tell the tale of his awakening during Earthfall as the meteorite landed on Golarion, tearing open the Inner Sea. Anything prior to that is currently undocumented or lost as a result of this cataclysmic event.

**Title** The First Jarl

**Areas of Concern** Ice, salt, tribute

**Edicts** Take any valuables you come across, fiercely defend your treasure, never back down from a fight

**Anathema** Show anyone in your command favoritism, give up any of your own treasures, take the Test of the Starstone

**Religious Symbol** frozen blue gemstone

**Sacred Animal** wooly rhinoceros

**Sacred Colors** icy blue, white

**Source:** `= this.source` (`= this.source-type`)
