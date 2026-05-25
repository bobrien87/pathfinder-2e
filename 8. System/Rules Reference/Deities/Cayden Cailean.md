---
type: deity
source-type: "Remaster"
domains: "Cities, Freedom, Indulgence, Might"
favored-weapon: "Rapier"
divine-font: "Heal"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Fleet Step]], Rank 2: [[Stupefy]], Rank 5: [[Hallucination]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Cayden Cailean is the deity of freedom, bravery, and alcoholic drinks. Alongside Iomedae and Norgorber, he is one of the Ascended—three mortals who reached godhood after conquering the Test of the Starstone. In life, Cayden Cailean was a sellsword notorious for his indomitable spirit, adherence to his moral code, and unbridled revelry. It was precisely during a night of riotous celebration that he entered the Starstone Cathedral as part of a dare, first to the amusement and later to the concern of his fellow partygoers. Three days later, he emerged from the deadly maze, laughing, still intoxicated, and having achieved divinity. Deific power did little to change Cayden Cailean's personality and habits. He continued enjoying a good drink while surrounded by allies and friends, flirting with people, roaming the land in search of adventure, and defending underdogs.

**Title** The Accidental God

**Areas of Concern** ale, bravery, freedom, wine

**Edicts** drink, aid the oppressed, seek glory and adventure

**Anathema** waste alcohol, be mean or standoffish when drunk, oppress the vulnerable

**Religious Symbol** tankard

**Sacred Animal** hound

**Sacred Colors** silver, tan

**Source:** `= this.source` (`= this.source-type`)
