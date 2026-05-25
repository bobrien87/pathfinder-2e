---
type: deity
source-type: "Remaster"
domains: "Ambition, Cities, Creation, Secrecy"
favored-weapon: "Crossbow"
divine-font: "Harm"
divine-skill: "Crafting"
divine-spells: "Rank 1: [[Gentle Landing]], Rank 3: [[Cozy Cabin]], Rank 4: [[Weapon Storm]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Perched atop the Watch of Arocard, Malthus surveys his grand works of architecture, expansion, and waste. His form is that of an ashen man with the torso of an ibis and five insidious beaks. He observes, unmoving, for such long spans that regolith accumulates upon his crest—a crust that crumbles off like shale as he takes flight. Since mortals first piled earth to make walls, Malthus has manipulated them to his coordination. From his five beaks, he promises favor for small, subtle design modifications that in their singular instance are innocuous. From up above, the buildings across continents and built over generations begin to make greater patterns of infernal geometry. Countless sigils waiting to be exploited are hidden in plain sight, their purpose known only to the Five-Beaked above and below.

**Title** The Five-Beaked

**Areas of Concern** Architecture, expansion, waste

**Edicts** Scan your surroundings from above, join form with function, waste as an act of luxury

**Anathema** Take impulsive action, demolish buildings, take in moderation

**Religious Symbol** five crossed arrows

**Sacred Animal** parrot

**Sacred Colors** blue, red

**Source:** `= this.source` (`= this.source-type`)
