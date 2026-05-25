---
type: deity
source-type: "Remaster"
domains: "Decay, Delirium, Nature, Nightmares"
favored-weapon: "Scythe"
divine-font: "Harm, Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Summon Plant Or Fungus]], Rank 3: [[Wall Of Thorns]], Rank 5: [[Plant Form]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

A rare few of those who've indulged in psychoactive plants have been met with horrifying visions of an old woman made of gnarled vines and roots, her sneering mouth full of fang-like thorns and pollen. Those unfortunate enough to meet Vermilion Mother are stalked in their sleep, choked nightly by her dream of a world overrun by plants and fungi. This sahkil tormentor cares little for those of flesh and blood, only that their bodies make for excellent fertilizer.

**Title** The Endless Root

**Areas of Concern** Fecundity, overgrown places, psychoactive plants

**Edicts** Indulge in substances derived from psychoactive plants, kill any who would pollute without mercy, protect endangered plants above all else

**Anathema** Alter a piece of unspoiled land, purposely destroy plants

**Religious Symbol** flower studded with bloody fangs

**Sacred Animal** moth

**Sacred Colors** brown, red

**Source:** `= this.source` (`= this.source-type`)
