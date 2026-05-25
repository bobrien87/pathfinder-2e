---
type: deity
source-type: "Remaster"
domains: "Destruction, Nature, Nightmares, Tyranny"
favored-weapon: "Greataxe"
divine-font: "Harm, Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Grim Tendrils]], Rank 3: [[Wall Of Thorns]], Rank 6: [[Tangling Creepers]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Treerazer, the Lord of the Blasted Tarn, first came to Golarion thousands of years ago after being forced to flee the Outer Rifts when his attempt to seize control of the demonic realm of Jeharlu from his father Cyth-V'sug failed spectacularly. Reduced in power to that of a nascent demon lord, Treerazer spent some time lying low before turning his attention to the abandoned elven lands of Kyonin. When his attempt to corrupt that realm resulted in the elves' return to defend their home and oppose his pestilent influence, Treerazer was forced to retreat again to the depths of a fetid swampland known as Tanglebriar.

**Title** Lord of the Blasted Tarn

**Areas of Concern** corruption of nature, pollution, slaughter of elves

**Edicts** corrupt plant life with evil or fungal influences, feast on rotten flesh or fungus, slay elves

**Anathema** grant mercy to elves, plant trees, encourage natural plant growth

**Religious Symbol** axe stuck into a bleeding tree stump

**Sacred Animal** deinonychus

**Sacred Colors** black, green

**Source:** `= this.source` (`= this.source-type`)
