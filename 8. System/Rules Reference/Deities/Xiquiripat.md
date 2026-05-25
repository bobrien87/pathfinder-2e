---
type: deity
source-type: "Remaster"
domains: "Air, Destruction, Might, Zeal"
favored-weapon: "Macuahuitl"
divine-font: "Harm"
divine-skill: "Acrobatics"
divine-spells: "Rank 1: [[Gust Of Wind]], Rank 3: [[Blazing Dive]], Rank 5: [[Impaling Spike]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Trapped deep beneath the Black Pyramid of Xibalba lives an embodiment of destruction known as the Flying Scab. Few have seen Xiquiripat and lived to tell tales of their constantly shifting guise, which changes from waves of congealed blood to a knot of fanged lampreys to a heaving mass of matted hair. Though this god's form is fluid, their goals are less so, as Xiquiripat has had only one unbending desire since the dawn of their existence: to instill fear into every living thing they meet before condemning them to oblivion.

**Title** The Flying Scab

**Areas of Concern** Evisceration, fatal falls, massacres

**Edicts** Never show mercy, pursue your enemies to their end or yours, teach all to fear you

**Anathema** Accept surrender from an enemy, show cowardice or weakness

**Religious Symbol** metal sphere covered in bloody spikes

**Sacred Animal** shrike

**Sacred Colors** black, purple

**Source:** `= this.source` (`= this.source-type`)
