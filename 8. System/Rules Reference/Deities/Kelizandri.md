---
type: deity
source-type: "Remaster"
domains: "Destruction, Nightmares, Travel, Water"
favored-weapon: "Trident"
divine-font: "Harm"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Hydraulic Push]], Rank 2: [[Summon Elemental]], Rank 4: [[Hydraulic Torrent]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Kelizandri, the elemental lord of water, oversees the deep sea, waves, and drowning. The Brackish Emperor claims to be the offspring of an ancient god and a brine dragon, and he usually takes the form of an immense aquatic dragon with metallic scales and crystalline talons. He spends much of his time slumbering in his magnificent Palace of Salt and Bones, entertaining himself with rampages of wanton destruction and conquest whenever he wakes. The lord's domain on the Plane of Water is the Brackish Empire Kelizandrika, a conglomeration of affiliated brine dragon–controlled realms. The most powerful dragons of Kelizandrika's ruling councils are said to advise the elemental lord personally.

**Title** The Brackish Emperor

**Areas of Concern** Drowning, water, waves

**Edicts** Instill hydrophobia in others, kill your foes by drowning them, sacrifice treasures to the depths of the ocean

**Anathema** Destroy a body of water, use magic to calm the waves

**Religious Symbol** notched shark's fin

**Sacred Animal** great white shark

**Sacred Colors** blue, green

**Source:** `= this.source` (`= this.source-type`)
