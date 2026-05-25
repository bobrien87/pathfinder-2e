---
type: deity
source-type: "Remaster"
domains: "Decay, Nightmares, Void, Time"
favored-weapon: "Sickle"
divine-font: "Harm"
divine-skill: "Occultism"
divine-spells: "Rank 1: [[Sleep]], Rank 3: [[One With Stone]], Rank 6: [[Phantasmal Calamity]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Rhan-Tegoth, last to sleep and first to wake, is a Great Old One tasked with being the forerunner of the end of all things. Many centuries ago, Rhan-Tegoth ruled a mighty empire on a far-flung world. When its subjects turned away from its rule, it did not retaliate; instead, it entered a hibernation state, transforming into a stone effigy. In the eons since, the Herald has amassed followers across the Universe and beyond, each cult subtly guided by Rhan-Tegoth's terrible influence. Though some of these groups seek to hasten their god's awakening, such an act—in the rare case of its success—has invariably resulted in the devouring of all those involved before the Herald simply returns to its timeless slumber.

**Title** Herald of the End Times

**Areas of Concern** Hibernation, immortality, ruin

**Edicts** Create statues of Rhan-Tegoth, sacrifice living sentient creatures

**Anathema** None

**Religious Symbol** three black stars

**Sacred Animal** none

**Sacred Colors** black, purple

**Source:** `= this.source` (`= this.source-type`)
